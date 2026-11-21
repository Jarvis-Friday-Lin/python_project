"""A 股日线技术分析：运行后生成 Excel 报告。

示例：python3 a_share_analysis.py --code 600519
也可以使用本地 CSV：python3 a_share_analysis.py --code 600519 --input data.csv
"""
import argparse
import json
import math
import os
import ssl
import urllib.parse
import urllib.request
import zipfile
import time
from datetime import datetime
from xml.sax.saxutils import escape

import numpy as np
import pandas as pd

# 默认分析的股票代码：直接修改这一行即可更换股票。
DEFAULT_CODE = "601318"
KNOWN_NAMES = {"601318": "中国平安"}


def fetch_eastmoney(code, days=260):
    secid = ("1." if code.startswith(("6", "9")) else "0.") + code
    params = {"secid": secid, "klt": "101", "fqt": "1", "beg": "0", "end": "20500101",
              "lmt": str(days), "fields1": "f1", "fields2": "f51,f52,f53,f54,f55,f56,f57,f58,f59,f60,f61"}
    params["ut"] = "fa5fd1943c7b386f172d6893dbfba10b"
    url = "https://push2his.eastmoney.com/api/qt/stock/kline/get?" + urllib.parse.urlencode(params)
    headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/124 Safari/537.36",
               "Accept": "application/json,text/plain,*/*", "Referer": "https://quote.eastmoney.com/"}
    context = ssl._create_unverified_context()
    last_error = None
    for attempt in range(3):
        try:
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req, timeout=20, context=context) as response:
                payload = json.loads(response.read().decode("utf-8"))
            break
        except Exception as exc:
            last_error = exc
            if attempt < 2:
                time.sleep(1.5 * (attempt + 1))
    else:
        raise RuntimeError(f"行情接口连续 3 次未响应：{last_error}")
    if not payload.get("data") or not payload["data"].get("klines"):
        raise RuntimeError("接口没有返回行情数据，请检查股票代码。")
    rows = []
    for line in payload["data"]["klines"]:
        x = line.split(",")
        rows.append({"date": x[0], "open": x[1], "close": x[2], "high": x[3], "low": x[4],
                     "volume": x[5], "amount": x[6], "amplitude": x[7], "pct_change": x[8],
                     "change": x[9], "turnover": x[10]})
    result = pd.DataFrame(rows)
    result.attrs["stock_name"] = payload["data"].get("name") or KNOWN_NAMES.get(code, code)
    return result


def fetch_tencent(code, days=260):
    """东方财富不可用时，使用腾讯证券日线接口作为备用来源。"""
    market = "sh" if code.startswith(("6", "9")) else "sz"
    url = f"https://web.ifzq.gtimg.cn/appstock/app/fqkline/get?param={market}{code},day,,,{days},qfq"
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0", "Referer": "https://gu.qq.com/"})
    with urllib.request.urlopen(req, timeout=20, context=ssl._create_unverified_context()) as response:
        payload = json.loads(response.read().decode("utf-8"))
    rows = payload.get("data", {}).get(f"{market}{code}", {}).get("qfqday", [])
    if not rows:
        raise RuntimeError("腾讯证券接口没有返回行情数据")
    result = pd.DataFrame(rows, columns=["date", "open", "close", "high", "low", "volume"])
    result["turnover"] = np.nan
    result.attrs["stock_name"] = KNOWN_NAMES.get(code, code)
    return result


def load_data(code, input_file=None):
    if input_file:
        data = pd.read_csv(input_file)
    else:
        try:
            data = fetch_eastmoney(code)
        except Exception as eastmoney_error:
            print(f"东方财富接口不可用，切换腾讯证券接口：{eastmoney_error}")
            try:
                data = fetch_tencent(code)
            except Exception as tencent_error:
                raise RuntimeError(f"东方财富和腾讯证券接口均不可用；腾讯错误：{tencent_error}") from tencent_error
    required = {"date", "open", "close", "high", "low", "volume"}
    missing = required - set(data.columns)
    if missing:
        raise ValueError("输入数据缺少字段：" + ", ".join(sorted(missing)))
    for col in ["open", "close", "high", "low", "volume", "amount", "pct_change", "turnover"]:
        if col in data:
            data[col] = pd.to_numeric(data[col], errors="coerce")
    data["date"] = pd.to_datetime(data["date"])
    data.attrs.setdefault("stock_name", KNOWN_NAMES.get(code, code))
    return data.sort_values("date").reset_index(drop=True)


def add_indicators(d):
    d = d.copy()
    d["pct_change"] = d.get("pct_change", d["close"].pct_change() * 100)
    d["turnover"] = d.get("turnover", np.nan)
    d["volume_ma5"] = d["volume"].rolling(5).mean()
    d["volume_ma20"] = d["volume"].rolling(20).mean()
    for n in [5, 10, 20, 60]: d[f"ma{n}"] = d["close"].rolling(n).mean()
    ema12 = d["close"].ewm(span=12, adjust=False).mean()
    ema26 = d["close"].ewm(span=26, adjust=False).mean()
    d["dif"] = ema12 - ema26
    d["dea"] = d["dif"].ewm(span=9, adjust=False).mean()
    d["macd"] = (d["dif"] - d["dea"]) * 2
    low9, high9 = d["low"].rolling(9).min(), d["high"].rolling(9).max()
    rsv = (d["close"] - low9) / (high9 - low9) * 100
    d["k"] = rsv.ewm(com=2, adjust=False).mean()
    d["d"] = d["k"].ewm(com=2, adjust=False).mean()
    d["j"] = 3 * d["k"] - 2 * d["d"]
    delta = d["close"].diff(); gain = delta.clip(lower=0); loss = -delta.clip(upper=0)
    for n in [6, 12, 24]:
        avg_gain, avg_loss = gain.rolling(n).mean(), loss.rolling(n).mean()
        d[f"rsi{n}"] = 100 - 100 / (1 + avg_gain / avg_loss.replace(0, np.nan))
    d["boll_mid"] = d["close"].rolling(20).mean()
    std = d["close"].rolling(20).std()
    d["boll_up"], d["boll_low"] = d["boll_mid"] + 2 * std, d["boll_mid"] - 2 * std
    body = (d["close"] - d["open"]).abs(); rng = (d["high"] - d["low"]).replace(0, np.nan)
    d["kline_body"] = body; d["upper_shadow"] = d["high"] - d[["open", "close"]].max(axis=1)
    d["lower_shadow"] = d[["open", "close"]].min(axis=1) - d["low"]
    d["kline_pattern"] = np.select(
        [(body / rng < .1), (d["lower_shadow"] > body * 2) & (d["upper_shadow"] < body),
         (d["upper_shadow"] > body * 2) & (d["lower_shadow"] < body)],
        ["十字星", "长下影/锤头倾向", "长上影"], default="普通K线")
    # 规则化背离：当前窗口价格创近期高/低，但指标没有同步创高/低。
    win = 20
    price_high, price_low = d["close"].rolling(win).max(), d["close"].rolling(win).min()
    rsi_high, rsi_low = d["rsi6"].rolling(win).max(), d["rsi6"].rolling(win).min()
    macd_high, macd_low = d["macd"].rolling(win).max(), d["macd"].rolling(win).min()
    d["top_divergence"] = (d["close"] >= price_high) & ((d["rsi6"] < rsi_high.shift(1)) | (d["macd"] < macd_high.shift(1)))
    d["bottom_divergence"] = (d["close"] <= price_low) & ((d["rsi6"] > rsi_low.shift(1)) | (d["macd"] > macd_low.shift(1)))
    return d


def conclusion(d, stock_name=""):
    x = d.iloc[-1]; score, reasons, risks = 0, [], []
    if x["close"] > x["ma20"]: score += 1; reasons.append("收盘价在 MA20 上方")
    else: score -= 1; reasons.append("收盘价在 MA20 下方")
    if x["dif"] > x["dea"]: score += 1; reasons.append("MACD DIF 在 DEA 上方")
    else: score -= 1; reasons.append("MACD DIF 在 DEA 下方")
    if x["k"] > x["d"]: score += 1; reasons.append("KDJ K 在 D 上方")
    else: score -= 1; reasons.append("KDJ K 在 D 下方")
    if 30 <= x["rsi6"] <= 70: reasons.append("RSI6 未处于极端区间")
    elif x["rsi6"] > 70: score -= 1; risks.append("RSI6 超买，追高风险较大")
    else: score += 1; reasons.append("RSI6 偏低，存在反弹观察价值")
    if x["close"] > x["boll_up"]: score -= 1; risks.append("收盘价突破布林上轨，注意回撤")
    elif x["close"] < x["boll_low"]: score += 1; reasons.append("收盘价跌破布林下轨，关注超跌")
    if x["top_divergence"]: score -= 2; risks.append("出现规则化顶背离信号")
    if x["bottom_divergence"]: score += 2; reasons.append("出现规则化底背离信号")
    advice = "偏多观察" if score >= 2 else "偏空观察" if score <= -2 else "震荡/观望"
    latest_date = pd.to_datetime(x["date"]).strftime("%Y-%m-%d")
    return pd.DataFrame([{"股票名称": stock_name, "股票代码": "", "最新日期": latest_date,
                          "最新收盘": x["close"], "涨跌幅(%)": x["pct_change"],
                          "成交量": x["volume"], "换手率(%)": x["turnover"],
                          "MA5": x["ma5"], "MA10": x["ma10"], "MA20": x["ma20"], "MA60": x["ma60"],
                          "DIF": x["dif"], "DEA": x["dea"], "MACD柱": x["macd"],
                          "K": x["k"], "D": x["d"], "J": x["j"],
                          "RSI6": x["rsi6"], "RSI12": x["rsi12"], "RSI24": x["rsi24"],
                          "BOLL上轨": x["boll_up"], "BOLL中轨": x["boll_mid"], "BOLL下轨": x["boll_low"],
                          "K线形态": x["kline_pattern"], "顶背离": "是" if x["top_divergence"] else "否",
                          "底背离": "是" if x["bottom_divergence"] else "否", "综合评分": score, "结论": advice,
                          "支持理由": "；".join(reasons), "风险提示": "；".join(risks) or "指标未发现明显额外风险；仍需止损和仓位控制。"}])


def write_xlsx(path, sheets):
    """无第三方 Excel 引擎时，直接写入最小可用的 xlsx 文件。"""
    def cell(v):
        if pd.isna(v): return "<c/>"
        if isinstance(v, (int, float, np.number)) and not isinstance(v, bool) and math.isfinite(float(v)):
            return f'<c t="n"><v>{float(v)}</v></c>'
        return f'<c t="inlineStr"><is><t>{escape(str(v))}</t></is></c>'
    with zipfile.ZipFile(path, "w", zipfile.ZIP_DEFLATED) as z:
        z.writestr("[Content_Types].xml", '<?xml version="1.0"?><Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types"><Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/><Default Extension="xml" ContentType="application/xml"/><Override PartName="/xl/workbook.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet.main+xml"/><Override PartName="/xl/styles.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.styles+xml"/></Types>')
        z.writestr("_rels/.rels", '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships"><Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="xl/workbook.xml"/></Relationships>')
        rels = ''.join(f'<Relationship Id="rId{i+1}" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/worksheet" Target="worksheets/sheet{i+1}.xml"/>' for i in range(len(sheets)))
        z.writestr("xl/_rels/workbook.xml.rels", f'<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">{rels}</Relationships>')
        names = list(sheets)
        z.writestr("xl/workbook.xml", '<workbook xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships"><sheets>' + ''.join(f'<sheet name="{escape(n)}" sheetId="{i+1}" r:id="rId{i+1}"/>' for i,n in enumerate(names)) + '</sheets></workbook>')
        z.writestr("xl/styles.xml", '<styleSheet xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main"><fonts count="1"><font><sz val="11"/><name val="Calibri"/></font></fonts><fills count="1"><fill><patternFill patternType="none"/></fill></fills><borders count="1"><border/></borders><cellXfs count="1"><xf/></cellXfs></styleSheet>')
        for i, (name, frame) in enumerate(sheets.items(), 1):
            rows = [list(frame.columns)] + frame.astype(object).values.tolist()
            xml = '<worksheet xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main"><sheetData>'
            for r, row in enumerate(rows, 1): xml += f'<row r="{r}">' + ''.join(cell(v) for v in row) + '</row>'
            z.writestr(f"xl/worksheets/sheet{i}.xml", xml + '</sheetData></worksheet>')


def main():
    p = argparse.ArgumentParser(description="A 股技术指标分析并导出 Excel")
    p.add_argument("--code", default=DEFAULT_CODE, help="股票代码，如 000001")
    p.add_argument("--input", help="可选：本地 CSV，列名需含 date/open/close/high/low/volume")
    p.add_argument("--output", help="输出 xlsx 路径")
    args = p.parse_args()
    try:
        data = add_indicators(load_data(args.code, args.input))
    except Exception as e:
        print(f"获取/读取行情失败：{e}")
        print("可启动 FlClash 后重试，或用 --input 传入本地 CSV 行情文件。")
        return 1
    stock_name = data.attrs.get("stock_name", args.code)
    report = conclusion(data, stock_name); report["股票代码"] = args.code
    out = args.output or os.path.join(os.path.dirname(__file__), "outputs", f"A股分析_{args.code}_{datetime.now():%Y%m%d_%H%M%S}.xlsx")
    os.makedirs(os.path.dirname(out) or ".", exist_ok=True)
    write_xlsx(out, {"分析结论": report, "指标数据": data, "信号说明": pd.DataFrame([
        {"项目":"顶/底背离", "说明":"价格创近20日高/低点，而 RSI6 或 MACD 柱未同步创高/低；这是规则化观察信号，不是确定预测。"},
        {"项目":"综合评分", "说明":"MA、MACD、KDJ、RSI、BOLL 和背离信号的简单加权，仅用于辅助研究，不构成投资建议。"}])})
    x = data.iloc[-1]
    print(f"股票：{stock_name}（{args.code}） | 日期：{x['date']:%Y-%m-%d} | 收盘：{x['close']:.2f} | 涨跌幅：{x['pct_change']:.2f}%")
    print(f"成交量：{x['volume']:.0f} | 换手率：{x['turnover'] if pd.notna(x['turnover']) else '接口未提供'} | K线：{x['kline_pattern']}")
    print(f"MA5/MA20/MA60：{x['ma5']:.2f} / {x['ma20']:.2f} / {x['ma60']:.2f}")
    print(f"MACD DIF/DEA/柱：{x['dif']:.4f} / {x['dea']:.4f} / {x['macd']:.4f}")
    print(f"KDJ K/D/J：{x['k']:.2f} / {x['d']:.2f} / {x['j']:.2f} | RSI6/12/24：{x['rsi6']:.2f} / {x['rsi12']:.2f} / {x['rsi24']:.2f}")
    print(f"BOLL 上/中/下轨：{x['boll_up']:.2f} / {x['boll_mid']:.2f} / {x['boll_low']:.2f}")
    print(f"顶背离：{'是' if x['top_divergence'] else '否'} | 底背离：{'是' if x['bottom_divergence'] else '否'}")
    print(report[["综合评分", "结论", "支持理由", "风险提示"]].to_string(index=False))
    print(f"Excel 已生成：{out}")
    return 0


if __name__ == "__main__":
    for i in range(10):
        raise SystemExit(main())

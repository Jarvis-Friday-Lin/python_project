"""读取 Binance 实时 K 线，输出指标综合买卖参考。"""

from __future__ import annotations

import argparse
import json
import ssl
from urllib.parse import urlencode
from urllib.request import urlopen

import pandas as pd


API_URL = "https://api.binance.com/api/v3/klines"


def fetch(symbol: str, interval: str, limit: int) -> pd.DataFrame:
    query = urlencode({"symbol": symbol.upper(), "interval": interval, "limit": limit})
    try:
        import certifi
    except ImportError as error:
        raise RuntimeError("当前环境缺少 certifi，请先执行：python -m pip install -U certifi") from error
    context = ssl.create_default_context(cafile=certifi.where())
    try:
        with urlopen(f"{API_URL}?{query}", timeout=15, context=context) as response:
            rows = json.load(response)
    except Exception as error:
        raise RuntimeError(
            "无法访问 Binance 接口。请检查网络/VPN，或先执行：python -m pip install -U certifi"
        ) from error
    columns = ["open_time", "open", "high", "low", "close", "volume", "close_time", "quote_volume", "trades", "taker_base", "taker_quote", "unused"]
    data = pd.DataFrame(rows, columns=columns)
    for column in ["open", "high", "low", "close", "volume"]:
        data[column] = pd.to_numeric(data[column])
    data["date"] = pd.to_datetime(data["open_time"], unit="ms")
    return data


def indicators(data: pd.DataFrame) -> pd.DataFrame:
    result = data.copy()
    close = result["close"]
    result["ma20"] = close.rolling(20).mean()
    result["ma60"] = close.rolling(60).mean()

    # MACD：EMA12 - EMA26，再与 9 日信号线比较。
    result["macd"] = close.ewm(span=12, adjust=False).mean() - close.ewm(span=26, adjust=False).mean()
    result["macd_signal"] = result["macd"].ewm(span=9, adjust=False).mean()
    result["macd_hist"] = result["macd"] - result["macd_signal"]

    # RSI(14)：观察上涨与下跌动能，30/70 只是常见参考区间。
    change = close.diff()
    gain = change.clip(lower=0).rolling(14).mean()
    loss = (-change.clip(upper=0)).rolling(14).mean()
    result["rsi"] = 100 - 100 / (1 + gain / loss.replace(0, pd.NA))

    # KDJ(9,3,3)：观察收盘价在近期高低区间中的位置。
    low9 = result["low"].rolling(9).min()
    high9 = result["high"].rolling(9).max()
    rsv = (close - low9) / (high9 - low9) * 100
    result["k"] = rsv.ewm(com=2, adjust=False).mean()
    result["d"] = result["k"].ewm(com=2, adjust=False).mean()
    result["j"] = 3 * result["k"] - 2 * result["d"]

    # BOLL(20,2)：中轨 MA20，上下轨为中轨加减两倍标准差。
    result["boll_mid"] = close.rolling(20).mean()
    deviation = close.rolling(20).std()
    result["boll_upper"] = result["boll_mid"] + 2 * deviation
    result["boll_lower"] = result["boll_mid"] - 2 * deviation
    return result


def report(data: pd.DataFrame, symbol: str, interval: str) -> None:
    latest, previous = data.iloc[-1], data.iloc[-2]
    score = 0
    print(f"\n===== {symbol.upper()} / {interval} 实时指标参考 =====")
    print(f"数据时间：{latest['date']:%Y-%m-%d %H:%M:%S}")
    print(f"最新价格：{latest['close']:.6f}")

    if latest["close"] > latest["ma20"] > latest["ma60"]:
        score += 1
        print(f"MA：价格 > MA20({latest['ma20']:.6f}) > MA60({latest['ma60']:.6f})，趋势偏多")
    elif latest["close"] < latest["ma20"] < latest["ma60"]:
        score -= 1
        print(f"MA：价格 < MA20({latest['ma20']:.6f}) < MA60({latest['ma60']:.6f})，趋势偏空")
    else:
        print(f"MA：未形成同向排列，暂不确认趋势（MA20={latest['ma20']:.6f}，MA60={latest['ma60']:.6f}）")

    if latest["macd"] > latest["macd_signal"] and latest["macd_hist"] >= previous["macd_hist"]:
        score += 1
        print("MACD：快线在信号线上方且柱体增强，动能偏多")
    elif latest["macd"] < latest["macd_signal"] and latest["macd_hist"] <= previous["macd_hist"]:
        score -= 1
        print("MACD：快线在信号线下方且柱体减弱，动能偏空")
    else:
        print("MACD：动能信号不一致")

    if latest["rsi"] < 30:
        score += 1
        print(f"RSI：{latest['rsi']:.2f}，相对超卖，存在反弹观察价值")
    elif latest["rsi"] > 70:
        score -= 1
        print(f"RSI：{latest['rsi']:.2f}，相对超买，追高风险较大")
    else:
        print(f"RSI：{latest['rsi']:.2f}，处于中性区间")

    if latest["k"] > latest["d"] and previous["k"] <= previous["d"]:
        score += 1
        print(f"KDJ：K({latest['k']:.2f}) 上穿 D({latest['d']:.2f})，短线转强")
    elif latest["k"] < latest["d"] and previous["k"] >= previous["d"]:
        score -= 1
        print(f"KDJ：K({latest['k']:.2f}) 下穿 D({latest['d']:.2f})，短线转弱")
    else:
        print(f"KDJ：K={latest['k']:.2f}，D={latest['d']:.2f}，暂无新交叉")

    if latest["close"] > latest["boll_upper"]:
        score -= 1
        print("BOLL：价格突破上轨，趋势强但追高风险较大")
    elif latest["close"] < latest["boll_lower"]:
        score += 1
        print("BOLL：价格跌破下轨，可能超跌但必须等待反转确认")
    else:
        print("BOLL：价格仍在布林通道内")

    if score >= 3:
        action = "偏多：仅考虑分批、轻仓和等待确认，不建议一次性追涨。"
    elif score <= -3:
        action = "偏空：优先控制风险，暂不建议仅凭指标抄底。"
    else:
        action = "观望：指标分歧，没有形成明确买入或卖出信号。"
    print(f"\n===== 综合参考：{action}（评分 {score}/5） =====")
    print("这不是确定性预测或个性化投资建议；请自行设置仓位、止损和最大可承受损失。")


def main() -> None:
    parser = argparse.ArgumentParser(description="Binance 指标综合买卖参考")
    parser.add_argument("--symbol", default="BTCUSDT", help="交易对，例如 BTCUSDT、ETHUSDT、BNBUSDT")
    parser.add_argument("--interval", default="1d", help="K 线周期，例如 1d、4h、1h")
    parser.add_argument("--limit", type=int, default=180, help="K 线数量，至少 60 根")
    args = parser.parse_args()
    if args.limit < 60:
        parser.error("--limit 至少需要 60 根 K 线")
    report(indicators(fetch(args.symbol, args.interval, args.limit)), args.symbol, args.interval)


if __name__ == "__main__":
    main()

"""案例驱动示例：识别重复、非法与退款记录"""
# 对应 PDF：Pandas 第 20—46 页；重复订单检查为流程补充
# 任务：计算可确认的已付款收入，同时保留问题订单的排除原因。
# 重复订单号必须先按规则处理；同一订单重复上报不能被算成两笔收入。
# 案例数据：
# | order_id | city | amount | status |
# |---|---|---:|---|
# | A | 上海 | 100 | paid |
# | B | 北京 | 200 | paid |
# | A | 上海 | 100 | paid |
# | C | 上海 | 错误 | paid |
# | D | 北京 | -50 | paid |
# | E | 深圳 | 500 | unpaid |
# 先看整体路线：
# 第 1 步：先保留原金额，对订单号检查重复。
# 第 2 步：按本案例规则排除重复、未付款、非法和负金额，给出原因。
# 第 3 步：按城市汇总并做收入对账，保存明细与问题清单。

from pathlib import Path
import numpy as np
import pandas as pd
course=Path(__file__).resolve().parents[2]
data=pd.read_csv(course/"datasets"/"orders_audit.csv")
data["amount_raw"]=data["amount"]
data["amount"]=pd.to_numeric(data["amount"],errors="coerce")
# duplicated(subset,keep="first")标记相同订单号后续出现的记录。
# 本例重复A完全相同，可按首次上报保留；真实冲突记录不能盲目保留第一条。
duplicate=data.duplicated(subset=["order_id"],keep="first")
data["reason"]=np.select([duplicate,data["status"].ne("paid"),data["amount"].isna(),data["amount"].lt(0)],
                        ["重复订单","未付款","非法金额","负金额需核查"],default="有效")
print('\n===== data.to_markdown(index=False) =====')
print(data.to_markdown(index=False))
# np.select按第一个命中条件分配原因，因此原因顺序是显式规则的一部分。
valid=data.loc[data["reason"].eq("有效")].copy()
issues=data.loc[data["reason"].ne("有效")].copy()
summary=valid.groupby("city",as_index=False).agg(revenue=("amount","sum"),orders=("order_id","size"))
print('\n===== summary.to_markdown(index=False) =====')
print(summary.to_markdown(index=False))
print('\n===== issues[["order_id","amount_raw","reason"]].to_markdown(index=False) =====')
print(issues[["order_id","amount_raw","reason"]].to_markdown(index=False))
assert valid["order_id"].tolist()==["A","B"]
assert valid["amount"].sum()==summary["revenue"].sum()==300
assert len(valid)+len(issues)==len(data)
out=Path(__file__).resolve().parent/"outputs"
out.mkdir(exist_ok=True)
for name,frame in [("valid",valid),("issues",issues),("summary",summary)]:
    frame.to_csv(out/(name+".csv"),index=False,encoding="utf-8-sig")
# 负金额可能是退款，不一定错误；此案例在未确认前单独列出，不混入“确认收入”。

# 学完先自己回答，再看下面的参考答案：
# 1. 这个知识点解决什么类型的问题？
# 2. 为什么当前案例需要它？
# 3. 每一步代码为什么要在此时出现？
# 4. 如果换一种做法，代价和风险是什么？

# 参考答案：
# 1. 把数据清洗规则变成可追溯的收入确认流程。
# 2. 重复上报与未核实退款会使汇总收入不可信。
# 3. 先保留原值，再识别重复和金额问题，按明确优先级标记后才汇总有效收入。
# 4. 简单删行不留原因难以追查；自动把负数删掉可能漏掉退款，需要单独核查业务。

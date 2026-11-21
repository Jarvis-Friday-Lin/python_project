"""案例驱动示例：从原始订单到可复查的城市报表"""
# 对应 PDF：13-pandas-full.pdf 第 20—46 页综合
# 任务：读取订单，剔除未付款记录，对有效已付款金额按城市统计并保存。
# 必须先明确有效范围，否则未付款与非法金额会混入经营结论。
# 案例数据：
# | order_id | city | amount | status |
# |---|---|---:|---|
# | A | 上海 | 100 | paid |
# | B | 北京 | 200 | paid |
# | C | 上海 | 300 | paid |
# | D | 北京 | 错误 | paid |
# | E | 深圳 | 500 | unpaid |
# 先看整体路线：
# 第 1 步：读入原始订单并保留原金额。
# 第 2 步：转换金额，区分已付款、非法和未付款。
# 第 3 步：汇总有效记录，检查总额守恒，再导出。

from pathlib import Path
import pandas as pd
course=Path(__file__).resolve().parents[2]
data=pd.read_csv(course/"datasets"/"orders.csv")
data["amount_raw"]=data["amount"]
data["amount"]=pd.to_numeric(data["amount"],errors="coerce")
print('\n===== data.to_markdown(index=False) =====')
print(data.to_markdown(index=False))
paid=data["status"].eq("paid")
valid_amount=data["amount"].notna()&data["amount"].ge(0)
excluded=data.loc[~(paid&valid_amount)].copy()
valid=data.loc[paid&valid_amount].copy()
print('\n===== excluded.to_markdown(index=False) =====')
print(excluded.to_markdown(index=False))
report=valid.groupby("city",as_index=False).agg(total=("amount","sum"),orders=("order_id","size"))
print('\n===== report.to_markdown(index=False) =====')
print(report.to_markdown(index=False))
# 金额守恒只在相同“有效已付款”范围内核对，不拿全部原始订单总额比较。
assert report["total"].sum()==valid["amount"].sum()==600
output=Path(__file__).resolve().parent/"outputs"
output.mkdir(exist_ok=True)
report.to_csv(output/"city_report.csv",index=False,encoding="utf-8-sig")
excluded.to_csv(output/"excluded_orders.csv",index=False,encoding="utf-8-sig")
print('\n===== output =====')
print(output)
# 被排除的记录另存，避免让清洗看似成功却失去追溯能力。

# 学完先自己回答，再看下面的参考答案：
# 1. 这个知识点解决什么类型的问题？
# 2. 为什么当前案例需要它？
# 3. 每一步代码为什么要在此时出现？
# 4. 如果换一种做法，代价和风险是什么？

# 参考答案：
# 1. 把读取、清洗、筛选、分组和输出连成可复查流程。
# 2. 非法金额和未付款不能计入已付款收入。
# 3. 先保留原数据再转类型，确认有效范围后汇总，最后核对总额再输出。
# 4. 直接groupby更快写出报表，却可能把坏数据与未付款混入业务结论。

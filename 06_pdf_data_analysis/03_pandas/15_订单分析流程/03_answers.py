"""参考答案：从原始订单到可复查的城市报表"""
# 对应 PDF：13-pandas-full.pdf 第 20—46 页综合
# 建议先完成 02_exercises.py；下面的实现与该题数据、要求一一对应。

from pathlib import Path
import pandas as pd
course=Path(__file__).resolve().parents[2]
data=pd.read_csv(course/"datasets"/"orders.csv")
data["amount_raw"]=data["amount"]
data["amount"]=pd.to_numeric(data["amount"],errors="coerce")
mask=data["status"].eq("paid")&data["amount"].notna()&data["amount"].ge(0)
valid=data.loc[mask].copy()
excluded=data.loc[~mask].copy()
report=valid.groupby("city",as_index=False).agg(total=("amount","sum"),orders=("order_id","size"))
print('\n===== report.to_markdown(index=False) =====')
print(report.to_markdown(index=False))
assert valid["order_id"].tolist()==["A","B","C"]
assert excluded["order_id"].tolist()==["D","E"]
assert report.set_index("city")["total"].to_dict()=={"上海":400,"北京":200}
assert report["total"].sum()==600
out=Path(__file__).resolve().parent/"outputs"
out.mkdir(exist_ok=True)
report.to_csv(out/"exercise_city_report.csv",index=False,encoding="utf-8-sig")
excluded.to_csv(out/"exercise_excluded.csv",index=False,encoding="utf-8-sig")

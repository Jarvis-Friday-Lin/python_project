"""参考答案：识别重复、非法与退款记录"""
# 对应 PDF：Pandas 第 20—46 页；重复订单检查为流程补充
# 建议先完成 02_exercises.py；下面的实现与该题数据、要求一一对应。

from pathlib import Path
import numpy as np
import pandas as pd
course=Path(__file__).resolve().parents[2]
data=pd.read_csv(course/"datasets"/"orders_audit.csv")
data["amount_raw"]=data["amount"]
data["amount"]=pd.to_numeric(data["amount"],errors="coerce")
data["reason"]=np.select([data.duplicated("order_id"),data["status"].ne("paid"),data["amount"].isna(),data["amount"].lt(0)],
                        ["重复订单","未付款","非法金额","负金额需核查"],default="有效")
valid=data.loc[data["reason"].eq("有效")]
issues=data.loc[data["reason"].ne("有效")]
summary=valid.groupby("city",as_index=False).agg(revenue=("amount","sum"),orders=("order_id","size"))
print('\n===== summary.to_markdown(index=False) =====')
print(summary.to_markdown(index=False))
print('\n===== issues.to_markdown(index=False) =====')
print(issues.to_markdown(index=False))
assert data["reason"].tolist()==["有效","有效","重复订单","非法金额","负金额需核查","未付款"]
assert len(valid)==2 and len(issues)==4
assert summary["revenue"].sum()==300
out=Path(__file__).resolve().parent/"outputs"
out.mkdir(exist_ok=True)
for name,frame in [("exercise_valid",valid),("exercise_issues",issues),("exercise_summary",summary)]:
    frame.to_csv(out/(name+".csv"),index=False,encoding="utf-8-sig")

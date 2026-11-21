"""参考答案：缺失不是零分，非法文本也不是数字"""
# 对应 PDF：13-pandas-full.pdf 第 41—42 页；to_numeric与可空整数为实用补充
# 建议先完成 02_exercises.py；下面的实现与该题数据、要求一一对应。

import pandas as pd
data=pd.DataFrame({"name":["A","B","C","D"],"raw_score":["80","缺考",None,"0"]})
data["score"]=pd.to_numeric(data["raw_score"],errors="coerce")
invalid=data["raw_score"].notna()&data["score"].isna()
print('\n===== data.to_markdown(index=False) =====')
print(data.to_markdown(index=False))
assert data.loc[invalid,"name"].tolist()==["B"]
assert data["score"].isna().sum()==2
assert data.loc[data["score"]==0,"name"].tolist()==["D"]
nullable=data["score"].astype("Int64")
assert str(nullable.dtype)=="Int64" and nullable.isna().sum()==2
assert pd.to_numeric(pd.Series(["80","0"]),errors="raise").tolist()==[80,0]

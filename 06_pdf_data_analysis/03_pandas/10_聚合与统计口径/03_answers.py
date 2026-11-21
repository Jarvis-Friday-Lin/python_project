"""参考答案：列统计、行统计与缺失计数"""
# 对应 PDF：13-pandas-full.pdf 第 31—33 页
# 建议先完成 02_exercises.py；下面的实现与该题数据、要求一一对应。

import pandas as pd
data=pd.DataFrame({"name":["A","B"],"salary":[100,200],"bonus":[10,30]})
n=data[["salary","bonus"]]
print('\n===== n.agg(["sum","mean","min","max","std"]).to_markdown() =====')
print(n.agg(["sum","mean","min","max","std"]).to_markdown())
assert data["salary"].sum()==300 and data["salary"].mean()==150
assert data["bonus"].max()==30
assert n.sum(axis=1).tolist()==[110,230]
n.loc[1,"bonus"]=None
assert n["bonus"].count()==1 and n.size==4
assert pd.isna(pd.Series([None,None],dtype=float).sum(min_count=1))

"""参考答案：同一缺失表可以有不同清洗结果"""
# 对应 PDF：13-pandas-full.pdf 第 43—44 页
# 建议先完成 02_exercises.py；下面的实现与该题数据、要求一一对应。

import pandas as pd
data=pd.DataFrame({"name":["A","B","C","D"],"salary":[100,None,300,None],"experience":[2,5,None,None]})
assert data[["salary","experience"]].isna().sum().tolist()==[2,2]
assert data.dropna(subset=["salary"])["name"].tolist()==["A","C"]
assert data.dropna(subset=["salary","experience"],how="all")["name"].tolist()==["A","B","C"]
filled=data.fillna({"salary":data["salary"].mean()})
filled["salary_imputed"]=data["salary"].isna()
print('\n===== filled.to_markdown(index=False) =====')
print(filled.to_markdown(index=False))
assert filled["salary"].tolist()==[100,200,300,200]
assert filled["experience"].isna().sum()==2
assert filled.loc[filled["salary_imputed"],"name"].tolist()==["B","D"]
empty=pd.Series([None,None],dtype=float)
assert empty.fillna(empty.mean()).isna().all()

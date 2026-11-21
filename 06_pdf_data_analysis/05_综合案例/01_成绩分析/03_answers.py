"""参考答案：加权成绩、排名、中心化与相似学生"""
# 对应 PDF：NumPy 第 3—51 页、Pandas 第 4—33 页综合
# 建议先完成 02_exercises.py；下面的实现与该题数据、要求一一对应。

from pathlib import Path
import numpy as np
import pandas as pd
course=Path(__file__).resolve().parents[2]
data=pd.read_csv(course/"datasets"/"grades.csv")
x=data[["python","math","english"]].to_numpy(dtype=float)
data["weighted"]=x@np.array([.5,.3,.2])
order=np.argsort(-data["weighted"].to_numpy(),kind="stable")
centered=x-x.mean(axis=0,keepdims=True)
distance=np.sqrt(((x[:,None,:]-x[None,:,:])**2).sum(axis=2))
np.fill_diagonal(distance,np.inf)
nearest=distance.argmin(axis=1)
data["nearest"]=data["name"].to_numpy()[nearest]
data["nearest_distance"]=distance[np.arange(len(data)),nearest]
print('\n===== data.iloc[order].to_markdown(index=False) =====')
print(data.iloc[order].to_markdown(index=False))
assert np.allclose(data["weighted"],[79,70.5,80.5,79])
assert data.iloc[order]["name"].tolist()==["C","A","D","B"]
assert np.allclose(centered.mean(axis=0),0)
assert data.loc[0,"nearest"]=="D" and data.loc[3,"nearest"]=="A"
assert data.loc[0,"nearest_distance"]==data.loc[3,"nearest_distance"]==0
out=Path(__file__).resolve().parent/"outputs"
out.mkdir(exist_ok=True)
data.iloc[order].to_csv(out/"exercise_grade_report.csv",index=False,encoding="utf-8-sig")

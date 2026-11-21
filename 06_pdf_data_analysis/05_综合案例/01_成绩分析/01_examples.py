"""案例驱动示例：加权成绩、排名、中心化与相似学生"""
# 对应 PDF：NumPy 第 3—51 页、Pandas 第 4—33 页综合
# 任务：给教务处交付加权成绩排名，并说明学生各科相对均值的优势与最相似的同学。
# 先约定三科权重0.5/0.3/0.2，不把权重当作客观必然。
# 案例数据：
# | name | python | math | english |
# |---|---:|---:|---:|
# | A | 80 | 70 | 90 |
# | B | 60 | 85 | 75 |
# | C | 90 | 65 | 80 |
# | D | 80 | 70 | 90 |
# 先看整体路线：
# 第 1 步：读取指定数值列，核对范围与缺失。
# 第 2 步：矩阵乘权重、稳定排序，按科目中心化。
# 第 3 步：广播求距离，排除自身后找最近同学，导出结果。

from pathlib import Path
import numpy as np
import pandas as pd
course=Path(__file__).resolve().parents[2]
data=pd.read_csv(course/"datasets"/"grades.csv")
features=["python","math","english"]
x=data[features].to_numpy(dtype=float)
assert not np.isnan(x).any()
assert np.all((x>=0)&(x<=100))
weights=np.array([.5,.3,.2])
assert np.isclose(weights.sum(),1)
# (4,3)@(3,)->(4,)，每人恰好一个综合分。
data["weighted"]=x@weights
order=np.argsort(-data["weighted"].to_numpy(),kind="stable")
ranking=data.iloc[order]
print('\n===== ranking.to_markdown(index=False) =====')
print(ranking.to_markdown(index=False))
centered=x-x.mean(axis=0,keepdims=True)
print('\n===== pd.DataFrame(centered,index=data["name"],columns=features).to_markdown() =====')
print(pd.DataFrame(centered,index=data["name"],columns=features).to_markdown())
# 同一个集合与自己比较会让对角线距离0；先屏蔽自身，不能屏蔽所有0距离。
distances=np.sqrt(((x[:,None,:]-x[None,:,:])**2).sum(axis=2))
np.fill_diagonal(distances,np.inf)
nearest=distances.argmin(axis=1)
data["nearest"]=data["name"].to_numpy()[nearest]
data["nearest_distance"]=distances[np.arange(len(data)),nearest]
print('\n===== data.to_markdown(index=False) =====')
print(data.to_markdown(index=False))
# A与D成绩完全相同，他们是彼此距离0的不同人；不能把所有0当作自身。
assert data["nearest"].tolist()==["D","A","A","A"]
assert np.allclose(centered.mean(axis=0),0)
out=Path(__file__).resolve().parent/"outputs"
out.mkdir(exist_ok=True)
data.iloc[order].to_csv(out/"grade_report.csv",index=False,encoding="utf-8-sig")
# 特征都使用0—100相同量纲；不同量纲的特征需先讨论缩放。

# 学完先自己回答，再看下面的参考答案：
# 1. 这个知识点解决什么类型的问题？
# 2. 为什么当前案例需要它？
# 3. 每一步代码为什么要在此时出现？
# 4. 如果换一种做法，代价和风险是什么？

# 参考答案：
# 1. 组合数值计算、身份标签与可追溯输出。
# 2. 教务处既要排名，也想知道单科差异和相似学生。
# 3. 先校验输入再加权；排序不丢身份；中心化后另算原尺度距离，屏蔽对角线才取最近。
# 4. 单独排序分数会丢姓名；所有零距离都屏蔽会误伤同分同学，权重与尺度也影响结论。

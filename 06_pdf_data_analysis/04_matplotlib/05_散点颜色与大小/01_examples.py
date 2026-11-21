"""案例驱动示例：学习时长和成绩有没有关系"""
# 对应 PDF：14-matplotlib-full.pdf 第 14 页
# 任务：同时展示学习时长、成绩、出勤率。
# 散点保留每个样本的位置，颜色与面积可以编码额外变量；相关形态不证明因果。
# 案例数据：
# | 学生 | hours | score | attendance |
# |---|---:|---:|---:|
# | A | 1 | 60 | 0.6 |
# | B | 2 | 75 | 0.8 |
# | C | 3 | 80 | 0.9 |
# | D | 4 | 90 | 1.0 |
# 先看整体路线：
# 第 1 步：先画学习时长与成绩的成对坐标。
# 第 2 步：用颜色与面积编码出勤率。
# 第 3 步：增加色条解释颜色，而不是只做装饰。

import numpy as np
import matplotlib.pyplot as plt
hours=np.array([1,2,3,4])
scores=np.array([60,75,80,90])
attendance=np.array([.6,.8,.9,1.])
fig,ax=plt.subplots(figsize=(6,4))
# scatter(x,y,c,s,cmap)：c可为数值数组，s是点的面积（平方点），不是半径。
points=ax.scatter(hours,scores,c=attendance,s=attendance*200,cmap="viridis",alpha=.8)
# colorbar需要接收散点对象来知道数值到颜色的映射。
fig.colorbar(points,ax=ax,label="Attendance rate")
ax.set(xlabel="Study hours",ylabel="Score",title="Study and attendance")
fig.tight_layout()
print('\n===== points.get_offsets() =====')
print(points.get_offsets())
assert points.get_offsets().shape==(4,2)
assert np.allclose(points.get_array(),attendance)
# 四个点不足以推断总体规律；出勤、基础水平等也可能同时影响成绩。
plt.show()

# 学完先自己回答，再看下面的参考答案：
# 1. 这个知识点解决什么类型的问题？
# 2. 为什么当前案例需要它？
# 3. 每一步代码为什么要在此时出现？
# 4. 如果换一种做法，代价和风险是什么？

# 参考答案：
# 1. 查看成对变量关系与样本差异。
# 2. 每名学生都有时长和成绩，出勤还能作为第三个变量。
# 3. 先匹配每人的x/y，再加颜色大小，最后用色条提供解码依据。
# 4. 折线会暗示学生之间存在连续顺序；散点更合适，但不能从相关图直接推因果。

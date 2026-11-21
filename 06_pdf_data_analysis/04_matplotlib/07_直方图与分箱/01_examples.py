"""案例驱动示例：同一批成绩为什么能画出不同分布"""
# 对应 PDF：14-matplotlib-full.pdf 第 18—19 页
# 任务：统计不同成绩区间各有多少学生。
# 柱状图的类别通常已知；直方图先按数值区间分箱，再统计每箱人数。
# 案例数据：
# | 成绩序列 |
# |---|
# | 50,60,65,70,75,80,85,90,95,100 |
# 先看整体路线：
# 第 1 步：先手工数[50,70)、[70,90)、[90,101]的人数。
# 第 2 步：用明确边界bins绘图并读取返回计数。
# 第 3 步：比较密度与频数，解释分箱影响。

import numpy as np
import matplotlib.pyplot as plt
scores=np.array([50,60,65,70,75,80,85,90,95,100])
print('\n===== [sum((scores>=lo)&(scores<hi)) for lo,hi in [(50,70),(70,90),(90,101)]] =====')
print([sum((scores>=lo)&(scores<hi)) for lo,hi in [(50,70),(70,90),(90,101)]])
fig,axes=plt.subplots(1,2,figsize=(9,4))
# hist返回counts、edges、patches；除了最后一箱，其余通常左闭右开。
counts,edges,_=axes[0].hist(scores,bins=[50,70,90,101],color="steelblue",edgecolor="black",alpha=.7)
axes[0].set(xlabel="Score",ylabel="Students",title="Explicit bins")
print('\n===== counts =====')
print(counts)
print('\n===== edges =====')
print(edges)
# bins=5指定箱数；density=True令柱面积和为1，不是每箱概率直接相加为1。
density,bounds,_=axes[1].hist(scores,bins=5,density=True,edgecolor="black")
axes[1].set(xlabel="Score",ylabel="Density",title="Five-bin density")
assert counts.tolist()==[3,4,3]
assert np.isclose(np.sum(density*np.diff(bounds)),1)
fig.tight_layout()
plt.show()

# 学完先自己回答，再看下面的参考答案：
# 1. 这个知识点解决什么类型的问题？
# 2. 为什么当前案例需要它？
# 3. 每一步代码为什么要在此时出现？
# 4. 如果换一种做法，代价和风险是什么？

# 参考答案：
# 1. 观察单变量的区间频数分布。
# 2. 平均分无法说明成绩集中在哪些区间。
# 3. 先手工数边界案例，再用hist核对返回计数，最后比较分箱和密度。
# 4. 柱状图需先自行分组；自动分箱更快但箱数不同会影响视觉判断。

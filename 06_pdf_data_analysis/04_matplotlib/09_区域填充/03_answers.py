"""参考答案：标出实际与目标的差额区域"""
# 对应 PDF：14-matplotlib-full.pdf 第 25 页
# 建议先完成 02_exercises.py；下面的实现与该题数据、要求一一对应。

import numpy as np
import matplotlib.pyplot as plt
x=np.arange(1,5)
a=np.array([10,20,18,12])
t=np.full(4,15)
fig,ax=plt.subplots()
ax.plot(x,a,label="Actual")
ax.plot(x,t,label="Target")
ax.fill_between(x,a,t,where=a>=t,interpolate=True,color="green",alpha=.25)
ax.fill_between(x,a,t,where=a<t,interpolate=True,color="red",alpha=.15)
ax.legend()
assert len(ax.lines)==2 and len(ax.collections)==2
assert (a-t).tolist()==[-5,5,3,-3]
# 图形面积包含对采样点之间的插值，离散总盈余应直接对每日差额求和。
assert (a-t).sum()==0
plt.show()

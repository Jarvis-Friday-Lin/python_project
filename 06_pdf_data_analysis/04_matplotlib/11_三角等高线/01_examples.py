"""案例驱动示例：零散测量点如何展示空间分布"""
# 对应 PDF：14-matplotlib-full.pdf 第 24 页
# 任务：只有5个不规则位置的温度测量，不能假装已经有完整矩形网格。
# 三角剖分先连接样本点，tricontour在三角区域内依据样本值画等高线。
# 案例数据：
# | x | y | temperature |
# |---:|---:|---:|
# | 0 | 0 | 20 |
# | 2 | 0 | 22 |
# | 0 | 2 | 24 |
# | 2 | 2 | 26 |
# | 0.8 | 0.7 | 23 |
# 先看整体路线：
# 第 1 步：明确x/y/z是一维且逐点对应。
# 第 2 步：建立Triangulation并观察连接关系。
# 第 3 步：使用tricontour绘等值线并保留观测点。

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.tri import Triangulation
x=np.array([0,2,0,2,.8])
y=np.array([0,0,2,2,.7])
z=np.array([20,22,24,26,23])
# Triangulation(x,y)可自动三角剖分；也能传triangles指定每个三角形的顶点编号。
tri=Triangulation(x,y)
print('\n===== tri.triangles =====')
print(tri.triangles)
fig,axes=plt.subplots(1,2,figsize=(9,4))
axes[0].triplot(tri,color="gray")
axes[0].scatter(x,y,c=z,cmap="plasma")
# tricontour(triangulation,z,...)接受剖分对象；不是传“triangulate=”关键字。
contours=axes[1].tricontour(tri,z,levels=[20,21,22,23,24,25,26],cmap="plasma")
axes[1].clabel(contours)
axes[1].scatter(x,y,color="black",s=15)
fig.colorbar(contours,ax=axes[1],label="Temperature")
for ax in axes: ax.set(xlabel="x",ylabel="y",aspect="equal")
axes[0].set_title("Sampling triangles")
axes[1].set_title("Triangular contours")
fig.tight_layout()
assert len(x)==len(y)==len(z)==5
assert tri.triangles.shape[1]==3
# 重复坐标、共线点、缺失z可能使剖分无效；未观测区域的插值不是事实测量。
plt.show()

# 学完先自己回答，再看下面的参考答案：
# 1. 这个知识点解决什么类型的问题？
# 2. 为什么当前案例需要它？
# 3. 每一步代码为什么要在此时出现？
# 4. 如果换一种做法，代价和风险是什么？

# 参考答案：
# 1. 依据不规则空间样本绘制等值线。
# 2. 测量点不是规则网格，不能套用完整网格的假设。
# 3. 先逐点匹配位置和值，再剖分，再画等值线并叠加观测点。
# 4. 先插值成网格也能画，但新增插值步骤与假设；三角插值仍不等于真实观测。

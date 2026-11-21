"""参考答案：零散测量点如何展示空间分布"""
# 对应 PDF：14-matplotlib-full.pdf 第 24 页
# 建议先完成 02_exercises.py；下面的实现与该题数据、要求一一对应。

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.tri import Triangulation
x=np.array([0,2,0,2,.8])
y=np.array([0,0,2,2,.7])
z=np.array([20,22,24,26,23])
tri=Triangulation(x,y)
fig,axes=plt.subplots(1,2)
axes[0].triplot(tri)
cs=axes[1].tricontour(tri,z,levels=[21,22,23,24,25])
axes[1].clabel(cs)
axes[1].scatter(x,y,color="black")
assert tri.triangles.shape[1]==3
assert tri.triangles.min()>=0 and tri.triangles.max()<5
# 样本位置不规则，不存在对应每个行列交点的规则测量表。
plt.show()

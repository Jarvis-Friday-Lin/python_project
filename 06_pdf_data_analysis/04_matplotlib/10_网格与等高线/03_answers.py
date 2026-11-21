"""参考答案：在平面上显示温度变化"""
# 对应 PDF：14-matplotlib-full.pdf 第 22—23 页
# 建议先完成 02_exercises.py；下面的实现与该题数据、要求一一对应。

import numpy as np
import matplotlib.pyplot as plt
x=np.linspace(-2,2,5)
y=np.linspace(-2,2,5)
X,Y=np.meshgrid(x,y)
Z=30-X**2-Y**2
fig,axes=plt.subplots(1,2,figsize=(9,4))
levels=[22,24,26,28,30]
lines=axes[0].contour(X,Y,Z,levels=levels)
axes[0].clabel(lines)
filled=axes[1].contourf(X,Y,Z,levels=levels)
fig.colorbar(filled,ax=axes[1],label="Temperature")
for ax in axes: ax.set(xlabel="x",ylabel="y",aspect="equal")
assert Z.shape==(5,5) and Z[2,2]==30 and Z[0,0]==22
fig.tight_layout()
plt.show()

"""参考答案：绘制模拟地形的等高线"""
# 对应 PDF：14-matplotlib-full.pdf 第 22—23 页
# 课件核心：第22—23页：meshgrid、contour、levels、cmap、colorbar；contourf为课件自行探索。
# 扩展：clabel和set_aspect为扩展，模拟公式不是实测地形。
# 案例数据（据此自行创建对象，不能照抄 examples 的数据）：
# | 参数 | 值 |
# |---|---|
# | x | -3到3，7个等距点 |
# | y | -2到2，5个等距点 |
# | 高度公式 | Z=100-2*X**2-Y**2 |
# | 等高线层级 | [78,82,86,90,94,98,100] |
# 建议先做练习，再逐段对照下面的实现；assert 用于验证结果。

import numpy as np
import matplotlib.pyplot as plt
x,y = np.linspace(-3,3,7), np.linspace(-2,2,5)
X,Y = np.meshgrid(x,y)
Z = 100-2*X**2-Y**2
levels = [78,82,86,90,94,98,100]
fig, axes = plt.subplots(1,2,figsize=(10,4))
contours = axes[0].contour(X,Y,Z,levels=levels,cmap='viridis')
axes[0].clabel(contours,inline=True)
filled = axes[1].contourf(X,Y,Z,levels=levels,cmap='viridis')
fig.colorbar(filled,ax=axes[1],label='Height (m)')
for ax in axes:
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_aspect('equal')
assert X.shape == Y.shape == Z.shape == (5,7)
assert Z[2,3] == 100 and Z[0,0] == Z[-1,-1] == 78
assert list(contours.levels) == levels
# meshgrid默认xy布局：行对应y，列对应x；有5个y和7个x，因此形状(5,7)。
fig.tight_layout()
plt.show()
plt.close(fig)

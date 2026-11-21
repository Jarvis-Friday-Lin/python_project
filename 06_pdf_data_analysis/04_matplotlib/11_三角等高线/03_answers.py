"""参考答案：对不规则采样点绘制土壤湿度"""
# 对应 PDF：14-matplotlib-full.pdf 第 24 页
# 课件核心：第24页：一维坐标、Triangulation、tricontour与levels。
# 扩展：triplot为第22页自行探索；scatter复习第14页；三角形索引检查为扩展。
# 案例数据（据此自行创建对象，不能照抄 examples 的数据）：
# | point | x | y | moisture |
# |---|---|---|---|
# | P1 | 0 | 0 | 15 |
# | P2 | 3 | 0 | 21 |
# | P3 | 0 | 3 | 24 |
# | P4 | 3 | 3 | 30 |
# | P5 | 1 | 0.8 | 20 |
# | P6 | 2.2 | 1.7 | 26 |
# 建议先做练习，再逐段对照下面的实现；assert 用于验证结果。

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.tri import Triangulation
x,y = np.array([0,3,0,3,1,2.2]), np.array([0,0,3,3,0.8,1.7])
moisture = np.array([15,21,24,30,20,26])
tri = Triangulation(x,y)
fig, axes = plt.subplots(1,2,figsize=(9,4))
axes[0].triplot(tri)
curves = axes[1].tricontour(tri,moisture,levels=[18,21,24,27],cmap='plasma')
axes[1].scatter(x,y,color='black')
fig.colorbar(curves,ax=axes[1],label='Moisture (%)')
for ax in axes:
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
assert tri.triangles.shape[1] == 3
assert tri.triangles.min() >= 0 and tri.triangles.max() < 6
assert list(curves.levels) == [18,21,24,27]
# 点的位置不形成规则行列，即使有6个值也不能用reshape冒充规则网格。
# 三角网格只描述采样覆盖区域的插值关系，不能保证区域外湿度。
fig.tight_layout()
plt.show()
plt.close(fig)

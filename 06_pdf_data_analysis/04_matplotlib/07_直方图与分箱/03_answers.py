"""参考答案：配送时长的直方图边界"""
# 对应 PDF：14-matplotlib-full.pdf 第 18—19 页
# 课件核心：第18—19页：hist、bins、颜色、透明度与边框。
# 扩展：density参数与密度积分检查为扩展；bin边界含义属于结果理解。
# 案例数据（据此自行创建对象，不能照抄 examples 的数据）：
# | delivery_minutes |
# |---|
# | 5,8,10,12,15,18,20,22,25,30,35,40 |
# | 基础分箱边界：0,10,20,30,40 |
# 建议先做练习，再逐段对照下面的实现；assert 用于验证结果。

import numpy as np
import matplotlib.pyplot as plt
minutes = np.array([5,8,10,12,15,18,20,22,25,30,35,40])
fig, axes = plt.subplots(1,3,figsize=(12,3))
counts, edges, _ = axes[0].hist(minutes,bins=[0,10,20,30,40],color='blue',alpha=0.7,edgecolor='black')
axes[1].hist(minutes,bins=6,edgecolor='black')
density, density_edges, _ = axes[2].hist(minutes,bins=6,density=True)
for ax in axes:
    ax.set_xlabel('Delivery time (min)')
axes[0].set_ylabel('Count')
axes[1].set_ylabel('Count')
axes[2].set_ylabel('Density')
print('\n===== counts =====')
print(counts)
assert counts.tolist() == [2,4,3,3] and counts.sum() == 12
# 前三箱左闭右开，最后一箱两端都包含，40不会被丢弃。
assert np.isclose(np.sum(density*np.diff(density_edges)),1)
fig.tight_layout()
plt.show()
plt.close(fig)

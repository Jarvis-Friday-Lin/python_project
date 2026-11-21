"""参考答案：在六张子图比较六台电机"""
# 对应 PDF：14-matplotlib-full.pdf 第 8、12 页
# 课件核心：第8、12页：多行多列subplots、二维Axes索引、每图单独设置标题。
# 扩展：sharex/sharey共享轴与对象检查是扩展；循环只是简化重复设置。
# 案例数据（据此自行创建对象，不能照抄 examples 的数据）：
# | hour | M1 | M2 | M3 | M4 | M5 | M6 |
# |---|---|---|---|---|---|---|
# | 0 | 30 | 32 | 34 | 36 | 38 | 40 |
# | 1 | 31 | 33 | 35 | 37 | 39 | 41 |
# | 2 | 29 | 31 | 33 | 35 | 37 | 39 |
# | 3 | 32 | 34 | 36 | 38 | 40 | 42 |
# 建议先做练习，再逐段对照下面的实现；assert 用于验证结果。

import numpy as np
import matplotlib.pyplot as plt
hours = [0,1,2,3]
values = np.array([[30,32,34,36,38,40],[31,33,35,37,39,41],
                   [29,31,33,35,37,39],[32,34,36,38,40,42]])
fig, axes = plt.subplots(2,3,figsize=(12,6),sharex=True,sharey=True)
for i, ax in enumerate(axes.flat):
    ax.plot(hours,values[:,i],marker='o')
    ax.set_title(f'M{i+1}')
    ax.set_xlabel('Hour')
    ax.set_ylabel('Temperature (C)')
fig.tight_layout()
assert axes.shape == (2,3) and len(fig.axes) == 6
assert axes[1,1].get_title() == 'M5'
assert all(len(ax.lines) == 1 and len(ax.lines[0].get_xdata()) == 4 for ax in axes.flat)
assert list(axes[1,1].lines[0].get_ydata()) == [38,39,37,40]
plt.show()
plt.close(fig)

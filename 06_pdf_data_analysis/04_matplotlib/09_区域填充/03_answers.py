"""参考答案：标出水库水位超出参考线的区间"""
# 对应 PDF：14-matplotlib-full.pdf 第 25 页
# 课件核心：第25页：fill_between、两条曲线、color/alpha/label。
# 扩展：where/interpolate条件填充为扩展；面积不是水量测量。
# 案例数据（据此自行创建对象，不能照抄 examples 的数据）：
# | day | level_m | reference_m |
# |---|---|---|
# | 1 | 9 | 10 |
# | 2 | 11 | 10 |
# | 3 | 13 | 10 |
# | 4 | 10 | 10 |
# | 5 | 8 | 10 |
# 建议先做练习，再逐段对照下面的实现；assert 用于验证结果。

import numpy as np
import matplotlib.pyplot as plt
days, level = np.arange(1,6), np.array([9,11,13,10,8])
reference = np.full(5,10)
fig, ax = plt.subplots()
ax.plot(days,level,label='Measured',marker='o')
ax.plot(days,reference,label='Reference',linestyle='--')
# 扩展：where提供每个采样点是否参与填充；interpolate补上交叉处边界。
ax.fill_between(days,level,reference,where=level > reference,interpolate=True,color='orange',alpha=0.4,label='Above')
ax.fill_between(days,level,reference,where=level < reference,interpolate=True,color='blue',alpha=0.3,label='Below')
ax.set_xlabel('Day')
ax.set_ylabel('Water level (m)')
ax.legend()
counts = ((level > reference).sum(),(level == reference).sum(),(level < reference).sum())
print('\n===== counts =====')
print(counts)
assert counts == (2,1,2) and len(ax.lines) == 2 and len(ax.collections) == 2
# 横轴是天、纵轴是米，带状面积并非立方米水量，更不包含水库横截面信息。
plt.show()
plt.close(fig)

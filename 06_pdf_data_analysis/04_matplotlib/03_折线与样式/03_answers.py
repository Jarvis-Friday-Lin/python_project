"""参考答案：对比两条线路的公交等候时间"""
# 对应 PDF：14-matplotlib-full.pdf 第 10—13 页
# 课件核心：第10—13页：plot多条线、marker、color、linestyle与legend。
# 扩展：Line2D对象读取/修改为验证扩展。
# 案例数据（据此自行创建对象，不能照抄 examples 的数据）：
# | hour | route_A | route_B |
# |---|---|---|
# | 7 | 8 | 12 |
# | 9 | 6 | 7 |
# | 12 | 10 | 8 |
# | 18 | 15 | 11 |
# 建议先做练习，再逐段对照下面的实现；assert 用于验证结果。

import numpy as np
import matplotlib.pyplot as plt
hours, a, b = [7,9,12,18], np.array([8,6,10,15]), np.array([12,7,8,11])
fig, ax = plt.subplots()
line_a, = ax.plot(hours,a,color='blue',linestyle='-',marker='o',label='Route A')
ax.plot(hours,b,color='orange',linestyle='--',marker='x',label='Route B')
ax.set_xlabel('Hour')
ax.set_ylabel('Minutes')
ax.legend()
diff = a-b
print('\n===== diff =====')
print(diff)
assert diff.tolist() == [-4,-1,2,4]
assert np.array(hours)[diff > 0].tolist() == [12,18]
assert ax.get_legend_handles_labels()[1] == ['Route A','Route B']
# 扩展：只修改线型，不删除坐标数据；None字符串表示不画连接线。
line_a.set_linestyle('None')
assert len(line_a.get_xdata()) == 4 and line_a.get_linestyle() == 'None'
plt.show()
plt.close(fig)

"""参考答案：比较不同线路的工作日与周末客流"""
# 对应 PDF：14-matplotlib-full.pdf 第 15—16 页
# 课件核心：第15—16页：bar的高度、宽度、偏移、tick_label与legend。
# 扩展：barh水平柱状图及柱对象读取为扩展。
# 案例数据（据此自行创建对象，不能照抄 examples 的数据）：
# | route | weekday | weekend |
# |---|---|---|
# | R1 | 120 | 90 |
# | R2 | 80 | 110 |
# | R3 | 150 | 130 |
# | R4 | 60 | 85 |
# 建议先做练习，再逐段对照下面的实现；assert 用于验证结果。

import numpy as np
import matplotlib.pyplot as plt
routes = ['R1','R2','R3','R4']
weekday, weekend = np.array([120,80,150,60]), np.array([90,110,130,85])
x, width = np.arange(4), 0.3
fig, ax = plt.subplots()
ax.bar(x-width/2,weekday,width=width,label='Weekday')
ax.bar(x+width/2,weekend,width=width,label='Weekend')
ax.set_xticks(x,labels=routes)
ax.set_ylabel('Passengers')
ax.legend()
diff = weekend-weekday
print('\n===== diff =====')
print(diff)
assert diff.tolist() == [-30,30,-20,25]
assert np.array(routes)[diff > 0].tolist() == ['R2','R4']
assert len(ax.patches) == 8
fig2, ax2 = plt.subplots()
ax2.barh(routes,weekend)
ax2.set_xlabel('Passengers')
assert len(ax2.patches) == 4 and [p.get_width() for p in ax2.patches] == weekend.tolist()
plt.show()
plt.close(fig)
plt.close(fig2)

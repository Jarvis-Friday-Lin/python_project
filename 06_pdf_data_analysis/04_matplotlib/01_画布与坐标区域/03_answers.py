"""参考答案：绘制房间四个时刻的温度"""
# 对应 PDF：14-matplotlib-full.pdf 第2—7、11页
# 课件核心：第2—7、11页：Figure/Axes、subplots、plot、轴标签与标题。
# 扩展：fig.axes与Line2D读取数据是对象检查扩展。
# 案例数据（据此自行创建对象，不能照抄 examples 的数据）：
# | hour | temperature_c |
# |---|---|
# | 6 | 16 |
# | 10 | 21 |
# | 14 | 25 |
# | 18 | 20 |
# 建议先做练习，再逐段对照下面的实现；assert 用于验证结果。

import matplotlib.pyplot as plt
hours, temperature = [6,10,14,18], [16,21,25,20]
fig, ax = plt.subplots(figsize=(7,3))
line, = ax.plot(hours,temperature,marker='o')
ax.set_xlabel('Hour')
ax.set_ylabel('Temperature (C)')
ax.set_title('Room temperature')
# Figure是整张画布；ax是一个绘图区；ax.xaxis/ax.yaxis是该图内的两根坐标轴。
assert len(fig.axes) == 1 and len(line.get_xdata()) == 4
assert list(line.get_ydata()) == temperature
assert list(fig.get_size_inches()) == [7,3]
plt.show()
plt.close(fig)

"""参考答案：从一张空白画布到销售趋势"""
# 对应 PDF：14-matplotlib-full.pdf 第 2—7 页
# 建议先完成 02_exercises.py；下面的实现与该题数据、要求一一对应。

import matplotlib.pyplot as plt
fig,ax=plt.subplots(figsize=(6,4))
ax.plot([1,2,3],[10,20,15],marker="o")
ax.set(xlabel="Day",ylabel="Sales (units)",title="Three-day sales")
assert len(fig.axes)==1
assert list(ax.lines[0].get_ydata())==[10,20,15]
# Figure是画布；Axes是绘图区；Axis管理一个坐标方向的刻度等。
plt.show()


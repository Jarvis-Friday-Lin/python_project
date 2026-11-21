"""案例驱动示例：从一张空白画布到销售趋势"""
# 对应 PDF：14-matplotlib-full.pdf 第 2—7 页
# Matplotlib 用于把数据绘制成图形。Figure是整张画布，Axes是放图的区域，Axis是管理刻度和坐标方向的对象。
# 任务：用三天销量画第一张折线图，理解方法到底属于哪个对象。
# 案例数据：
# | day | sales |
# |---:|---:|
# | 1 | 10 |
# | 2 | 20 |
# | 3 | 15 |
# 先看整体路线：
# 第 1 步：先用表格观察销量但不急于选样式。
# 第 2 步：创建Figure与Axes，解释返回值解包。
# 第 3 步：绘制坐标点，添加含义后显示。

import matplotlib.pyplot as plt
days=[1,2,3]
sales=[10,20,15]
print('\n===== list(zip(days,sales)) =====')
print(list(zip(days,sales)))
# 一张表能看确切值，但折线能突出先升后降的顺序变化。
# subplots返回两个对象，figsize=(6,4)单位是英寸，不是像素。
fig,ax=plt.subplots(figsize=(6,4))
# plot(x,y)按输入顺序连接点；两份输入长度必须相同。
ax.plot(days,sales,marker="o")
ax.set_xlabel("Day")
ax.set_ylabel("Sales (units)")
ax.set_title("Three-day sales")
print('\n===== type(fig).__name__ =====')
print(type(fig).__name__)
print('\n===== type(ax).__name__ =====')
print(type(ax).__name__)
print('\n===== type(ax.xaxis).__name__ =====')
print(type(ax.xaxis).__name__)
assert len(fig.axes)==1
assert len(ax.lines[0].get_ydata())==3
# show()显示已创建的图；在PyCharm中可能进入Plots工具窗或弹出独立窗口。
plt.show()

# 学完先自己回答，再看下面的参考答案：
# 1. 这个知识点解决什么类型的问题？
# 2. 为什么当前案例需要它？
# 3. 每一步代码为什么要在此时出现？
# 4. 如果换一种做法，代价和风险是什么？

# 参考答案：
# 1. 理解图形对象归属并画基础图。
# 2. 后续多图时必须知道线画在哪个Axes里。
# 3. 先确定x/y业务含义，再建画布，画线后补坐标含义，最后显示。
# 4. 直接plt.plot也能画，但对象式ax接口在多子图时更清楚。

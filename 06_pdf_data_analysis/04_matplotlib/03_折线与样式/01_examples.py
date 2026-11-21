"""案例驱动示例：对比实际销量与目标销量"""
# 对应 PDF：14-matplotlib-full.pdf 第 10—13 页
# 任务：观察实际销量与目标的差距，区分折线、仅点与多曲线。
# 连线适合有顺序的变量，不应让未排序的日期产生来回折返。
# 案例数据：
# | day | actual | target |
# |---:|---:|---:|
# | 1 | 10 | 15 |
# | 2 | 20 | 15 |
# | 3 | 15 | 15 |
# 先看整体路线：
# 第 1 步：先比较每一天的差额。
# 第 2 步：在同一Axes画两条有明确样式的线。
# 第 3 步：展示仅点模式与规则采样曲线。

import numpy as np
import matplotlib.pyplot as plt
days=[1,2,3]
actual=[10,20,15]
target=[15,15,15]
print('\n===== [a-b for a,b in zip(actual,target)] =====')
print([a-b for a,b in zip(actual,target)])
fig,axes=plt.subplots(1,2,figsize=(9,4))
# plot返回Line2D列表；常用参数有color/linestyle/linewidth/marker/markersize/label。
axes[0].plot(days,actual,color="tab:blue",marker="o",linewidth=2,label="Actual")
axes[0].plot(days,target,color="tab:red",linestyle="--",label="Target")
axes[0].legend()
axes[0].set(title="Actual vs target",xlabel="Day",ylabel="Sales")
x=np.linspace(0,2,10)
# linestyle="None"只画点，不连接；NumPy函数可批量算函数曲线的y值。
axes[1].plot(x,np.exp(x),linestyle="None",marker="x",color="green")
axes[1].set(title="Sampled exponential",xlabel="x",ylabel="exp(x)")
fig.tight_layout()
assert len(axes[0].lines)==2
assert np.array_equal(axes[0].lines[0].get_ydata(),actual)
plt.show()

# 学完先自己回答，再看下面的参考答案：
# 1. 这个知识点解决什么类型的问题？
# 2. 为什么当前案例需要它？
# 3. 每一步代码为什么要在此时出现？
# 4. 如果换一种做法，代价和风险是什么？

# 参考答案：
# 1. 显示顺序变化与多组趋势。
# 2. 逐日差额有方向性，实际和目标需要同图对照。
# 3. 先核对差额，再画真实曲线，添加目标线后说明样式和图例。
# 4. 表格更精确但趋势不突出；未排序x直接连线会误导时间走势。

"""案例驱动示例：标出实际与目标的差额区域"""
# 对应 PDF：14-matplotlib-full.pdf 第 25 页
# 任务：不仅画实际与目标两条线，还把超过目标的区域着色。
# fill_between根据相同x坐标对应的两组y边界填充，可用where限制范围。
# 案例数据：
# | day | actual | target |
# |---:|---:|---:|
# | 1 | 10 | 15 |
# | 2 | 20 | 15 |
# | 3 | 18 | 15 |
# | 4 | 12 | 15 |
# 先看整体路线：
# 第 1 步：先计算正负差额。
# 第 2 步：绘出两条边界线再填充差额。
# 第 3 步：用where与interpolate处理交叉位置。

import numpy as np
import matplotlib.pyplot as plt
x=np.array([1,2,3,4])
actual=np.array([10,20,18,12])
target=np.full(4,15)
print('\n===== actual-target =====')
print(actual-target)
fig,ax=plt.subplots(figsize=(6,4))
ax.plot(x,actual,label="Actual",marker="o")
ax.plot(x,target,label="Target",linestyle="--")
# y1/y2是两条边界；where是布尔条件；alpha控制透明度。
# interpolate=True会在曲线交叉处求交点，避免着色只停在采样点。
ax.fill_between(x,actual,target,where=actual>=target,interpolate=True,
                color="green",alpha=.25,label="Above target")
ax.fill_between(x,actual,target,where=actual<target,interpolate=True,
                color="red",alpha=.15,label="Below target")
ax.set(xlabel="Day",ylabel="Sales",title="Gap to target")
ax.legend()
assert len(ax.collections)==2
assert (actual-target).tolist()==[-5,5,3,-3]
# 填色只是把给定曲线之间的范围突出显示，不是预测置信区间。
plt.show()

# 学完先自己回答，再看下面的参考答案：
# 1. 这个知识点解决什么类型的问题？
# 2. 为什么当前案例需要它？
# 3. 每一步代码为什么要在此时出现？
# 4. 如果换一种做法，代价和风险是什么？

# 参考答案：
# 1. 突出两条曲线之间的范围和差额方向。
# 2. 需要快速识别哪些时间高于目标，哪些低于目标。
# 3. 先给边界和差额，再画线，最后按条件填色并解释交点。
# 4. 单独画线也能看差距；填色更突出但不自动代表概率区间或离散金额总和。

"""案例驱动示例：比较城市实际销售额和目标"""
# 对应 PDF：14-matplotlib-full.pdf 第 15—16 页
# 任务：比较三个城市实际与目标金额。
# 柱状图展示类别间大小；分组柱用左右偏移避免实际与目标互相覆盖。
# 案例数据：
# | city | actual | target |
# |---|---:|---:|
# | 上海 | 100 | 120 |
# | 北京 | 200 | 180 |
# | 深圳 | 150 | 160 |
# 先看整体路线：
# 第 1 步：先比较实际与目标的差额。
# 第 2 步：用bar展示类别金额，认识barh。
# 第 3 步：计算左右偏移画分组柱并放置类别刻度。

import numpy as np
import matplotlib.pyplot as plt
# 图内先用英文城市名避免未安装中文字体；第12节演示检测与使用中文字体。
labels=["Shanghai","Beijing","Shenzhen"]
actual=np.array([100,200,150])
target=np.array([120,180,160])
print('\n===== actual-target =====')
print(actual-target)
x=np.arange(len(labels))
width=.36
fig,axes=plt.subplots(1,2,figsize=(10,4))
# bar(x,height,width)返回柱子的容器；x是数值中心位置。
axes[0].bar(x-width/2,actual,width=width,label="Actual")
axes[0].bar(x+width/2,target,width=width,label="Target")
axes[0].set_xticks(x,labels=labels)
axes[0].set_ylabel("Sales (yuan)")
axes[0].set_title("Actual and target")
axes[0].legend()
# barh(y,width)是横向柱状图，width在这里表示数据值而非柱厚。
axes[1].barh(labels,actual)
axes[1].set(xlabel="Sales (yuan)",title="Actual sales")
fig.tight_layout()
assert len(axes[0].patches)==6
assert [p.get_height() for p in axes[0].patches[:3]]==[100,200,150]
plt.show()

# 学完先自己回答，再看下面的参考答案：
# 1. 这个知识点解决什么类型的问题？
# 2. 为什么当前案例需要它？
# 3. 每一步代码为什么要在此时出现？
# 4. 如果换一种做法，代价和风险是什么？

# 参考答案：
# 1. 比较类别数值与同类别的不同系列。
# 2. 城市是类别，实际和目标要成对比较。
# 3. 先算差额确认方向，再确定组中心与左右偏移，最后添加图例。
# 4. 同位置覆盖柱可能隐藏较小值；折线则容易暗示城市有连续距离关系。

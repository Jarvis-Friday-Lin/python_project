"""案例驱动示例：让图表不依赖口头解释"""
# 对应 PDF：14-matplotlib-full.pdf 第 11—12、15—16 页
# 任务：让读图者知道销量单位、日期和目标线含义。
# 颜色不能承担全部信息，标签、单位和刻度能减少误解。
# 案例数据：
# | day | sales |
# |---:|---:|
# | 1 | 10 |
# | 2 | 20 |
# | 3 | 15 |
# 先看整体路线：
# 第 1 步：先画缺乏说明的数据线，识别歧义。
# 第 2 步：增加标题、单位和图例。
# 第 3 步：设定刻度、网格和范围，并说明截断风险。

import matplotlib.pyplot as plt
fig,ax=plt.subplots(figsize=(6,4))
ax.plot([1,2,3],[10,20,15],marker="o",label="Sales")
# set_title/set_xlabel/set_ylabel各返回文字对象；不是创建新数据。
ax.set_title("Daily sales")
ax.set_xlabel("Day")
ax.set_ylabel("Sales (units)")
# set_xticks位置与标签一一对应；不要只改标签而不固定位置。
ax.set_xticks([1,2,3],labels=["Mon","Tue","Wed"])
ax.set_ylim(0,25)
ax.grid(axis="y",linestyle="--",alpha=.4)
ax.legend(loc="upper right")
# annotate(text,xy,xytext,arrowprops)标注具体坐标点。
ax.annotate("Peak: 20",xy=(2,20),xytext=(2.15,22),arrowprops={"arrowstyle":"->"})
fig.tight_layout()
assert ax.get_ylabel()=="Sales (units)"
assert [v.get_text() for v in ax.get_xticklabels()]==["Mon","Tue","Wed"]
# 可以缩小y范围观察细节，但必须显式保留刻度，别夸大微小变化。
plt.show()

# 学完先自己回答，再看下面的参考答案：
# 1. 这个知识点解决什么类型的问题？
# 2. 为什么当前案例需要它？
# 3. 每一步代码为什么要在此时出现？
# 4. 如果换一种做法，代价和风险是什么？

# 参考答案：
# 1. 给可视化补足业务语义与读数线索。
# 2. 数字20不说明单位就可能被理解为金额或数量。
# 3. 先有数据坐标，再设置刻度标签，最后标注峰值及辅助网格。
# 4. 仅靠颜色更短但不可自解释；过度装饰会遮挡信息，刻度截断可能夸大变化。


"""案例驱动示例：先回答问题再选择图形"""
# 对应 PDF：14-matplotlib-full.pdf 第 8—21 页综合
# 任务：同一份订单既有每日趋势，也有城市差异与金额分布，分别用合适的图回答。
# 不能把每一列都随便画成折线：图形要对应问题和数据类型。
# 案例数据：
# | day | city | amount |
# |---:|---|---:|
# | 1 | Shanghai | 100 |
# | 1 | Beijing | 200 |
# | 2 | Shanghai | 300 |
# | 2 | Beijing | 100 |
# | 3 | Shanghai | 200 |
# | 3 | Beijing | 300 |
# 先看整体路线：
# 第 1 步：用Pandas得到每日与城市汇总。
# 第 2 步：趋势用折线，类别比较用柱，分布用直方和箱线。
# 第 3 步：逐图检查对应数据，保存完整面板。

from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
data=pd.DataFrame({"day":[1,1,2,2,3,3],"city":["Shanghai","Beijing"]*3,"amount":[100,200,300,100,200,300]})
daily=data.groupby("day")["amount"].sum().sort_index()
city=data.groupby("city")["amount"].sum()
print('\n===== daily =====')
print(daily)
print('\n===== city =====')
print(city)
fig,axes=plt.subplots(2,2,figsize=(10,7))
axes[0,0].plot(daily.index,daily.to_numpy(),marker="o")
axes[0,0].set(title="Daily revenue",xlabel="Day",ylabel="Yuan")
axes[0,1].bar(city.index,city.to_numpy())
axes[0,1].set(title="City revenue",ylabel="Yuan")
axes[1,0].hist(data["amount"],bins=[50,150,250,350],edgecolor="black")
axes[1,0].set(title="Order amounts",xlabel="Yuan",ylabel="Orders")
groups=[group["amount"].to_numpy() for _,group in data.groupby("city")]
axes[1,1].boxplot(groups)
axes[1,1].set_xticks([1,2],labels=city.index)
axes[1,1].set(title="Amount by city",ylabel="Yuan")
fig.tight_layout()
out=Path(__file__).resolve().parent/"outputs"
out.mkdir(exist_ok=True)
fig.savefig(out/"orders_dashboard.png",dpi=160,bbox_inches="tight")
assert daily.tolist()==[300,400,500]
assert city.sum()==daily.sum()==1200
assert list(axes[0,0].lines[0].get_ydata())==[300,400,500]
plt.show()

# 学完先自己回答，再看下面的参考答案：
# 1. 这个知识点解决什么类型的问题？
# 2. 为什么当前案例需要它？
# 3. 每一步代码为什么要在此时出现？
# 4. 如果换一种做法，代价和风险是什么？

# 参考答案：
# 1. 将表格分析结果转换成对应问题的多图报告。
# 2. 时间、类别和分布是不同分析维度，单图回答不全。
# 3. 先汇总得到正确数据，再按问题选图，最后核对图元与汇总一致并保存。
# 4. 一张大折线容易混淆类别；多面板更全面，但要保持口径和分组顺序一致。

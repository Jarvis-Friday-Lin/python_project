"""案例驱动示例：用六张图交付销售分析"""
# 对应 PDF：三份PDF综合应用
# 任务：从固定销售数据做一份能解释趋势、城市表现、单价关系和金额分布的报告。
# 所有图来自同一份数据；不把不同口径的结果拼成看似统一的结论。
# 案例数据：
# | day | city | units | price | revenue |
# |---:|---|---:|---:|---:|
# | 1 | Shanghai | 2 | 50 | 100 |
# | 1 | Beijing | 2 | 100 | 200 |
# | 2 | Shanghai | 3 | 100 | 300 |
# | 2 | Beijing | 2 | 50 | 100 |
# | 3 | Shanghai | 4 | 50 | 200 |
# | 3 | Beijing | 3 | 100 | 300 |
# 先看整体路线：
# 第 1 步：校验收入等于数量乘单价，得到日与城市汇总。
# 第 2 步：画趋势、类别、散点、直方、箱线和目标差距六图。
# 第 3 步：检查图上数据和总额一致，输出报告与简短结论。

from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
course=Path(__file__).resolve().parents[2]
data=pd.read_csv(course/"datasets"/"sales_ready.csv")
assert np.allclose(data["units"]*data["price"],data["revenue"])
daily=data.groupby("day")["revenue"].sum().sort_index()
cities=data.groupby("city")["revenue"].sum()
target=np.full(len(daily),400)
fig,axes=plt.subplots(2,3,figsize=(14,8))
axes[0,0].plot(daily.index,daily,marker="o")
axes[0,0].set_xticks(daily.index)
axes[0,0].set(title="Daily revenue",xlabel="Day",ylabel="Yuan")
axes[0,1].bar(cities.index,cities)
axes[0,1].set(title="Revenue by city",ylabel="Yuan")
scatter=axes[0,2].scatter(data["price"],data["units"],c=data["revenue"],cmap="viridis")
# 6条记录仅有4种价量组合，重合点会遮挡；可见点少不等于记录丢失。
fig.colorbar(scatter,ax=axes[0,2],label="Revenue (yuan)")
axes[0,2].set(title="Price and units",xlabel="Price",ylabel="Units")
counts,_,_=axes[1,0].hist(data["revenue"],bins=[50,150,250,350],edgecolor="black")
axes[1,0].set(title="Revenue distribution",xlabel="Yuan",ylabel="Orders")
axes[1,0].set_yticks([0,1,2])
axes[1,1].boxplot([g["revenue"] for _,g in data.groupby("city")])
axes[1,1].set_xticks([1,2],labels=cities.index)
axes[1,1].set(title="City distributions",ylabel="Yuan")
axes[1,2].plot(daily.index,daily,label="Actual")
axes[1,2].plot(daily.index,target,linestyle="--",label="Target")
axes[1,2].fill_between(daily.index,daily,target,alpha=.2)
axes[1,2].set(title="Gap to daily target",xlabel="Day",ylabel="Yuan")
axes[1,2].legend()
axes[1,2].set_xticks(daily.index)
fig.tight_layout()
assert daily.tolist()==[300,400,500] and cities.sum()==1200
assert counts.tolist()==[2,2,2]
out=Path(__file__).resolve().parent/"outputs"
out.mkdir(exist_ok=True)
daily.rename("revenue").to_csv(out/"daily_revenue.csv",encoding="utf-8-sig")
fig.savefig(out/"sales_report.png",dpi=160,bbox_inches="tight")
fig.savefig(out/"sales_report.pdf",bbox_inches="tight")
print('\n===== "每日收入300→400→500；两城市累计均600。样本仅3天，不能据此保证未来继续增长。" =====')
print("每日收入300→400→500；两城市累计均600。样本仅3天，不能据此保证未来继续增长。")
print('\n===== "日目标400，累计实际1200与累计目标1200一致，但首日未达标，第三日超额。" =====')
print("日目标400，累计实际1200与累计目标1200一致，但首日未达标，第三日超额。")
# 散点只描述当前样本价量位置，单价与销量受商品构成等因素影响，不能直接认定需求规律。
plt.show()

# 学完先自己回答，再看下面的参考答案：
# 1. 这个知识点解决什么类型的问题？
# 2. 为什么当前案例需要它？
# 3. 每一步代码为什么要在此时出现？
# 4. 如果换一种做法，代价和风险是什么？

# 参考答案：
# 1. 将计算、统计、绘图与文字结论统一交付。
# 2. 业务需要同时看趋势、结构与分布，而不只是总额。
# 3. 先验证明细公式，再汇总，按问题画图，检查图元后输出可复查结论。
# 4. 只展示漂亮图可能掩盖错误口径；只输出表不易看趋势，组合时须确保来源一致。

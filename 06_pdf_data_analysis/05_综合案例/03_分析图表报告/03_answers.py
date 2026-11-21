"""参考答案：用六张图交付销售分析"""
# 对应 PDF：三份PDF综合应用
# 建议先完成 02_exercises.py；下面的实现与该题数据、要求一一对应。

from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
course=Path(__file__).resolve().parents[2]
data=pd.read_csv(course/"datasets"/"sales_ready.csv")
assert np.allclose(data["units"]*data["price"],data["revenue"])
daily=data.groupby("day")["revenue"].sum()
cities=data.groupby("city")["revenue"].sum()
fig,axes=plt.subplots(2,3,figsize=(14,8))
axes[0,0].plot(daily.index,daily,marker="o")
axes[0,0].set_xticks(daily.index)
axes[0,0].set(title="Daily revenue",xlabel="Day",ylabel="Yuan")
axes[0,1].bar(cities.index,cities)
axes[0,1].set(title="City revenue",ylabel="Yuan")
points=axes[0,2].scatter(data["price"],data["units"],c=data["revenue"])
fig.colorbar(points,ax=axes[0,2],label="Yuan")
axes[0,2].set(title="Price and units",xlabel="Price",ylabel="Units")
counts,_,_=axes[1,0].hist(data["revenue"],bins=[50,150,250,350])
axes[1,0].set(title="Revenue distribution",xlabel="Yuan",ylabel="Orders")
axes[1,0].set_yticks([0,1,2])
axes[1,1].boxplot([g["revenue"] for _,g in data.groupby("city")])
axes[1,1].set_xticks([1,2],labels=cities.index)
axes[1,1].set(title="By city",ylabel="Yuan")
axes[1,2].plot(daily.index,daily,label="Actual")
axes[1,2].plot(daily.index,[400]*3,label="Target")
axes[1,2].fill_between(daily.index,daily,400,alpha=.2)
axes[1,2].legend()
axes[1,2].set(title="Target gap",xlabel="Day",ylabel="Yuan")
axes[1,2].set_xticks(daily.index)
fig.tight_layout()
assert daily.tolist()==[300,400,500] and cities.tolist()==[600,600]
assert daily.sum()==1200 and counts.tolist()==[2,2,2]
assert list(axes[0,0].lines[0].get_ydata())==daily.tolist()
out=Path(__file__).resolve().parent/"outputs"
out.mkdir(exist_ok=True)
fig.savefig(out/"exercise_report.png",dpi=160,bbox_inches="tight")
fig.savefig(out/"exercise_report.pdf",bbox_inches="tight")
print('\n===== "每日收入300、400、500，三天累计1200；城市均600。" =====')
print("每日收入300、400、500，三天累计1200；城市均600。")
print('\n===== "首日低于日目标100，第三日高100，累计恰好达标。三天样本不足以外推未来。" =====')
print("首日低于日目标100，第三日高100，累计恰好达标。三天样本不足以外推未来。")
plt.show()

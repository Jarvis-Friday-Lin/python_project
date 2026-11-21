"""参考答案：先回答问题再选择图形"""
# 对应 PDF：14-matplotlib-full.pdf 第 8—21 页综合
# 建议先完成 02_exercises.py；下面的实现与该题数据、要求一一对应。

from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
data=pd.DataFrame({"day":[1,1,2,2,3,3],"city":["Shanghai","Beijing"]*3,"amount":[100,200,300,100,200,300]})
daily=data.groupby("day")["amount"].sum()
cities=data.groupby("city")["amount"].sum()
fig,axes=plt.subplots(2,2,figsize=(10,7))
axes[0,0].plot(daily.index,daily,marker="o")
axes[0,0].set(title="Daily total",xlabel="Day",ylabel="Yuan")
axes[0,1].bar(cities.index,cities)
axes[0,1].set(title="City total",ylabel="Yuan")
axes[1,0].hist(data["amount"],bins=[50,150,250,350])
axes[1,0].set(title="Amounts",xlabel="Yuan",ylabel="Orders")
axes[1,1].boxplot([g["amount"] for _,g in data.groupby("city")])
axes[1,1].set_xticks([1,2],labels=cities.index)
axes[1,1].set(title="By city",ylabel="Yuan")
fig.tight_layout()
out=Path(__file__).resolve().parent/"outputs"
out.mkdir(exist_ok=True)
fig.savefig(out/"exercise_dashboard.png",dpi=160,bbox_inches="tight")
assert daily.tolist()==[300,400,500] and cities.tolist()==[600,600]
assert daily.sum()==cities.sum()==1200
assert list(axes[0,0].lines[0].get_ydata())==daily.tolist()
plt.show()

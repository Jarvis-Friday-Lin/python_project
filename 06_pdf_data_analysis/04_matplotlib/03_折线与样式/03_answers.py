"""参考答案：对比实际销量与目标销量"""
# 对应 PDF：14-matplotlib-full.pdf 第 10—13 页
# 建议先完成 02_exercises.py；下面的实现与该题数据、要求一一对应。

import matplotlib.pyplot as plt
days=[1,2,3]
actual=[10,20,15]
target=[15,15,15]
fig,ax=plt.subplots()
ax.plot(days,actual,marker="o",linestyle="None",label="Actual")
ax.plot(days,target,color="red",linestyle="--",label="Target")
ax.legend()
ax.set(xlabel="Day",ylabel="Sales",title="Actual vs target")
assert [a-b for a,b in zip(actual,target)]==[-5,5,0]
assert ax.get_legend_handles_labels()[1]==["Actual","Target"]
assert len(ax.lines[0].get_ydata())==3
plt.show()

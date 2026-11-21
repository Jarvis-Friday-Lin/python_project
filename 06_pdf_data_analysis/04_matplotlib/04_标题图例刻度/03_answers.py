"""参考答案：让图表不依赖口头解释"""
# 对应 PDF：14-matplotlib-full.pdf 第 11—12、15—16 页
# 建议先完成 02_exercises.py；下面的实现与该题数据、要求一一对应。

import matplotlib.pyplot as plt
fig,ax=plt.subplots()
ax.plot([1,2,3],[10,20,15],label="Sales",marker="o")
ax.set(title="Daily sales",xlabel="Day",ylabel="Sales (units)",ylim=(0,25))
ax.set_xticks([1,2,3],labels=["Mon","Tue","Wed"])
ax.legend()
ax.grid(axis="y",linestyle="--",alpha=.4)
ax.annotate("Peak: 20",xy=(2,20),xytext=(2.1,22),arrowprops={"arrowstyle":"->"})
assert ax.get_ylabel()=="Sales (units)"
assert [t.get_text() for t in ax.get_xticklabels()]==["Mon","Tue","Wed"]
plt.show()

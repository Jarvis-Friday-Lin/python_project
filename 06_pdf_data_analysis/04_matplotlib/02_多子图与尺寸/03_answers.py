"""参考答案：把四家门店放在同一画布"""
# 对应 PDF：14-matplotlib-full.pdf 第 8、12 页
# 建议先完成 02_exercises.py；下面的实现与该题数据、要求一一对应。

import matplotlib.pyplot as plt
fig,axes=plt.subplots(2,2,figsize=(8,6),sharex=True,sharey=True)
for ax,(name,values) in zip(axes.flat,{"A":[10,20,15],"B":[20,30,25],"C":[30,20,10],"D":[40,50,45]}.items()):
    ax.plot([1,2,3],values,marker="o")
    ax.set(title="Store "+name,xlabel="Day",ylabel="Sales")
fig.tight_layout()
assert len(fig.axes)==4 and axes[1,0].get_title()=="Store C"
assert all(len(ax.lines)==1 and len(ax.lines[0].get_ydata())==3 for ax in axes.flat)
# subplots默认squeeze=True会去掉长度1的Axes数组维度。
plt.show()


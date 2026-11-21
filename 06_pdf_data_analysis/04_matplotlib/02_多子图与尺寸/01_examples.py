"""案例驱动示例：把四家门店放在同一画布"""
# 对应 PDF：14-matplotlib-full.pdf 第 8、12 页
# 任务：同一张图展示四家门店的三天销量。
# 多个Axes可以各自画图；如果默认缩放不同，视觉上的高低不能直接比较。
# 案例数据：
# | day | A | B | C | D |
# |---:|---:|---:|---:|---:|
# | 1 | 10 | 20 | 30 | 40 |
# | 2 | 20 | 30 | 20 | 50 |
# | 3 | 15 | 25 | 10 | 45 |
# 先看整体路线：
# 第 1 步：先决定2行2列的对比布局。
# 第 2 步：用二维数组索引找到每个Axes。
# 第 3 步：共享坐标轴并调整布局，避免尺度误导。

import matplotlib.pyplot as plt
days=[1,2,3]
stores={"A":[10,20,15],"B":[20,30,25],"C":[30,20,10],"D":[40,50,45]}
# nrows/ncols决定子图网格；sharey=True使四图使用同一销量刻度范围。
fig,axes=plt.subplots(nrows=2,ncols=2,figsize=(8,6),sharex=True,sharey=True)
print('\n===== axes.shape =====')
print(axes.shape)
# flat遍历二维Axes数组，图的位置按行展开。
for ax,(name,values) in zip(axes.flat,stores.items()):
    ax.plot(days,values,marker="o")
    ax.set_title("Store "+name)
    ax.set_xlabel("Day")
    ax.set_ylabel("Sales")
fig.suptitle("Store comparison")
# tight_layout给标题与标签留间距；rect为上方总标题留空间。
fig.tight_layout(rect=(0,0,1,.94))
assert axes.shape==(2,2)
assert len(fig.axes)==4
# 仅1图时默认axes是单个对象，不是二维数组；squeeze=False可始终返回二维数组。
print('\n===== axes[1,0].get_title() =====')
print(axes[1,0].get_title())
plt.show()

# 学完先自己回答，再看下面的参考答案：
# 1. 这个知识点解决什么类型的问题？
# 2. 为什么当前案例需要它？
# 3. 每一步代码为什么要在此时出现？
# 4. 如果换一种做法，代价和风险是什么？

# 参考答案：
# 1. 同画布布局多个相关视图。
# 2. 门店各有曲线，统一尺度才便于比较销量。
# 3. 先定布局，再逐图赋数据，最后共享刻度与调整间距。
# 4. 四次单独打开窗口也能看，但难并排且容易因自动刻度造成错觉。

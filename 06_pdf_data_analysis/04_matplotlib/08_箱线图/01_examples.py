"""案例驱动示例：均值相近的班级也可能很不同"""
# 对应 PDF：14-matplotlib-full.pdf 第 18、20 页
# 任务：比较两班成绩的中位数、波动和极端值。
# 箱体表示四分位区间，须通常延伸到1.5倍IQR范围内的最远观测值，不一定是最小最大值。
# 案例数据：
# | 班级 | 成绩 |
# |---|---|
# | A | 60,65,70,75,80 |
# | B | 60,65,70,75,100 |
# 先看整体路线：
# 第 1 步：先算四分位数与IQR。
# 第 2 步：画两个箱线图并设置外观。
# 第 3 步：对照异常点规则，避免直接把异常点当坏数据。

import numpy as np
import matplotlib.pyplot as plt
a=np.array([60,65,70,75,80])
b=np.array([60,65,70,75,100])
quartiles=np.percentile(b,[25,50,75])
q1,median,q3=quartiles
iqr=q3-q1
print('\n===== quartiles =====')
print(quartiles)
print('\n===== (q1-1.5*iqr,q3+1.5*iqr) =====')
print((q1-1.5*iqr,q3+1.5*iqr))
fig,ax=plt.subplots(figsize=(6,4))
# patch_artist让箱体可填色；notch=True显示中位数附近的近似缺口，不代表数据缺失。
# 为兼容多版本，刻度文字单独设置，不依赖版本变化中的labels参数名。
artists=ax.boxplot([a,b],patch_artist=True,notch=False,
                   boxprops={"facecolor":"lightblue"},medianprops={"color":"red"})
ax.set_xticks([1,2],labels=["Class A","Class B"])
ax.set(ylabel="Score",title="Score distributions")
print('\n===== artists["fliers"][1].get_ydata() =====')
print(artists["fliers"][1].get_ydata())
assert median==70 and iqr==10
assert list(artists["fliers"][1].get_ydata())==[100]
# 100分在统计规则中是离群点，但可能是真实优异成绩，不能自动删除。
plt.show()

# 学完先自己回答，再看下面的参考答案：
# 1. 这个知识点解决什么类型的问题？
# 2. 为什么当前案例需要它？
# 3. 每一步代码为什么要在此时出现？
# 4. 如果换一种做法，代价和风险是什么？

# 参考答案：
# 1. 用分位数比较分布和离群观测。
# 2. 只看均值会忽略班级内差异。
# 3. 先核对分位数和IQR，再看图元对应，最后区分离群与错误。
# 4. 直方图提供分布细节但多班对比占空间；箱线图紧凑，却隐藏多峰等结构。

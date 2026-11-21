"""案例驱动示例：在平面上显示温度变化"""
# 对应 PDF：14-matplotlib-full.pdf 第 22—23 页
# 任务：房间中心温度高，向外逐渐变低，用二维图表示三维关系。
# 等高线连接相同Z值的位置；X/Y/Z矩阵形状必须能对应同一批网格点。
# 案例数据：
# | x采样 | y采样 | 温度公式 |
# |---|---|---|
# | -2到2，共5点 | -2到2，共5点 | Z=30-X²-Y² |
# 先看整体路线：
# 第 1 步：生成横向与纵向采样坐标。
# 第 2 步：用meshgrid构造网格，计算每点温度。
# 第 3 步：对照等高线与填色等高线，用色条解释数值。

import numpy as np
import matplotlib.pyplot as plt
x=np.linspace(-2,2,5)
y=np.linspace(-2,2,5)
# meshgrid(x,y)默认xy索引，输出矩阵shape=(len(y),len(x))。
X,Y=np.meshgrid(x,y)
Z=30-X**2-Y**2
print('\n===== X =====')
print(X)
print('\n===== Y =====')
print(Y)
print('\n===== Z =====')
print(Z)
fig,axes=plt.subplots(1,2,figsize=(9,4))
# levels可以是数量或具体等值列表；选择值应落在实际Z范围内。
lines=axes[0].contour(X,Y,Z,levels=[22,24,26,28,30],cmap="viridis")
axes[0].clabel(lines,inline=True,fontsize=8)
filled=axes[1].contourf(X,Y,Z,levels=[22,24,26,28,30],cmap="viridis")
fig.colorbar(filled,ax=axes[1],label="Temperature")
for ax in axes:
    ax.set(xlabel="x",ylabel="y",aspect="equal")
axes[0].set_title("Contour")
axes[1].set_title("Filled contour")
fig.tight_layout()
assert X.shape==Y.shape==Z.shape==(5,5)
assert Z[2,2]==30 and Z[0,0]==22
plt.show()

# 学完先自己回答，再看下面的参考答案：
# 1. 这个知识点解决什么类型的问题？
# 2. 为什么当前案例需要它？
# 3. 每一步代码为什么要在此时出现？
# 4. 如果换一种做法，代价和风险是什么？

# 参考答案：
# 1. 在二维平面展示第三个数值变量。
# 2. 每个房间位置有温度，单条折线不能充分表达空间关系。
# 3. 先建坐标网格再算同shape的Z，最后选择等值级别并给色条。
# 4. 三维图也能画但易遮挡；网格细化改善视觉，不能伪装为更密的真实观测。

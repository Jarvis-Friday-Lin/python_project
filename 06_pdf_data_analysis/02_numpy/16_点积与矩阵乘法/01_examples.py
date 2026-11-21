"""案例驱动示例：计算加权总分与多套评分方案"""
# 对应 PDF：11-numpy-full.pdf 第 17—21 页
# 任务：Python、数学、英语权重分别0.5、0.3、0.2，计算每人综合分。
# 点积是对应相乘再相加；矩阵乘法将多组这样的计算一次组织起来。
# 案例数据：
# | 学生 | Python | 数学 | 英语 |
# |---|---:|---:|---:|
# | A | 80 | 70 | 90 |
# | B | 60 | 85 | 75 |
# 先看整体路线：
# 第 1 步：用zip与sum算一个人的加权分。
# 第 2 步：对比逐元素乘法和点积。
# 第 3 步：用矩阵乘法同时计算两套方案。

import numpy as np
scores=np.array([[80,70,90],[60,85,75]])
weights=np.array([.5,.3,.2])
print('\n===== sum(x*w for x,w in zip(scores[0],weights)) =====')
print(sum(x*w for x,w in zip(scores[0],weights)))
print('\n===== scores[0]*weights =====')
print(scores[0]*weights)
print('\n===== np.dot(scores[0],weights) =====')
print(np.dot(scores[0],weights))
print('\n===== scores @ weights =====')
print(scores @ weights)
# @ 与matmul做矩阵乘法，内部维度必须一致：(2,3)@(3,) -> (2,)。
print('\n===== np.matmul(scores,weights) =====')
print(np.matmul(scores,weights))
# dot还可以作为数组方法调用，一维/二维场景与上面的结果相同。
print('\n===== scores.dot(weights) =====')
print(scores.dot(weights))
# 每列是一套评分权重；(2,3)@(3,2) -> (2,2)。
schemes=np.array([[.5,.2],[.3,.3],[.2,.5]])
print('\n===== scores @ schemes =====')
print(scores @ schemes)
assert np.allclose(scores@weights,[79,70.5])
# 1D点积返回标量；2D矩阵乘法返回矩阵；逐元素*不做求和。
# 高于2维时dot与matmul的轴组合规则不同，不应把它们当作完全相同的别名。

# 学完先自己回答，再看下面的参考答案：
# 1. 这个知识点解决什么类型的问题？
# 2. 为什么当前案例需要它？
# 3. 每一步代码为什么要在此时出现？
# 4. 如果换一种做法，代价和风险是什么？

# 参考答案：
# 1. 把对应乘积合成为一个分数，并批量计算多个方案。
# 2. 综合分不是三列乘积的表，而是每人的一个加权总值。
# 3. 先看单人乘加，再理解点积，最后扩展为矩阵多方案。
# 4. 逐元素乘后sum容易检查；@简洁但必须核对内部维度和权重方向。

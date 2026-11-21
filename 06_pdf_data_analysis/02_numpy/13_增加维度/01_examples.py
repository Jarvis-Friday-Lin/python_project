"""案例驱动示例：行向量、列向量与长度1的轴"""
# 对应 PDF：11-numpy-full.pdf 第 29—34 页
# 任务：同一份三门科目的加分规则，要分别表示成一行或一列。
# 一维数组没有明确行列方向，增加长度1的轴后，方向才能参与广播判断。
# 案例数据：
# | Python加分 | 数学加分 | 英语加分 |
# |---:|---:|---:|
# | 5 | 2 | 3 |
# 先看整体路线：
# 第 1 步：先观察一维shape。
# 第 2 步：用newaxis与None创建行列形状。
# 第 3 步：用expand_dims在指定位置插入轴。

import numpy as np
bonus = np.array([5,2,3])
print('\n===== bonus.shape =====')
print(bonus.shape)
# newaxis是None的别名；每出现一次就插入一根长度1的轴。
row = bonus[np.newaxis, :]
column = bonus[:, None]
print('\n===== row =====')
print(row)
print('\n===== column =====')
print(column)
# expand_dims(a,axis) 的axis指定新增轴在结果中的位置。
print('\n===== np.expand_dims(bonus, axis=0) =====')
print(np.expand_dims(bonus, axis=0))
print('\n===== np.expand_dims(bonus, axis=1) =====')
print(np.expand_dims(bonus, axis=1))
table = np.arange(6).reshape(2,3)
print('\n===== np.expand_dims(table, axis=1).shape =====')
print(np.expand_dims(table, axis=1).shape)
print('\n===== np.expand_dims(table, axis=2).shape =====')
print(np.expand_dims(table, axis=2).shape)
assert row.shape == (1,3) and column.shape == (3,1)
assert np.array_equal(row,np.expand_dims(bonus,0))
assert np.expand_dims(table,1).shape==(2,1,3)
# 增轴没有新增分数；size保持不变。

# 学完先自己回答，再看下面的参考答案：
# 1. 这个知识点解决什么类型的问题？
# 2. 为什么当前案例需要它？
# 3. 每一步代码为什么要在此时出现？
# 4. 如果换一种做法，代价和风险是什么？

# 参考答案：
# 1. 明确一维数据的方向，构造可广播形状。
# 2. 同样三个加分值，按行或按列作用含义不同。
# 3. 先观察原shape，再指定新轴位置，最后核对size没有变化。
# 4. reshape也能实现这次增轴，但newaxis更直接表达只插入长度1的轴。

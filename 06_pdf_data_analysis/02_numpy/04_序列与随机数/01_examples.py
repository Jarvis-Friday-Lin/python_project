"""案例驱动示例：生成编号、采样点和可重复数据"""
# 对应 PDF：11-numpy-full.pdf 第 4、28、63—66 页；linspace 衔接 Matplotlib 第13页
# 任务：生成 20 到 60 的编号，以及可重复的模拟成绩。
# 模拟数据只用于练习，不代表真实统计结论。
# 案例数据：
# | 起始编号 | 末尾编号 | 采样起点 | 采样终点 | 采样数量 |
# |---:|---:|---:|---:|---:|
# | 20 | 60 | 0 | 1 | 5 |
# 先看整体路线：
# 第 1 步：用 range 理解左闭右开。
# 第 2 步：对比 arange 的步长与 linspace 的点数。
# 第 3 步：固定随机种子，以便复现结果。

import numpy as np
print('\n===== list(range(20, 61)) =====')
print(list(range(20, 61)))
# arange(start,stop,step) 通常不含 stop；整数编号最适合用它。
ids = np.arange(20, 61)
print('\n===== ids =====')
print(ids)
# linspace(start,stop,num) 默认包含终点；num 是点数，不是步长。
points = np.linspace(0, 1, num=5)
print('\n===== points =====')
print(points)
# default_rng 返回随机生成器；seed=42 让教学输出可重现。
rng = np.random.default_rng(seed=42)
scores = rng.integers(low=60, high=101, size=(2, 3))
print('\n===== scores =====')
print(scores)
# integers 的 high 不包含；均匀随机小数 random 在 [0,1)，normal 给正态样本。
print('\n===== rng.random((2, 2)) =====')
print(rng.random((2, 2)))
print('\n===== rng.normal(loc=80, scale=5, size=3) =====')
print(rng.normal(loc=80, scale=5, size=3))
# PDF 的 np.random.rand(2,3) 是旧式全局随机接口，下面展示其调用形状。
print('\n===== np.random.default_rng(7).random((2, 3)).shape =====')
print(np.random.default_rng(7).random((2, 3)).shape)
assert len(ids) == 41 and ids[-1] == 60
assert np.allclose(points, [0,.25,.5,.75,1])

# 学完先自己回答，再看下面的参考答案：
# 1. 这个知识点解决什么类型的问题？
# 2. 为什么当前案例需要它？
# 3. 每一步代码为什么要在此时出现？
# 4. 如果换一种做法，代价和风险是什么？

# 参考答案：
# 1. 程序化生成规律序列和可复现的测试数据。
# 2. 编号和采样点各有不同的终点要求。
# 3. 先确定是否含终点，再选步长或点数，随机数据最后固定种子。
# 4. 手写方便观察少数值，但难扩展；不固定种子会让答案难对照。

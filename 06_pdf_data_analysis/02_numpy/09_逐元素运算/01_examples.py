"""案例驱动示例：计算售价、收入与误差"""
# 对应 PDF：11-numpy-full.pdf 第 15、63—66 页
# 任务：两件商品调价，计算收入和预测误差。
# 逐元素运算把同位置的数一对一组合，与矩阵乘法不是一回事。
# 案例数据：
# | 商品 | 单价 | 数量 | 预测销量 |
# |---|---:|---:|---:|
# | A | 10 | 2 | 3 |
# | B | 20 | 3 | 1 |
# 先看整体路线：
# 第 1 步：用循环计算每件商品的收入。
# 第 2 步：用数组运算符及同义函数重算。
# 第 3 步：引出绝对误差、平方根和对数的适用范围。

import numpy as np
prices = np.array([10.,20.])
counts = np.array([2.,3.])
forecast = np.array([3.,1.])
print('\n===== [p*q for p,q in zip(prices,counts)] =====')
print([p*q for p,q in zip(prices,counts)])
print('\n===== prices * counts =====')
print(prices * counts)
# add/subtract/multiply/divide 与 + - * / 对应，返回逐元素结果。
print('\n===== np.add(prices, 5) =====')
print(np.add(prices, 5))
print('\n===== np.subtract(counts, forecast) =====')
print(np.subtract(counts, forecast))
print('\n===== np.multiply(prices, counts) =====')
print(np.multiply(prices, counts))
print('\n===== np.divide(prices, 2) =====')
print(np.divide(prices, 2))
# abs 让正负误差都成为距离；sqrt 返回非负实数的平方根。
error = counts - forecast
print('\n===== np.abs(error) =====')
print(np.abs(error))
print('\n===== np.sqrt(error ** 2) =====')
print(np.sqrt(error ** 2))
# log 是自然对数，数据应为正数；0会得到-inf，负实数得到nan，不能无脑套用。
print('\n===== np.log(prices) =====')
print(np.log(prices))
assert (prices*counts).tolist() == [20,60]
assert np.array_equal(np.abs(error), np.sqrt(error**2))

# 学完先自己回答，再看下面的参考答案：
# 1. 这个知识点解决什么类型的问题？
# 2. 为什么当前案例需要它？
# 3. 每一步代码为什么要在此时出现？
# 4. 如果换一种做法，代价和风险是什么？

# 参考答案：
# 1. 一对一数值计算和误差转换。
# 2. 单价必须与对应商品销量相乘，不能交叉混算。
# 3. 先对应字段，再计算收入，误差先求差后取绝对值才不会抵消。
# 4. zip循环适合小数据；数组更简洁，但形状和运算含义须核对。

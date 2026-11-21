"""参考答案：为四种商品单价准备行列向量"""
# 对应 PDF：11-numpy-full.pdf 第 29—34 页
# 课件核心：第29—34页：newaxis、None、expand_dims与新增长度1的轴。
# 扩展：无。
# 案例数据（据此自行创建对象，不能照抄 examples 的数据）：
# | item | unit_price |
# |---|---|
# | pen | 3 |
# | ruler | 5 |
# | notebook | 8 |
# | folder | 12 |
# 建议先做练习，再逐段对照下面的实现；assert 用于验证结果。

import numpy as np
price = np.array([3,5,8,12])
row, column = price[None, :], price[:, np.newaxis]
# axis是插入后新轴的位置；0插在最前，1插在一维数组后。
row2, column2 = np.expand_dims(price, 0), np.expand_dims(price, 1)
print('\n===== (row.shape, column.shape) =====')
print((row.shape, column.shape))
assert np.array_equal(row, row2) and np.array_equal(column, column2)
assert np.array_equal(column.T, row)
assert row.shape == (1,4) and column.shape == (4,1)
stock = np.array([price, price * 2])
expanded = np.expand_dims(stock, axis=1)
print('\n===== expanded =====')
print(expanded)
assert expanded.shape == (2,1,4) and expanded.size == stock.size == 8

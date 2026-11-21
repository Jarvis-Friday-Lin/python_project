"""参考答案：按各站点指定时段提取用电量"""
# 对应 PDF：11-numpy-full.pdf 第 9—10 页
# 课件核心：第9—10页：配对整数索引、逐行选值及原位更新。
# 扩展：np.ix_建立行列交叉子表是扩展，区别于配对取值。
# 案例数据（据此自行创建对象，不能照抄 examples 的数据）：
# | station | morning | noon | evening | selected_column_index |
# |---|---|---|---|---|
# | S1 | 12 | 18 | 21 | 0 |
# | S2 | 10 | 16 | 24 | 2 |
# | S3 | 14 | 20 | 22 | 1 |
# | S4 | 9 | 15 | 19 | 2 |
# 建议先做练习，再逐段对照下面的实现；assert 用于验证结果。

import numpy as np
a = np.array([[12,18,21],[10,16,24],[14,20,22],[9,15,19]])
original = a.copy()
rows, columns = np.arange(4), np.array([0,2,1,2])
print('\n===== a[rows, columns] =====')
print(a[rows, columns])
assert a[rows, columns].tolist() == [12,24,20,19]
a[rows, columns] += 2
print('\n===== a =====')
print(a)
# 用原表构造预期更新表，验证没有误更新其他位置。
expected = original.copy()
for r, c in zip(rows, columns):
    expected[r, c] += 2
assert np.array_equal(a, expected)
# 扩展：ix_将两个一维索引转换成可广播的行列网格。
cross = a[np.ix_([0,2], [0,2])]
print('\n===== cross =====')
print(cross)
assert cross.tolist() == [[14,21],[14,22]]

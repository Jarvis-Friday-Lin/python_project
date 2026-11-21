"""参考答案：追加测量并反推两种零件单价"""
# 对应 PDF：11-numpy-full.pdf 第20—21、63—66页
# 课件核心：第63—66页：append、repeat、full、linalg.inv；第20—21页矩阵乘法。
# 扩展：无；用逆矩阵反推仅用于本题小型非奇异系统，不推广为数值求解首选。
# 案例数据（据此自行创建对象，不能照抄 examples 的数据）：
# | 数据 | 内容 |
# |---|---|
# | 已测尺寸I | [4,7] |
# | 新测尺寸 | [9,11] |
# | 校准值 | 6，重复4次 |
# | 系数矩阵A | [[3,1],[1,2]] |
# | 两笔总价b | [16,12] |
# 建议先做练习，再逐段对照下面的实现；assert 用于验证结果。

import numpy as np
I = np.array([4,7])
extended = np.append(I, [9,11])
print('\n===== extended =====')
print(extended)
assert I.tolist() == [4,7] and extended.tolist() == [4,7,9,11]
assert np.array_equal(np.repeat(6,4), np.full(4,6))
A = np.array([[3,1],[1,2]])
b = np.array([16,12])
inverse = np.linalg.inv(A)
prices = inverse @ b
print('\n===== prices =====')
print(prices)
assert np.allclose(A @ inverse, np.eye(2))
assert np.allclose(prices, [4,4]) and np.allclose(A @ prices, b)
# 若矩阵两行成倍数，方程约束不独立，矩阵奇异，没有唯一逆矩阵。

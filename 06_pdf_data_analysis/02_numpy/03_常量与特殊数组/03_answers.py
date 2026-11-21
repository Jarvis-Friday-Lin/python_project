"""参考答案：建立停车场状态模板"""
# 对应 PDF：11-numpy-full.pdf 第4、13、17—21、63—66页；矩阵性质作为后续复习
# 课件核心：第4页：zeros、ones、full、eye。
# 扩展：无；整数dtype沿用第13页。
# 案例数据（据此自行创建对象，不能照抄 examples 的数据）：
# | 模板 | 行数 | 列数 | 初始值 |
# |---|---|---|---|
# | 空车位 | 3 | 4 | 0 |
# | 可用标记 | 3 | 4 | 1 |
# | 未检测状态 | 3 | 4 | -9 |
# | 车道关系 | 4 | 4 | 主对角线1，其余0 |
# 建议先做练习，再逐段对照下面的实现；assert 用于验证结果。

import numpy as np
empty = np.zeros((3, 4), dtype=int)
available = np.ones((3, 4), dtype=int)
unknown = np.full((3, 4), -9, dtype=int)
lanes = np.eye(4, dtype=int)
unknown[1, 2] = 1
print('\n===== empty =====')
print(empty)
print('\n===== available =====')
print(available)
print('\n===== unknown =====')
print(unknown)
print('\n===== lanes =====')
print(lanes)
print('\n===== [x.shape for x in [empty, available, unknown, lanes]] =====')
print([x.shape for x in [empty, available, unknown, lanes]])
assert empty.sum() == 0 and available.sum() == 12
assert (unknown == -9).sum() == 11 and unknown[1, 2] == 1
# 单位矩阵的乘法性质在课件第17—21页学习后再验证。
assert np.array_equal(lanes @ np.array([2, 4, 6, 8]), [2, 4, 6, 8])

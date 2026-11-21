"""参考答案：创建默认成绩与计算模板"""
# 对应 PDF：11-numpy-full.pdf 第 4、63—66 页
# 建议先完成 02_exercises.py；下面的实现与该题数据、要求一一对应。

import numpy as np
zero = np.zeros((2,3), dtype=int)
pending = np.full((2,3), -1, dtype=int)
identity = np.eye(3, dtype=int)
print('\n===== zero =====')
print(zero)
print('\n===== pending =====')
print(pending)
print('\n===== identity =====')
print(identity)
assert zero.shape == pending.shape == (2,3)
assert np.all(pending == -1)
assert np.array_equal(identity.diagonal(), [1,1,1])
assert np.array_equal(np.full(5,8), np.repeat(8,5))

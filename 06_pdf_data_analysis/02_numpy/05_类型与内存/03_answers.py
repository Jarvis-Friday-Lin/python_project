"""参考答案：重量测量值的精度与内存"""
# 对应 PDF：11-numpy-full.pdf 第13—14、36、54、63页
# 课件核心：第13—14、54页：dtype和内存；astype见第36页。
# 扩展：nbytes用于直接核对元素缓冲区，不包括对象头。
# 案例数据（据此自行创建对象，不能照抄 examples 的数据）：
# | package | weight |
# |---|---|
# | A | 12 |
# | B | 17 |
# | C | 23 |
# 建议先做练习，再逐段对照下面的实现；assert 用于验证结果。

import numpy as np
original = np.array([12, 17, 23], dtype=np.int16)
# astype(dtype) 默认创建转换后的副本，避免在整数容器中截断小数。
precise = original.astype(np.float64)
precise[1] = 17.75
truncated = original.copy()
truncated[1] = 17.75
print('\n===== precise =====')
print(precise)
print('\n===== truncated =====')
print(truncated)
print('\n===== (original.nbytes, precise.nbytes) =====')
print((original.nbytes, precise.nbytes))
assert precise[1] == 17.75 and truncated[1] == 17
assert original.nbytes == 6 and precise.nbytes == 24
assert original.tolist() == [12, 17, 23]

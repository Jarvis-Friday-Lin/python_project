"""参考答案：给气象站逐传感器校准并中心化"""
# 对应 PDF：11-numpy-full.pdf 第 37—46 页
# 课件核心：第37—46页：广播规则及按列中心化。
# 扩展：无；数据表最后两行是参数，不是站点测量行。
# 案例数据（据此自行创建对象，不能照抄 examples 的数据）：
# | station | sensor1 | sensor2 | sensor3 |
# |---|---|---|---|
# | A | 10 | 20 | 30 |
# | B | 14 | 24 | 34 |
# | 校准偏移 | -1 | 2 | 0 |
# | 每站追加偏移 | A加1 | B减2 | 不属于数据列 |
# 建议先做练习，再逐段对照下面的实现；assert 用于验证结果。

import numpy as np
a = np.array([[10,20,30],[14,24,34]])
column_offset = np.array([-1,2,0])
calibrated = a + column_offset
row_offset = np.array([1,-2])[:, None]
final = calibrated + row_offset
centered = a - a.mean(axis=0)
print('\n===== calibrated =====')
print(calibrated)
print('\n===== final =====')
print(final)
print('\n===== centered =====')
print(centered)
print('\n===== (a.shape, column_offset.shape, row_offset.shape, final.shape) =====')
print((a.shape, column_offset.shape, row_offset.shape, final.shape))
assert calibrated.tolist() == [[9,22,30],[13,26,34]]
assert final.tolist() == [[10,23,31],[11,24,32]]
assert np.allclose(centered.mean(axis=0), 0)
assert a.tolist() == [[10,20,30],[14,24,34]]
# (2,3)与(2,)的末尾维度3和2不兼容；(2,1)能按行扩展。

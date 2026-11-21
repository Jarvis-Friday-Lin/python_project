"""参考答案：筛查冷链箱温度是否合格"""
# 对应 PDF：11-numpy-full.pdf 第 11—12 页
# 课件核心：第11—12页：布尔掩码、&、|、~；区间2到8均含端点。
# 扩展：all(axis=1)、any(axis=1)为从元素条件到整行条件的扩展。
# 案例数据（据此自行创建对象，不能照抄 examples 的数据）：
# | box | sensor1 | sensor2 |
# |---|---|---|
# | C1 | 2 | 8 |
# | C2 | 1 | 6 |
# | C3 | 5 | 9 |
# | C4 | 4 | 7 |
# 建议先做练习，再逐段对照下面的实现；assert 用于验证结果。

import numpy as np
names = np.array(['C1','C2','C3','C4'])
a = np.array([[2,8],[1,6],[5,9],[4,7]])
ok = (a >= 2) & (a <= 8)
print('\n===== a[ok] =====')
print(a[ok])
print('\n===== a[(a < 2) | (a > 8)] =====')
print(a[(a < 2) | (a > 8)])
assert np.array_equal(a[~ok], [1,9])
# 扩展：axis=1把每箱的两次判断归并成一个布尔值。
good_boxes = ok.all(axis=1)
bad_boxes = (~ok).any(axis=1)
print('\n===== a[good_boxes] =====')
print(a[good_boxes])
print('\n===== names[bad_boxes] =====')
print(names[bad_boxes])
assert names[good_boxes].tolist() == ['C1','C4']
assert names[bad_boxes].tolist() == ['C2','C3']
assert a[a > 100].size == 0

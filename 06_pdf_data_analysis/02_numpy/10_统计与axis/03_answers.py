"""参考答案：门店每天用水量的统计轴"""
# 对应 PDF：11-numpy-full.pdf 第 22、46、63—66 页
# 课件核心：第22、46、63—66页：mean、sum、min、max、std、median及axis。
# 扩展：keepdims和ddof参数的比较为扩展。
# 案例数据（据此自行创建对象，不能照抄 examples 的数据）：
# | shop | Mon | Tue | Wed |
# |---|---|---|---|
# | A | 10 | 14 | 18 |
# | B | 20 | 22 | 24 |
# | C | 6 | 9 | 12 |
# 建议先做练习，再逐段对照下面的实现；assert 用于验证结果。

import numpy as np
a = np.array([[10,14,18],[20,22,24],[6,9,12]])
daily = a.mean(axis=0)
totals = a.sum(axis=1)
print('\n===== daily =====')
print(daily)
print('\n===== totals =====')
print(totals)
print('\n===== a.max(axis=0) =====')
print(a.max(axis=0))
print('\n===== a.min(axis=1) =====')
print(a.min(axis=1))
print('\n===== np.median(a) =====')
print(np.median(a))
assert np.allclose(daily, [12,15,18])
assert totals.tolist() == [42,66,27]
assert a.max(axis=0).tolist() == [20,22,24] and np.median(a) == 14
assert a.min(axis=1).tolist() == [10,20,6]
# 扩展：ddof控制分母为N-ddof，样本标准差(ddof=1)在这里更大。
population, sample = a.std(axis=0, ddof=0), a.std(axis=0, ddof=1)
print('\n===== (population, sample) =====')
print((population, sample))
assert (sample > population).all()
assert a.mean(axis=0, keepdims=True).shape == (1,3)

"""参考答案：把摄氏温度批量换算为华氏温度"""
# 扩展：无新增API；温度换算公式是案例背景。
# 案例数据（据此自行创建对象，不能照抄 examples 的数据）：
# | 时刻 | celsius |
# |---|---|
# | 08:00 | -10 |
# | 12:00 | 0 |
# | 16:00 | 25 |
# | 20:00 | 40 |
# 建议先做练习，再逐段对照下面的实现；assert 用于验证结果。

import numpy as np
celsius = [-10, 0, 25, 40]
manual = [v * 1.8 + 32 for v in celsius]
a = np.array(celsius)
fahrenheit = a * 1.8 + 32
print('\n===== fahrenheit =====')
print(fahrenheit)
print('\n===== fahrenheit.max() =====')
print(fahrenheit.max())
assert np.allclose(fahrenheit, manual)
assert np.allclose((fahrenheit - 32) / 1.8, a)
assert np.array_equal(a, celsius)
assert fahrenheit.max() == 104
# 列表乘整数重复列表；数组乘标量则逐元素计算。

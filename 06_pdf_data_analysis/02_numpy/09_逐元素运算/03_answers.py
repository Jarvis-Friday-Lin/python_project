"""参考答案：比较三种材料的采购成本"""
# 对应 PDF：11-numpy-full.pdf 第 15、63—66 页
# 课件核心：第15、63—66页：逐元素乘减除、abs、sqrt。
# 扩展：无新增API；成本公式为业务应用。
# 案例数据（据此自行创建对象，不能照抄 examples 的数据）：
# | material | price | actual_units | planned_units |
# |---|---|---|---|
# | 木料 | 12 | 3 | 2 |
# | 钢件 | 7 | 4 | 6 |
# | 塑料 | 5 | 8 | 8 |
# 建议先做练习，再逐段对照下面的实现；assert 用于验证结果。

import numpy as np
price, actual, planned = np.array([12,7,5]), np.array([3,4,8]), np.array([2,6,8])
actual_cost, planned_cost = price * actual, price * planned
print('\n===== actual_cost =====')
print(actual_cost)
print('\n===== planned_cost =====')
print(planned_cost)
print('\n===== actual_cost - planned_cost =====')
print(actual_cost - planned_cost)
discount_total = (price * 0.8 * actual).sum()
print('\n===== discount_total =====')
print(discount_total)
assert actual_cost.tolist() == [36,28,40]
assert (actual_cost - planned_cost).tolist() == [12,-14,0]
assert np.isclose(discount_total, 83.2)
assert np.array_equal(np.abs(actual - planned), np.sqrt((actual - planned)**2))
# 此处每个材料单独乘自己的数量，因此用逐元素乘法而非点积。

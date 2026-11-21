"""参考答案：按配料量计算两种采购方案成本"""
# 对应 PDF：11-numpy-full.pdf 第 17—21 页
# 课件核心：第17—21页：点积、矩阵乘向量、矩阵乘矩阵。
# 扩展：无；配料单位一致，单价为元/单位。
# 案例数据（据此自行创建对象，不能照抄 examples 的数据）：
# | recipe | flour | sugar | oil |
# |---|---|---|---|
# | R1 | 2 | 1 | 1 |
# | R2 | 1 | 3 | 2 |
# | 方案A单价 | 4 | 6 | 10 |
# | 方案B单价 | 5 | 5 | 8 |
# 建议先做练习，再逐段对照下面的实现；assert 用于验证结果。

import numpy as np
recipes = np.array([[2,1,1],[1,3,2]])
prices_a, prices_b = np.array([4,6,10]), np.array([5,5,8])
cost_a = recipes @ prices_a
print('\n===== cost_a =====')
print(cost_a)
assert np.array_equal(cost_a, (recipes * prices_a).sum(axis=1))
assert np.array_equal(cost_a, recipes.dot(prices_a))
assert np.array_equal(cost_a, np.matmul(recipes, prices_a))
prices = np.array([prices_a, prices_b]).T
costs = recipes @ prices
print('\n===== costs =====')
print(costs)
assert costs.tolist() == [[24,23],[42,36]]
# recipes为(2,3)，prices为(3,2)，相乘时内侧维度3一致。

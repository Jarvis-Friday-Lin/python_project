"""参考答案：试算折扣时保护原商品价格"""
# 对应 PDF：11-numpy-full.pdf 第 35—36 页
# 课件核心：第35—36页：基本切片视图、copy、高级索引副本。
# 扩展：shares_memory用于检验是否共享数据，属于诊断扩展。
# 案例数据（据此自行创建对象，不能照抄 examples 的数据）：
# | item | price |
# |---|---|
# | A | 15 |
# | B | 25 |
# | C | 35 |
# | D | 45 |
# 建议先做练习，再逐段对照下面的实现；assert 用于验证结果。

import numpy as np
price = np.array([15,25,35,45])
view = price[1:3]
view[0] = 20
assert price.tolist() == [15,20,35,45]
trial = price.copy()
trial -= 5
picked = price[[0,3]]
picked[0] = 0
print('\n===== price =====')
print(price)
print('\n===== trial =====')
print(trial)
print('\n===== picked =====')
print(picked)
# 扩展：shares_memory(a,b)检查两个数组实际是否共享内存。
assert np.shares_memory(price, view)
assert not np.shares_memory(price, trial)
assert not np.shares_memory(price, picked)
assert price.tolist() == [15,20,35,45] and trial.tolist() == [10,15,30,40]

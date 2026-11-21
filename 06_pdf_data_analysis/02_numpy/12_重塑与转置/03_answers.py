"""参考答案：传感器扁平数据的重排"""
# 对应 PDF：11-numpy-full.pdf 第 23—28 页
# 课件核心：第23—28页：reshape、-1自动推断、transpose和一维转置。
# 扩展：无。
# 案例数据（据此自行创建对象，不能照抄 examples 的数据）：
# | 数据 | 定义 |
# |---|---|
# | readings | 从10到33共24个连续整数 |
# | 初始布局 | 2台机器×3天×4个时段 |
# | 目标布局 | 4个时段×2台机器×3天 |
# 建议先做练习，再逐段对照下面的实现；assert 用于验证结果。

import numpy as np
readings = np.arange(10,34)
source = readings.reshape(2,3,4)
target = source.transpose(2,0,1)
print('\n===== target =====')
print(target)
print('\n===== (target.shape, target[3, 1, 2]) =====')
print((target.shape, target[3,1,2]))
assert target.shape == (4,2,3)
assert target[3,1,2] == source[1,2,3] == 33
assert not np.array_equal(target, readings.reshape(4,2,3))
assert readings.reshape(6,-1).shape == (6,4)
assert readings.T.shape == (24,)
# reshape按元素遍历顺序重新分组；transpose改变轴的角色，不是同一种重排。

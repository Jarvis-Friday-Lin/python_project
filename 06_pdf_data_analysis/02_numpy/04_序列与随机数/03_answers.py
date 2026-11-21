"""参考答案：生成采样时刻与模拟湿度"""
# 对应 PDF：11-numpy-full.pdf 第 4、28、63—66 页；linspace 衔接 Matplotlib 第13页
# 课件核心：NumPy第4、28、63—66页的arange和随机数组；Matplotlib第13页linspace。
# 扩展：default_rng和固定种子为可复现性补充；不假定固定随机输出值。
# 案例数据（据此自行创建对象，不能照抄 examples 的数据）：
# | 数据 | 起点 | 终点 | 规则 |
# |---|---|---|---|
# | 编号 | 102 | 126 | 间隔4，包含126 |
# | 时间 | 0 | 2 | 等距9点，含两端 |
# | 湿度 | 40 | 60 | 2×4随机小数，种子7 |
# 建议先做练习，再逐段对照下面的实现；assert 用于验证结果。

import numpy as np
ids = np.arange(102, 127, 4)
times = np.linspace(0, 2, 9)
# default_rng(seed) 创建生成器；random(shape) 返回 [0,1) 随机值，再缩放和平移。
humidity = 40 + 20 * np.random.default_rng(7).random((2, 4))
same = 40 + 20 * np.random.default_rng(7).random((2, 4))
print('\n===== ids =====')
print(ids)
print('\n===== times =====')
print(times)
print('\n===== humidity =====')
print(humidity)
assert len(ids) == 7 and ids[-1] == 126
assert np.allclose(np.diff(times), 0.25)
assert np.array_equal(humidity, same)
assert ((humidity >= 40) & (humidity < 60)).all()

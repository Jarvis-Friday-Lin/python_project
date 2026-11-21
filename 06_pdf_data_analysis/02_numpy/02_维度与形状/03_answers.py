"""参考答案：两台机器三天的温度结构"""
# 对应 PDF：11-numpy-full.pdf 第 3、8、16 页
# 课件核心：第3、8、16页：ndarray、维数、形状、向量/矩阵。
# 扩展：size是数组元素数量属性；用轴含义解释三维结构。
# 案例数据（据此自行创建对象，不能照抄 examples 的数据）：
# | machine | day1 | day2 | day3 |
# |---|---|---|---|
# | M1 | 31 | 34 | 33 |
# | M2 | 28 | 30 | 29 |
# 建议先做练习，再逐段对照下面的实现；assert 用于验证结果。

import numpy as np
temperature = np.array([[31, 34, 33], [28, 30, 29]])
workshops = np.array([temperature, temperature - 2])
print('\n===== (temperature.ndim, temperature.shape, temperature.size) =====')
print((temperature.ndim, temperature.shape, temperature.size))
print('\n===== workshops[1, 1, 2] =====')
print(workshops[1, 1, 2])
assert (temperature.ndim, temperature.shape, temperature.size) == (2, (2, 3), 6)
assert workshops.shape == (2, 2, 3) and workshops[1, 1, 2] == 27
assert temperature[0].shape == (3,) and temperature[0:1].shape == (1, 3)
# 三根轴依次表示车间、机器、日期；整数索引会消去被选中的轴。

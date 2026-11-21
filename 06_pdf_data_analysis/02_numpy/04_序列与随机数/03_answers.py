"""参考答案：生成编号、采样点和可重复数据"""
# 对应 PDF：11-numpy-full.pdf 第 4、28、63—66 页；linspace 衔接 Matplotlib 第13页
# 建议先完成 02_exercises.py；下面的实现与该题数据、要求一一对应。

import numpy as np
ids = np.arange(20,61)
points = np.linspace(0,1,5)
a = np.random.default_rng(42).random((3,3,3))
b = np.random.default_rng(42).random((3,3,3))
print('\n===== ids[::-1] =====')
print(ids[::-1])
print('\n===== points =====')
print(points)
print('\n===== a =====')
print(a)
assert len(ids) == 41 and ids[::-1][0] == 60
assert np.allclose(points,[0,.25,.5,.75,1])
assert np.array_equal(a,b) and np.all((a>=0)&(a<1))

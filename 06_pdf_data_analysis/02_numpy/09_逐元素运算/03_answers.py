"""参考答案：计算售价、收入与误差"""
# 对应 PDF：11-numpy-full.pdf 第 15、63—66 页
# 建议先完成 02_exercises.py；下面的实现与该题数据、要求一一对应。

import numpy as np
prices=np.array([10.,20.])
counts=np.array([2.,3.])
forecast=np.array([3.,1.])
income=prices*counts
mae=np.abs(counts-forecast).mean()
print('\n===== income =====')
print(income)
print('\n===== mae =====')
print(mae)
print('\n===== (prices*.9*counts).sum() =====')
print((prices*.9*counts).sum())
assert income.tolist()==[20,60]
assert mae==1.5
assert np.isclose((prices*.9*counts).sum(),72)
# 实数自然对数定义域是正数，0是趋向负无穷的边界，负实数无实值对数。

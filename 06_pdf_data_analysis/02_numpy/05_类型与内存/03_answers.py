"""参考答案：为什么整数数组写入小数会丢精度"""
# 对应 PDF：11-numpy-full.pdf 第 13—14、54、63 页
# 建议先完成 02_exercises.py；下面的实现与该题数据、要求一一对应。

import numpy as np
a = np.array([80,90],dtype=np.int32)
b = a.astype(np.float64)
b[0] = 80.5
direct = np.array([80.5,90],dtype=float)
print('\n===== b =====')
print(b)
print('\n===== (a.nbytes,b.nbytes) =====')
print((a.nbytes,b.nbytes))
assert a.nbytes == 8 and b.nbytes == 16
assert np.array_equal(b,direct)
assert a[0] == 80

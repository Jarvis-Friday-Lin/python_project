"""参考答案：提取学生、科目与保持维度"""
# 对应 PDF：11-numpy-full.pdf 第 5—8、63—66 页
# 建议先完成 02_exercises.py；下面的实现与该题数据、要求一一对应。

import numpy as np
a = np.array([[80,70,90],[60,85,75],[90,65,80]])
print('\n===== a[:,2] =====')
print(a[:,2])
print('\n===== a[0:1,:] =====')
print(a[0:1,:])
print('\n===== a[::2,1::2] =====')
print(a[::2,1::2])
assert a[:,2].tolist()==[90,75,80]
assert a[0:1,:].shape==(1,3)
assert a[::2,1::2].tolist()==[[70],[65]]
assert np.array_equal(a[::-1][0],a[-1])

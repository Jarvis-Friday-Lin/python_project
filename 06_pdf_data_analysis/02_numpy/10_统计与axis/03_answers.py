"""参考答案：到底在算学生平均还是科目平均"""
# 对应 PDF：11-numpy-full.pdf 第 22、46、63—66 页
# 建议先完成 02_exercises.py；下面的实现与该题数据、要求一一对应。

import numpy as np
a=np.array([[80,70,90],[60,85,75]])
print('\n===== a.mean(axis=0) =====')
print(a.mean(axis=0))
print('\n===== a.sum(axis=0) =====')
print(a.sum(axis=0))
print('\n===== a.max(axis=1) =====')
print(a.max(axis=1))
print('\n===== np.median(a) =====')
print(np.median(a))
print('\n===== a.std(axis=0,ddof=0) =====')
print(a.std(axis=0,ddof=0))
print('\n===== a.std(axis=0,ddof=1) =====')
print(a.std(axis=0,ddof=1))
assert np.allclose(a.mean(axis=0),[70,77.5,82.5])
assert np.allclose(a.mean(axis=1),[80,220/3])
assert a.sum(axis=0).tolist()==[140,155,165]
assert a.max(axis=1).tolist()==[90,85]
assert np.median(a)==77.5
assert a.mean(axis=0,keepdims=True).shape==(1,3)

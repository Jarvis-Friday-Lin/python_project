"""参考答案：行向量、列向量与长度1的轴"""
# 对应 PDF：11-numpy-full.pdf 第 29—34 页
# 建议先完成 02_exercises.py；下面的实现与该题数据、要求一一对应。

import numpy as np
a=np.array([5,2,3])
row=a[None,:]
col=a[:,None]
print('\n===== row =====')
print(row)
print('\n===== col =====')
print(col)
assert row.shape==(1,3) and col.shape==(3,1)
assert np.array_equal(row,np.expand_dims(a,0))
assert np.array_equal(col,np.expand_dims(a,1))
assert row.size==col.size==3
assert np.expand_dims(np.zeros((2,3)),1).shape==(2,1,3)

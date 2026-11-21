"""参考答案：计算加权总分与多套评分方案"""
# 对应 PDF：11-numpy-full.pdf 第 17—21 页
# 建议先完成 02_exercises.py；下面的实现与该题数据、要求一一对应。

import numpy as np
a=np.array([[80,70,90],[60,85,75]])
w=np.array([.5,.3,.2])
schemes=np.array([[.5,.2],[.3,.3],[.2,.5]])
print('\n===== a@w =====')
print(a@w)
print('\n===== a@schemes =====')
print(a@schemes)
assert np.allclose(a@w,[79,70.5])
assert np.allclose((a*w).sum(axis=1),a@w)
assert np.allclose(a@schemes,[[79,82],[70.5,75]])

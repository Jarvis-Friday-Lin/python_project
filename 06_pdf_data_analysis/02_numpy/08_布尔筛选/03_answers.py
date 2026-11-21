"""参考答案：找出达标成绩和达标学生"""
# 对应 PDF：11-numpy-full.pdf 第 11—12 页
# 建议先完成 02_exercises.py；下面的实现与该题数据、要求一一对应。

import numpy as np
a=np.array([[80,90],[60,85],[95,55]])
print('\n===== a[(a>=80)&(a<=90)] =====')
print(a[(a>=80)&(a<=90)])
print('\n===== a[(a>=60).all(axis=1)] =====')
print(a[(a>=60).all(axis=1)])
print('\n===== a[(a>=90).any(axis=1)] =====')
print(a[(a>=90).any(axis=1)])
assert a[(a>=80)&(a<=90)].tolist()==[80,90,85]
assert a[(a>=60).all(axis=1)].tolist()==[[80,90],[60,85]]
assert a[(a>=90).any(axis=1)].tolist()==[[80,90],[95,55]]
assert a[a>100].size==0

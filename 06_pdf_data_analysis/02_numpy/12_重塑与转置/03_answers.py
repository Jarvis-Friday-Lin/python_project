"""参考答案：把连续成绩整理成不同维度"""
# 对应 PDF：11-numpy-full.pdf 第 23—28 页
# 建议先完成 02_exercises.py；下面的实现与该题数据、要求一一对应。

import numpy as np
a=np.arange(12).reshape(3,4)
print('\n===== a.T =====')
print(a.T)
print('\n===== a.reshape(4,3) =====')
print(a.reshape(4,3))
assert a.T[1].tolist()==[1,5,9]
assert a.reshape(4,3)[1].tolist()==[3,4,5]
cube=np.arange(24).reshape(2,3,4)
b=cube.transpose(2,0,1)
assert b.shape==(4,2,3)
assert b[3,1,2]==cube[1,2,3]==23

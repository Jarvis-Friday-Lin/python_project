"""参考答案：修改子表为什么影响原成绩"""
# 对应 PDF：11-numpy-full.pdf 第 35—36 页
# 建议先完成 02_exercises.py；下面的实现与该题数据、要求一一对应。

import numpy as np
a=np.array([80,90,70])
view=a[1:]
view[0]=0
assert a.tolist()==[80,0,70]
trial=a.copy()
trial[0]=100
fancy=a[[0,2]]
fancy[0]=-1
print('\n===== a =====')
print(a)
print('\n===== trial =====')
print(trial)
assert a.tolist()==[80,0,70]
assert np.shares_memory(a,view)
assert not np.shares_memory(a,trial)
assert not np.shares_memory(a,fancy)

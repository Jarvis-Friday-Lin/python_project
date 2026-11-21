"""参考答案：每人选择不同科目的成绩"""
# 对应 PDF：11-numpy-full.pdf 第 9—10 页
# 建议先完成 02_exercises.py；下面的实现与该题数据、要求一一对应。

import numpy as np
a=np.array([[80,70,90],[60,85,75],[90,65,80]])
rows=np.arange(3)
cols=np.array([2,0,1])
assert a[rows,cols].tolist()==[90,60,65]
a[rows,cols]+=5
print('\n===== a =====')
print(a)
print('\n===== a[np.ix_([0,2],[0,2])] =====')
print(a[np.ix_([0,2],[0,2])])
assert a[rows,cols].tolist()==[95,65,70]
assert a[np.ix_([0,2],[0,2])].shape==(2,2)

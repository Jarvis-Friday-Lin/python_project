"""参考答案：从一名学生到多个班级"""
# 对应 PDF：11-numpy-full.pdf 第 3、8、16 页
# 建议先完成 02_exercises.py；下面的实现与该题数据、要求一一对应。

import numpy as np
scores = np.array([[80,70,90],[60,85,75]])
classes = np.array([scores, scores + 1])
print('\n===== (scores.ndim, scores.shape, scores.size) =====')
print((scores.ndim, scores.shape, scores.size))
print('\n===== classes[1,0,2] =====')
print(classes[1,0,2])
assert (scores.ndim, scores.shape, scores.size) == (2,(2,3),6)
assert classes.shape == (2,2,3)
assert classes[1,0,2] == 91

"""参考答案：排名之后如何找回学生"""
# 对应 PDF：11-numpy-full.pdf 第 63—66 页
# 建议先完成 02_exercises.py；下面的实现与该题数据、要求一一对应。

import numpy as np
names=np.array(["A","B","C","D"])
scores=np.array([80,95,70,95])
order=np.argsort(-scores,kind="stable")
print('\n===== names[order] =====')
print(names[order])
print('\n===== names[scores==scores.max()] =====')
print(names[scores==scores.max()])
print('\n===== np.nonzero(scores>=90)[0] =====')
print(np.nonzero(scores>=90)[0])
assert names[order].tolist()==["B","D","A","C"]
assert names[scores==scores.max()].tolist()==["B","D"]
assert np.nonzero(scores>=90)[0].tolist()==[1,3]
assert names[scores.argmin()]=="C"

"""参考答案：补充样本并反推线性关系"""
# 对应 PDF：11-numpy-full.pdf 第 63—66 页
# 建议先完成 02_exercises.py；下面的实现与该题数据、要求一一对应。

import numpy as np
a=np.array([1,2,3])
new=np.append(a,[4,5,6])
print('\n===== new =====')
print(new)
matrix=np.array([[2.,0.],[0.,4.]])
inverse=np.linalg.inv(matrix)
print('\n===== inverse =====')
print(inverse)
print('\n===== np.linalg.solve(matrix,[6.,8.]) =====')
print(np.linalg.solve(matrix,[6.,8.]))
assert a.tolist()==[1,2,3] and len(new)==6
assert np.repeat(a,2).tolist()==[1,1,2,2,3,3]
assert np.allclose(matrix@inverse,np.eye(2))
assert np.allclose(np.linalg.solve(matrix,[6.,8.]),[3,2])
# 两行成比例，矩阵奇异，不存在逆矩阵。

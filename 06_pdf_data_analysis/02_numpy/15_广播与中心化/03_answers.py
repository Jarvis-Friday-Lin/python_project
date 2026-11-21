"""参考答案：不同科目加不同分，再计算偏离均值"""
# 对应 PDF：11-numpy-full.pdf 第 37—46 页
# 建议先完成 02_exercises.py；下面的实现与该题数据、要求一一对应。

import numpy as np
a=np.array([[80,70,90],[60,85,75],[90,65,80]])
adjusted=a+np.array([5,2,3])
centered=a-a.mean(axis=0,keepdims=True)
student_adjusted=a+np.array([1,2,3])[:,None]
print('\n===== adjusted =====')
print(adjusted)
print('\n===== centered =====')
print(centered)
print('\n===== student_adjusted =====')
print(student_adjusted)
assert adjusted[0].tolist()==[85,72,93]
assert np.allclose(centered.mean(axis=0),0,atol=1e-12)
assert student_adjusted[1].tolist()==[62,87,77]
# 尾轴3与2既不相等也没有1；(3,1)的尾轴1则可扩成3。

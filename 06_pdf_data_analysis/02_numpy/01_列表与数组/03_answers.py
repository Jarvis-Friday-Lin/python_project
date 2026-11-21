"""参考答案：给成绩批量加分"""
# 对应 PDF：11-numpy-full.pdf 第 2、52—56 页
# 建议先完成 02_exercises.py；下面的实现与该题数据、要求一一对应。

import numpy as np
scores = [80, 90, 70]
loop = [x + 5 for x in scores]
a = np.array(scores)
print('\n===== a + 5 =====')
print(a + 5)
print('\n===== a * 2 =====')
print(a * 2)
assert (a + 5).tolist() == loop == [85, 95, 75]
assert (a * 2).tolist() == [160, 180, 140]
assert a.tolist() == scores
# 列表 *2 重复其元素序列，数组 *2 对数值做乘法。

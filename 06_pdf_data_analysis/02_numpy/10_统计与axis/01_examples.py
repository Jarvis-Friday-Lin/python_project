"""案例驱动示例：到底在算学生平均还是科目平均"""
# 对应 PDF：11-numpy-full.pdf 第 22、46、63—66 页
# 任务：给教务处分别报告各科平均、每人平均、全体平均。
# axis 指被压缩的轴：axis=0 跨学生汇总，剩下科目；axis=1 跨科目汇总，剩下学生。
# 案例数据：
# | 学生 | Python | 数学 | 英语 |
# |---|---:|---:|---:|
# | A | 80 | 70 | 90 |
# | B | 60 | 85 | 75 |
# 先看整体路线：
# 第 1 步：用基础求和分别计算行列均值。
# 第 2 步：用 axis 对照结果形状。
# 第 3 步：展示其他统计和标准差口径。

import numpy as np
a = np.array([[80,70,90],[60,85,75]])
print('\n===== [sum(row)/len(row) for row in a] =====')
print([sum(row)/len(row) for row in a])
print('\n===== [sum(a[:,j])/len(a) for j in range(3)] =====')
print([sum(a[:,j])/len(a) for j in range(3)])
print('\n===== a.mean(axis=0) =====')
print(a.mean(axis=0))
print('\n===== a.mean(axis=1) =====')
print(a.mean(axis=1))
print('\n===== a.mean() =====')
print(a.mean())
print('\n===== a.sum(axis=0) =====')
print(a.sum(axis=0))
print('\n===== a.min(axis=0) =====')
print(a.min(axis=0))
print('\n===== a.max(axis=1) =====')
print(a.max(axis=1))
print('\n===== np.median(a, axis=0) =====')
print(np.median(a, axis=0))
# std(ddof=0) 是总体标准差；ddof=1 按样本方差口径除以n-1。
print('\n===== a.std(axis=0, ddof=0) =====')
print(a.std(axis=0, ddof=0))
print('\n===== a.std(axis=0, ddof=1) =====')
print(a.std(axis=0, ddof=1))
# keepdims=True 保留长度1的被汇总轴，后面做广播时很有用。
print('\n===== a.mean(axis=0, keepdims=True) =====')
print(a.mean(axis=0, keepdims=True))
assert a.mean(axis=0).shape == (3,)
assert a.mean(axis=1).shape == (2,)
assert a.mean(axis=0, keepdims=True).shape == (1,3)

# 学完先自己回答，再看下面的参考答案：
# 1. 这个知识点解决什么类型的问题？
# 2. 为什么当前案例需要它？
# 3. 每一步代码为什么要在此时出现？
# 4. 如果换一种做法，代价和风险是什么？

# 参考答案：
# 1. 沿指定轴汇总多个数。
# 2. 按人和按科目是不同问题，不能只写一个mean。
# 3. 先命名轴，再汇总，再核对输出长度与业务对象数。
# 4. 手工计算易验证小样本；直接用默认axis=None可能把所有数混成一个。

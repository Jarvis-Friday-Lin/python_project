"""案例驱动示例：排名之后如何找回学生"""
# 对应 PDF：11-numpy-full.pdf 第 63—66 页
# 任务：按成绩排名，并找回第一名在原名单中的位置。
# 排序后的数值与原始位置是两种信息，不能混用。
# 案例数据：
# | 位置 | 学生 | 分数 |
# |---:|---|---:|
# | 0 | A | 80 |
# | 1 | B | 95 |
# | 2 | C | 70 |
# | 3 | D | 95 |
# 先看整体路线：
# 第 1 步：先用排序后的索引维护姓名分数对应。
# 第 2 步：比较 sort 与 argsort。
# 第 3 步：展示最大最小位置和非零位置。

import numpy as np
names = np.array(["A","B","C","D"])
scores = np.array([80,95,70,95])
manual = sorted(range(len(scores)), key=lambda i: scores[i])
print('\n===== manual =====')
print(manual)
print('\n===== np.sort(scores) =====')
print(np.sort(scores))
# argsort 返回“按这些位置取数就能升序”的索引，不直接返回分数。
order = np.argsort(scores, kind="stable")
print('\n===== names[order] =====')
print(names[order])
print('\n===== scores[order] =====')
print(scores[order])
# 稳定降序用对负分数稳定排序；简单[::-1]会反转同分人的相对顺序。
descending = np.argsort(-scores, kind="stable")
print('\n===== names[descending] =====')
print(names[descending])
# 并列最大时 argmax 只给第一个位置；要全部，用布尔筛选。
print('\n===== scores.argmax() =====')
print(scores.argmax())
print('\n===== names[scores == scores.max()] =====')
print(names[scores == scores.max()])
print('\n===== np.nonzero(scores >= 90) =====')
print(np.nonzero(scores >= 90))
print('\n===== scores.argmin() =====')
print(scores.argmin())
assert names[descending].tolist() == ["B","D","A","C"]

# 学完先自己回答，再看下面的参考答案：
# 1. 这个知识点解决什么类型的问题？
# 2. 为什么当前案例需要它？
# 3. 每一步代码为什么要在此时出现？
# 4. 如果换一种做法，代价和风险是什么？

# 参考答案：
# 1. 获得排名、位置与并列结果。
# 2. 只排序分数会失去与学生身份的联系。
# 3. 先保存原顺序，再排序索引，最后用同一索引取姓名和分数。
# 4. Python sorted足够完成；数组索引方便同步排序多份数据，但并列策略必须明确。

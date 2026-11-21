"""案例驱动示例：给成绩批量加分"""
# 对应 PDF：11-numpy-full.pdf 第 2、52—56 页
# NumPy 是用于数值计算的库，核心对象 ndarray 用来存放成批的同类型数值。
# 任务：三名学生各加 5 分。先证明列表也能做，再看数组把哪部分循环交给了库。
# 案例数据：
# | 学生 | 原分数 |
# |---|---:|
# | 小林 | 80 |
# | 小周 | 90 |
# | 小陈 | 70 |
# 先看整体路线：
# 第 1 步：用循环创建加分后的列表。
# 第 2 步：用数组实现同一计算，区分列表重复与数值乘法。
# 第 3 步：核对输入未变和两种结果一致。

import numpy as np
scores = [80, 90, 70]
adjusted_list = []
for score in scores:
    adjusted_list.append(score + 5)
print('\n===== adjusted_list =====')
print(adjusted_list)
# 循环能够完成，但每次增加运算都要继续描述怎样遍历。
# np.array 的第一个参数是数据；返回 ndarray，而不是改造原列表。
array = np.array(scores)
adjusted_array = array + 5
print('\n===== adjusted_array =====')
print(adjusted_array)
# +5 对每个元素做加法；新结果独立保存，原数组仍是原分数。
print('\n===== array =====')
print(array)
# 同一个 * 在不同对象上含义不同：列表重复，数组逐元素乘。
print('\n===== scores * 2 =====')
print(scores * 2)
print('\n===== array * 2 =====')
print(array * 2)
assert adjusted_array.tolist() == adjusted_list == [85, 95, 75]
assert scores == [80, 90, 70]

# 学完先自己回答，再看下面的参考答案：
# 1. 这个知识点解决什么类型的问题？
# 2. 为什么当前案例需要它？
# 3. 每一步代码为什么要在此时出现？
# 4. 如果换一种做法，代价和风险是什么？

# 参考答案：
# 1. 批量数值运算。
# 2. 同一加分规则要作用到所有成绩。
# 3. 先有循环作为正确基准，再建立数组，再比较相同输入下的结果。
# 4. 列表无需额外库，小数据很方便；连续数值运算用数组表达更直接。

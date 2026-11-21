"""案例驱动示例：从一名学生到多个班级"""
# 对应 PDF：11-numpy-full.pdf 第 3、8、16 页
# 任务：存放两名学生的三门成绩，再保存两个班级。
# shape 像收纳柜各方向的格数；ndim 是方向数量，不是学生人数。
# 案例数据：
# | 学生 | Python | 数学 | 英语 |
# |---|---:|---:|---:|
# | 小林 | 80 | 70 | 90 |
# | 小周 | 60 | 85 | 75 |
# 先看整体路线：
# 第 1 步：先创建一名学生的一维成绩。
# 第 2 步：扩展成二维表，检查形状和元素总数。
# 第 3 步：在表外再套一层，表示多个班级。

import numpy as np
one = np.array([80, 70, 90])
scores = np.array([[80, 70, 90], [60, 85, 75]])
print('\n===== one.shape =====')
print(one.shape)
print('\n===== scores.shape =====')
print(scores.shape)
# ndim 是轴的数量，size 是所有格子的数量；shape 是每个轴的长度元组。
print('\n===== (scores.ndim, scores.size) =====')
print((scores.ndim, scores.size))
classes = np.array([scores, scores + 1])
print('\n===== classes.shape =====')
print(classes.shape)
print('\n===== classes[1, 0, 2] =====')
print(classes[1, 0, 2])
# (3,) 只有一个轴；并不等于“明确的一行三列”(1,3)。
assert one.shape == (3,)
assert scores.shape == (2, 3)
assert classes.shape == (2, 2, 3)
assert classes[1, 0, 2] == 91

# 学完先自己回答，再看下面的参考答案：
# 1. 这个知识点解决什么类型的问题？
# 2. 为什么当前案例需要它？
# 3. 每一步代码为什么要在此时出现？
# 4. 如果换一种做法，代价和风险是什么？

# 参考答案：
# 1. 描述数组组织方式及每个轴的业务含义。
# 2. 同样六个数字可以表示两人三科，也可以表示三人两科。
# 3. 先约定轴含义，创建后检查形状，才能用正确的索引取值。
# 4. 嵌套列表同样能存数据，但 shape 与批量多维计算需自己维护。

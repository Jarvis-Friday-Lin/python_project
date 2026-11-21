"""案例驱动示例：修改子表为什么影响原成绩"""
# 对应 PDF：11-numpy-full.pdf 第 35—36 页
# 任务：试着调整部分学生成绩，但要保留原始成绩作为对照。
# 视图像同一个房间的另一扇窗，副本像另外建了一个房间。
# 案例数据：
# | 学生 | 分数 |
# |---|---:|
# | A | 80 |
# | B | 90 |
# | C | 70 |
# 先看整体路线：
# 第 1 步：演示普通变量赋值不是复制。
# 第 2 步：用切片观察共享内存。
# 第 3 步：使用copy隔离试算，比较高级索引。

import numpy as np
a = np.array([80,90,70])
alias = a
alias[0] = 81
print('\n===== a =====')
print(a)
view = a[1:]
# shares_memory(a,b) 检查是否共享底层元素内存，而不是只比数值。
print('\n===== np.shares_memory(a,view) =====')
print(np.shares_memory(a,view))
view[0] = 0
print('\n===== a =====')
print(a)
# 需要试算时先copy；修改试算结果不应污染原表。
trial = a.copy()
trial[0] = 100
print('\n===== trial =====')
print(trial)
print('\n===== a =====')
print(a)
fancy = a[[0,2]]
fancy[0] = -1
print('\n===== np.shares_memory(a,fancy) =====')
print(np.shares_memory(a,fancy))
assert a.tolist()==[81,0,70]
assert trial.tolist()==[100,0,70]
# reshape可能返回视图，也可能需要复制，取决于内存布局。
# 因此不要把“reshape永远是视图”当作保证；用shares_memory核实。

# 学完先自己回答，再看下面的参考答案：
# 1. 这个知识点解决什么类型的问题？
# 2. 为什么当前案例需要它？
# 3. 每一步代码为什么要在此时出现？
# 4. 如果换一种做法，代价和风险是什么？

# 参考答案：
# 1. 控制修改范围，防止原始数据被试算污染。
# 2. 需要同时保留原成绩和调整成绩。
# 3. 先验证共享行为，再copy隔离，最后修改并同时检查两份数据。
# 4. 全部copy简单但额外占内存；全部用视图快，却必须清楚副作用。

"""案例驱动示例：创建默认成绩与计算模板"""
# 任务：为两名学生的三门作业建立初始表。
# 大量相同初值无需逐格手写；不过 0 分与“未提交”是不同业务状态。
# 案例数据：
# | 学生数 | 科目数 | 已提交初值 | 待确认标记 |
# |---:|---:|---:|---:|
# | 2 | 3 | 0 | -1 |
# 先看整体路线：
# 第 1 步：先用嵌套推导式建立初始表。
# 第 2 步：用 zeros、ones、full 表达不同初值。
# 第 3 步：认识单位矩阵与 repeat，并说明使用边界。

import numpy as np
manual = [[0 for _ in range(3)] for _ in range(2)]
print('\n===== manual =====')
print(manual)
# shape=(2,3) 是两人三科；dtype=int 避免默认浮点显示。
zero = np.zeros((2, 3), dtype=int)
print('\n===== zero =====')
print(zero)
print('\n===== np.ones((2, 3), dtype=int) =====')
print(np.ones((2, 3), dtype=int))
# full 的第二个参数 fill_value 是每个格子的值。
pending = np.full((2, 3), fill_value=-1, dtype=int)
print('\n===== pending =====')
print(pending)
# eye(N) 生成 N×N 对角线为1的矩阵，后面用来验证矩阵乘法。
identity = np.eye(3, dtype=int)
print('\n===== identity =====')
print(identity)
# repeat(a,repeats) 重复元素；full 更适合直接指定整张表的形状。
print('\n===== np.repeat(8, 5) =====')
print(np.repeat(8, 5))
assert zero.tolist() == manual
assert np.all(pending == -1)
# PDF 第66页的 no.full 是笔误，正确写法是 np.full。

# 学完先自己回答，再看下面的参考答案：
# 1. 这个知识点解决什么类型的问题？
# 2. 为什么当前案例需要它？
# 3. 每一步代码为什么要在此时出现？
# 4. 如果换一种做法，代价和风险是什么？

# 参考答案：
# 1. 按形状和初值生成数组。
# 2. 初始化表格时，重复写数字易漏格也不好调整人数。
# 3. 先明确初值含义，再选择 zeros/full，最后检查形状类型。
# 4. 手写列表适合少量不同数值；批量相同初值用构造函数更清晰。

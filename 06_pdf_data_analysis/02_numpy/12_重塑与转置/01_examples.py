"""案例驱动示例：把连续成绩整理成不同维度"""
# 对应 PDF：11-numpy-full.pdf 第 23—28 页
# 任务：把12个连续数整理为3人4科的表，再换成按科目查看。
# reshape 改分组方式，transpose 交换坐标轴，二者不能因为形状相同就互换。
# 案例数据：
# | 连续数据 | 人数 | 科目数 |
# |---|---:|---:|
# | 0,1,2,3,4,5,6,7,8,9,10,11 | 3 | 4 |
# 先看整体路线：
# 第 1 步：先确定元素总数不变，再reshape。
# 第 2 步：用T交换二维行列，比较与重塑结果。
# 第 3 步：展示三维轴交换与一维转置不变。

import numpy as np
flat = np.arange(12)
# reshape(3,-1) 让NumPy推导另一个轴为4；只能有一个-1。
table = flat.reshape(3, -1)
print('\n===== table =====')
print(table)
print('\n===== table.T =====')
print(table.T)
print('\n===== table.reshape(4,3) =====')
print(table.reshape(4,3))
# T按坐标交换，reshape按遍历顺序重新分组，下面两个结果不同。
assert not np.array_equal(table.T, table.reshape(4,3))
cube = np.arange(24).reshape(2,3,4)
# axes=(2,0,1)：旧第2轴成为新第0轴，旧第0轴成为新第1轴。
moved = np.transpose(cube, axes=(2,0,1))
print('\n===== moved.shape =====')
print(moved.shape)
print('\n===== (cube[1,2,3], moved[3,1,2]) =====')
print((cube[1,2,3], moved[3,1,2]))
print('\n===== flat.T.shape =====')
print(flat.T.shape)
assert moved.shape == (4,2,3)
assert flat.T.shape == (12,)
# 12个元素不能reshape成(5,3)；这里保持为注释，正常运行不故意抛错。

# 学完先自己回答，再看下面的参考答案：
# 1. 这个知识点解决什么类型的问题？
# 2. 为什么当前案例需要它？
# 3. 每一步代码为什么要在此时出现？
# 4. 如果换一种做法，代价和风险是什么？

# 参考答案：
# 1. 改变数据布局与轴顺序。
# 2. 按人读与按科目读，需要交换两个业务轴。
# 3. 先核对元素总数，再选重塑或换轴，最后检查坐标映射。
# 4. 循环可重排但冗长；误用reshape可能形状对了而数据含义错了。

"""案例驱动示例：补充样本并反推线性关系"""
# 对应 PDF：11-numpy-full.pdf 第 63—66 页
# 任务：先把新成绩追加到样本，再用一个可逆矩阵反推未知量。
# 这两项来自文档末尾操作题，各有适用条件，不把求逆当作普通表格清洗。
# 案例数据：
# | 数组I | 追加值 | 系数矩阵A | 结果b |
# |---|---|---|---|
# | 1,2,3 | 4,5,6 | [[2,0],[0,4]] | [6,8] |
# 先看整体路线：
# 第 1 步：用列表extend作追加基准。
# 第 2 步：展示append、concatenate、repeat的不同。
# 第 3 步：验证逆矩阵，再用solve直接解方程。

import numpy as np
manual=[1,2,3]
manual.extend([4,5,6])
a=np.array([1,2,3])
# np.append返回新数组，不会就地扩容；不写axis时会先展平。
joined=np.append(a,[4,5,6])
print('\n===== joined =====')
print(joined)
print('\n===== np.concatenate((a,np.array([4,5,6])),axis=0) =====')
print(np.concatenate((a,np.array([4,5,6])),axis=0))
print('\n===== np.repeat(a,2) =====')
print(np.repeat(a,2))
assert a.tolist()==[1,2,3] and joined.tolist()==manual
matrix=np.array([[2.,0.],[0.,4.]])
b=np.array([6.,8.])
# 生活里的对应：A商品每箱2件、合计6件；B每箱4件、合计8件。
# 两个未知数是箱数，matrix@箱数=b，求得[3,2]；对角结构让我们能手工核对。
inverse=np.linalg.inv(matrix)
print('\n===== inverse =====')
print(inverse)
print('\n===== inverse@b =====')
print(inverse@b)
print('\n===== np.linalg.solve(matrix,b) =====')
print(np.linalg.solve(matrix,b))
assert np.allclose(matrix@inverse,np.eye(2))
assert np.allclose(np.linalg.solve(matrix,b),[3,2])
# inv需要方阵且非奇异；奇异矩阵不能求逆。
# 真正解Ax=b时，通常直接solve更合适，避免先显式构造逆矩阵。

# 学完先自己回答，再看下面的参考答案：
# 1. 这个知识点解决什么类型的问题？
# 2. 为什么当前案例需要它？
# 3. 每一步代码为什么要在此时出现？
# 4. 如果换一种做法，代价和风险是什么？

# 参考答案：
# 1. 追加数组、重复元素和处理可逆线性系统。
# 2. 追加样本需要保留旧数组；反推数量需要解线性关系。
# 3. 先比较追加的返回行为，再计算逆并验证，最后展示更直接的solve。
# 4. 循环append数组会频繁分配；显式求逆可教学，但解方程优先solve。

import numpy as np

A = np.array([[1, 2],
              [3, 4]])
B = np.array([[5, 6],
              [7, 8]])


print(np.dot(A, B))
print(np.matmul(A, B))
print(A @ B)
# ✅ 二维情况下 dot、matmul、@ 完全等价。



a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print(np.dot(a, b))     # 32  （内积，标量）
print(np.matmul(a, b))  # 32
print(a @ b)            # 32
# 一维时都算内积 → 结果一样。


A = np.array([[1, 2], [3, 4]])

print(np.dot(A, 10))
# [[10 20]
#  [30 40]]        ✅ dot 允许标量，逐元素乘

# print(np.matmul(A, 10))
# ❌ ValueError: matmul: Input operand 1 does not have enough dimensions
#    (has 0, gufunc core with signature (n?,k),(k,m?)->(n?,m?) requires 1)

# print(A @ 10)
# ❌ 同样报错

# np.dot 允许标量 → 退化为逐元素乘法
# matmul / @ 禁止标量（必须 ≥ 1 维）


# 形状 (2, 3, 4) 的"矩阵堆栈"：2 个 3×4 矩阵
A = np.arange(24).reshape(2, 3, 4)
# 形状 (2, 4, 5)：2 个 4×5 矩阵
B = np.arange(40).reshape(2, 4, 5)
print(A)
print(B)

#而 matmul / @ 是真正意义的批量矩阵乘法：每一对 A[i] (3×4) 和 B[i] (4×5) 相乘，得到 (2, 3, 5)。
print(np.matmul(A, B).shape)   # (2, 3, 5)   ← 按矩阵堆栈处理
print((A @ B).shape)           # (2, 3, 5)   ← 同 matmul
print(np.dot(A, B).shape)      # (2, 3, 2, 5) ← 完全不同的结果！
# 为什么 dot 结果是 (2, 3, 2, 5)？
# np.dot(A, B) 的定义是：把 A 的最后一个轴（大小 4）与 B 的倒数第二个轴（大小 4）求积和。
# 剩下的轴 A.shape[:-1] = (2,3) 和 B.shape[:-2] + B.shape[-1:] = (2,) + (5,) = (2,5) 全部保留下来拼接：
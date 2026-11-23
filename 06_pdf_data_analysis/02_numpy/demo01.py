# 用代码演示三者差异

## 准备
import numpy as np

A = np.array([[1, 2],
              [3, 4]])
B = np.array([[5, 6],
              [7, 8]])

## 1. 二维矩阵：三者结果相同
print(np.dot(A, B))
print(np.matmul(A, B))
print(A @ B)

# 输出全部相同：
# [[19 22]
#  [43 50]]

# ✅ 二维情况下 `dot`、`matmul`、`@` **完全等价**。

## 2. 一维数组：`dot` 与 `matmul` 也相同
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print(np.dot(a, b))     # 32  （内积，标量）
print(np.matmul(a, b))  # 32
print(a @ b)            # 32
# 一维时都算内积 → **结果一样**。


## 3. ⭐ 标量乘法：关键区别来了

A = np.array([[1, 2], [3, 4]])
print(np.dot(A, 10))
# [[10 20]
#  [30 40]]        ✅ dot 允许标量，逐元素乘

# print(np.matmul(A, 10))
# ❌ ValueError: matmul: Input operand 1 does not have enough dimensions
#    (has 0, gufunc core with signature (n?,k),(k,m?)->(n?,m?) requires 1)

# print(A @ 10)
# ❌ 同样报错
# - `np.dot` 允许标量 → 退化为逐元素乘法
# - `matmul` / `@` **禁止标量**（必须 ≥ 1 维）


## 4. ⭐ 高维数组：最重要的区别
# 这是 `dot` 和 `matmul` 分道扬镳的地方。

# 形状 (2, 3, 4) 的"矩阵堆栈"：2 个 3×4 矩阵
A = np.arange(24).reshape(2, 3, 4)
# 形状 (2, 4, 5)：2 个 4×5 矩阵
B = np.arange(40).reshape(2, 4, 5)

# A[0](3×4) @ B[0](4×5)   =   C[0](3×5)   ← 第0摞配对
# A[1](3×4) @ B[1](4×5)   =   C[1](3×5)   ← 第1摞配对

print(np.matmul(A, B).shape)   # (2, 3, 5)   ← 按矩阵堆栈处理
print((A @ B).shape)           # (2, 3, 5)   ← 同 matmul
print(np.dot(A, B).shape)      # (2, 3, 2, 5) ← 完全不同的结果！

# **为什么 `dot` 结果是 `(2, 3, 2, 5)`？**
# `np.dot(A, B)` 的定义是：把 `A` 的**最后一个轴**（大小 4）与 `B` 的**倒数第二个轴**（大小 4）求积和。剩下的轴 `A.shape[:-1] = (2,3)` 和 `B.shape[:-2] + B.shape[-1:] = (2,) + (5,) = (2,5)` 全部保留下来拼接：

# (2, 3)  +  (2, 5)  =  (2, 3, 2, 5)
# 而 `matmul` / `@` 是**真正意义的批量矩阵乘法**：每一对 `A[i]` (3×4) 和 `B[i]` (4×5) 相乘，得到 (2, 3, 5)。


## 5. ⭐ 高维 + 广播：`matmul` 独有的能力
A = np.arange(24).reshape(2, 3, 4)   # (2, 3, 4)
B = np.arange(20).reshape(4, 5)      # (4, 5)


print((A @ B).shape)        # (2, 3, 5)  ✅ matmul 支持广播
print(np.dot(A, B).shape)   # (2, 3, 4, 5) ← dot 不做堆栈广播，结果完全不同

# `matmul` 会把 `B` 广播到 `(2, 4, 5)` 然后逐组相乘；`dot` 只是按轴求和，不按"矩阵堆栈"语义广播。


## 6. 特殊情况：两者可能又相同

# 如果 **第一个参数是 1 维**，`dot` 和 `matmul` 又一致了：

a = np.array([1, 2, 3])           # (3,)
B = np.arange(12).reshape(3, 4)   # (3, 4)

print(a @ B)              # shape (4,)  —— 向量与矩阵相乘
print(np.dot(a, B))       # shape (4,)  —— 同样 (4,)

# 因为一维时 `matmul` 会先把 `a` 提升为 (1,3)，算完再压回 (4,)，而 `dot` 正好等价于相同操作。


## 7. 汇总表

# 每次运行观察 shape 与是否报错
# cases = [
#     ("2D 矩阵乘",       lambda: np.dot(np.eye(2), np.eye(2)),      "相等"),
#     ("1D 内积",         lambda: np.dot(np.ones(3), np.ones(3)),    "相等"),
#     ("矩阵 × 标量",     lambda: np.dot(np.eye(2), 10),             "dot 可以，matmul 报错"),
#     ("高维堆栈 (2,3,4)x(2,4,5)", lambda: np.dot(np.zeros((2,3,4)), np.zeros((2,4,5))), "不同结果"),
#     ("高维 + 广播",     lambda: np.dot(np.zeros((2,3,4)), np.zeros((4,5))),           "不同结果"),
# ]
#
# | 场景 | `dot` | `matmul` / `@` |
# |------|-------|----------------|
# | 2D × 2D | 矩阵乘 ✅ | 矩阵乘 ✅ |
# | 1D × 1D | 内积 | 内积（相同） |
# | 矩阵 × 标量 | 逐元素乘 ✅ | **报错 ❌** |
# | 高维堆栈 | 按**单轴收缩**，shape 不同 | 按**矩阵堆栈** + 广播 ✅ |
# | 高维 × 2D | 不做堆栈广播，shape 不同 | 自动广播 ✅ |


## 一句话记忆

# 想写矩阵乘法 → 用 @ 或 np.matmul（语义清晰、支持广播、拒绝标量）
C = A @ B

# np.dot → 历史遗留的通用点积，行为随维度变，高维下容易踩坑
# 核心口诀：2D 以内三者一样；一旦涉及高维或标量，`dot` 和 `matmul` 就完全不同 —— 做矩阵运算请首选 `@`。**
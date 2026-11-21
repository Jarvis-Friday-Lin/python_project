"""参考答案：课件27题的变式操作自测"""
# 对应 PDF：11-numpy-full.pdf 第 63—66 页
# 课件核心：第63—66页原27题知识点顺序不变，改数据与提取位置，不是原题原样复制。
# 扩展：default_rng固定种子为扩展；题号仍与原27题操作对应。
# 案例数据（据此自行创建对象，不能照抄 examples 的数据）：
# | 符号 | 本次变式输入 |
# |---|---|
# | A | 长度12的零数组 |
# | B | 30到54，步长2，包含54 |
# | D | 10到21的整数，整理为3×4 |
# | E | [[2,4],[6,8],[10,12]] |
# | F | [5,0,2,0,0,9] |
# | G | 2×3×4随机小数，种子11 |
# | H | [2,8,4,10,6] |
# | I | [2,4]，追加[6,8] |
# | J与K | J=[2,4,6]，K=[1,2,3] |
# | L | 6个-3 |
# | M | [9,3,7,1] |
# | N | [[2,1],[1,1]] |
# | O | [[1,2,3],[4,5,6],[7,8,9]] |
# | P | 1到20依次整理为4×5 |
# 建议先做练习，再逐段对照下面的实现；assert 用于验证结果。

import numpy as np
# 1—7：创建、字节数、范围终点、反转、形状与非零位置。
A = np.zeros(12)
print('\n===== A =====')
print(A)
print('\n===== A.size * A.itemsize =====')
print(A.size * A.itemsize)
B = np.arange(30,55,2)
C = B[::-1]
D = np.arange(10,22).reshape(3,4)
E = np.array([[2,4],[6,8],[10,12]])
F = np.array([5,0,2,0,0,9])
print('\n===== B =====')
print(B)
print('\n===== C =====')
print(C)
print('\n===== D =====')
print(D)
print('\n===== E.shape =====')
print(E.shape)
print('\n===== F.nonzero() =====')
print(F.nonzero())
assert len(B) == 13 and B[-1] == 54 and C[0] == 54
assert D.shape == (3,4) and E.shape == (3,2)
assert F.nonzero()[0].tolist() == [0,2,5]
# 8—14：随机数值不固定预期列表，固定种子后检查范围、形状。
G = np.random.default_rng(11).random((2,3,4))
H = np.array([2,8,4,10,6])
print('\n===== G =====')
print(G)
print('\n===== (H.max(), H.min(), H.mean(), H.std(), np.median(H)) =====')
print((H.max(), H.min(), H.mean(), H.std(), np.median(H)))
print('\n===== D.T =====')
print(D.T)
assert G.shape == (2,3,4) and ((G >= 0) & (G < 1)).all()
assert (H.max(), H.min(), H.mean(), np.median(H)) == (10,2,6,6)
assert np.isclose(H.std(), np.sqrt(8))
# 15—19：append返回新数组；log是自然对数，不是以10为底。
I = np.array([2,4])
extended = np.append(I,[6,8])
J, K = np.array([2,4,6]), np.array([1,2,3])
L = np.full(6,-3)
print('\n===== extended =====')
print(extended)
print('\n===== (J + K, J - K, J * K, J / K) =====')
print((J+K, J-K, J*K, J/K))
print('\n===== np.sum(I) =====')
print(np.sum(I))
print('\n===== np.log(I) =====')
print(np.log(I))
print('\n===== L =====')
print(L)
assert I.tolist() == [2,4] and extended.tolist() == [2,4,6,8]
assert np.sum(I) == 6 and np.allclose(np.log(I), [np.log(2),np.log(4)])
assert np.array_equal(L,np.repeat(-3,6))
# 20—27：argsort返回位置；基本切片的起始位置从0计数。
M = np.array([9,3,7,1])
N = np.array([[2,1],[1,1]])
O = np.arange(1,10).reshape(3,3)
P = np.arange(1,21).reshape(4,5)
print('\n===== np.sort(M) =====')
print(np.sort(M))
print('\n===== (M.argmax(), M.argmin(), M.argsort()) =====')
print((M.argmax(),M.argmin(),M.argsort()))
print('\n===== np.linalg.inv(N) =====')
print(np.linalg.inv(N))
print('\n===== np.abs(-N) =====')
print(np.abs(-N))
print('\n===== O[:, 1] =====')
print(O[:,1])
print('\n===== P[1::2, ::2] =====')
print(P[1::2,::2])
assert M.argsort().tolist() == [3,1,2,0]
assert M.argmax() == 0 and M.argmin() == 3
assert np.allclose(N @ np.linalg.inv(N), np.eye(2))
assert O[:,1].tolist() == [2,5,8]
assert P[1::2,::2].tolist() == [[6,8,10],[16,18,20]]

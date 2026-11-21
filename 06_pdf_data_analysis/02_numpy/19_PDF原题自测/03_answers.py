"""参考答案：文档末尾27道操作题"""
# 对应 PDF：11-numpy-full.pdf 第 63—66 页
# 建议先完成 02_exercises.py；下面的实现与该题数据、要求一一对应。

import numpy as np
# 01：zeros的shape可以是整数，表示一维长度。
A=np.zeros(15)
print('\n===== A =====')
print(A)
assert A.shape==(15,) and np.all(A==0)
# 02：nbytes等于size*itemsize，只计算元素缓冲区。
print('\n===== A.nbytes =====')
print(A.nbytes)
assert A.nbytes==A.size*A.itemsize
# 03：arange右端不包含，所以写61。
B=np.arange(20,61)
print('\n===== B =====')
print(B)
assert B[0]==20 and B[-1]==60 and B.size==41
# 04：负步长从尾到头读取。
C=B[::-1]
print('\n===== C =====')
print(C)
assert C[0]==60 and C[-1]==20
# 05：reshape保持总元素数。
D=np.arange(16).reshape(4,4)
print('\n===== D =====')
print(D)
assert D.shape==(4,4) and D[-1,-1]==15
# 06：文档这里“dimensions”问的是形状，同时补充轴数避免歧义。
E=np.array([[3,4,5],[6,7,8]])
print('\n===== E.shape =====')
print(E.shape)
print('\n===== E.ndim =====')
print(E.ndim)
assert E.shape==(2,3) and E.ndim==2
# 07：nonzero返回每个轴的位置数组组成的元组，一维取[0]。
F=np.array([0,3,0,0,4,0])
print('\n===== F.nonzero() =====')
print(F.nonzero())
assert F.nonzero()[0].tolist()==[1,4]
# 08：新式Generator确保教学复现，不修改全局随机状态。
G=np.random.default_rng(42).random((3,3,3))
print('\n===== G =====')
print(G)
assert G.shape==(3,3,3) and np.all((G>=0)&(G<1))
H=np.array([1,13,0,56,71,22])
# 09、10：返回数值而非位置。
print('\n===== H.max() =====')
print(H.max())
print('\n===== H.min() =====')
print(H.min())
assert H.max()==71 and H.min()==0
# 11、12、13：均值、总体标准差、中位数。
print('\n===== H.mean() =====')
print(H.mean())
print('\n===== H.std(ddof=0) =====')
print(H.std(ddof=0))
print('\n===== np.median(H) =====')
print(np.median(H))
assert np.isclose(H.mean(),163/6) and np.median(H)==17.5
assert np.isclose(H.std(),np.sqrt(((H-H.mean())**2).mean()))
# 14：二维转置交换行列轴。
print('\n===== D.T =====')
print(D.T)
assert np.array_equal(D.T[0],D[:,0])
# 15：append生成新数组，不改变I。
I=np.array([1,2,3])
appended=np.append(I,[4,5,6])
print('\n===== appended =====')
print(appended)
assert I.tolist()==[1,2,3] and appended.tolist()==[1,2,3,4,5,6]
# 16：每个位置一对一操作，除法返回浮点。
J=np.array([1,2,3])
K=np.array([4,5,6])
print('\n===== J+K =====')
print(J+K)
print('\n===== J-K =====')
print(J-K)
print('\n===== J*K =====')
print(J*K)
print('\n===== J/K =====')
print(J/K)
assert (J+K).tolist()==[5,7,9] and (J-K).tolist()==[-3,-3,-3]
assert (J*K).tolist()==[4,10,18] and np.allclose(J/K,[.25,.4,.5])
# 17、18：明确使用原I，消除前题重绑定变量可能造成的歧义。
print('\n===== I.sum() =====')
print(I.sum())
print('\n===== np.log(I) =====')
print(np.log(I))
assert I.sum()==6 and np.isclose(np.log(I)[0],0)
# 19：原文no.full是笔误，正确命名是np.full。
L=np.full(5,8)
print('\n===== L =====')
print(L)
print('\n===== np.repeat(8,5) =====')
print(np.repeat(8,5))
assert np.array_equal(L,np.repeat(8,5))
# 20—23：排序值、最大位置、最小位置和排序索引分别处理。
M=np.array([2,5,7,3,6])
print('\n===== np.sort(M) =====')
print(np.sort(M))
print('\n===== M.argmax() =====')
print(M.argmax())
print('\n===== M.argmin() =====')
print(M.argmin())
print('\n===== M.argsort() =====')
print(M.argsort())
assert np.sort(M).tolist()==[2,3,5,6,7]
assert M.argmax()==2 and M.argmin()==0
assert M.argsort().tolist()==[0,3,1,4,2]
# 24：逆矩阵用乘回单位矩阵检查，浮点不用==逐项严格比。
N=np.array([[6,1,1],[4,-2,5],[2,8,7]])
inverse=np.linalg.inv(N)
print('\n===== inverse =====')
print(inverse)
assert np.allclose(N@inverse,np.eye(3))
# 25：abs逐元素转换，负2变成2。
print('\n===== np.abs(N) =====')
print(np.abs(N))
assert np.abs(N)[1,1]==2
# 26：第三列位置是2，返回一维数组。
O=np.array([[11,22,33],[44,55,66],[77,88,99]])
print('\n===== O[:,2] =====')
print(O[:,2])
assert O[:,2].tolist()==[33,66,99]
# 27：日常奇数行从位置0起步2；偶数列从位置1起步2。
P=np.arange(3,61,3).reshape(5,4)
print('\n===== P[::2,1::2] =====')
print(P[::2,1::2])
assert P[::2,1::2].tolist()==[[6,12],[30,36],[54,60]]

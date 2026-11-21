"""案例驱动示例：找相似样本并实测计算成本"""
# 对应 PDF：11-numpy-full.pdf 第 47—55 页
# 任务：计算两位学生到两个参考样本的欧氏距离。
# 两两比较会产生“学生×参考样本”的结果；从双循环推导到广播，观察中间数组成本。
# 案例数据：
# | 集合 | 样本 | 特征1 | 特征2 |
# |---|---|---:|---:|
# | X | A | 0 | 0 |
# | X | B | 3 | 4 |
# | Y | C | 0 | 4 |
# | Y | D | 3 | 0 |
# 先看整体路线：
# 第 1 步：用双循环得到可信的距离表。
# 第 2 步：增轴后广播相减，再平方求和开根号。
# 第 3 步：用重复计时和数据内存量比较，不把一次结果当定律。

import numpy as np
from timeit import repeat
from sys import getsizeof

x=np.array([[0.,0.],[3.,4.]])
y=np.array([[0.,4.],[3.,0.]])
manual=np.array([[sum((a-b)**2 for a,b in zip(row,ref))**.5 for ref in y] for row in x])
print('\n===== manual =====')
print(manual)
# (M,1,D)-(1,N,D) -> (M,N,D)，每一格最后一个轴存逐特征差。
diffs=x[:,None,:]-y[None,:,:]
distances=np.sqrt(np.sum(diffs**2,axis=2))
print('\n===== diffs.shape =====')
print(diffs.shape)
print('\n===== distances =====')
print(distances)
# reshape/expand_dims与newaxis都可构造相同的比较轴。
assert np.allclose(distances,manual)
assert np.allclose(distances,[[4,3],[3,4]])
assert np.array_equal(x.reshape(2,1,2)-y.reshape(1,2,2),diffs)
assert np.array_equal(np.expand_dims(x,1)-np.expand_dims(y,0),diffs)

values=list(range(10000))
array=np.arange(10000)
# repeat执行3组，每组number=20次；以每组最快总时长作本机参考。
list_time=min(repeat(lambda:[v+1 for v in values],repeat=3,number=20))
array_time=min(repeat(lambda:array+1,repeat=3,number=20))
print('\n===== {"列表秒":list_time,"数组秒":array_time} =====')
print({"列表秒":list_time,"数组秒":array_time})
print('\n===== {"数组数据字节":array.nbytes,"列表浅大小":getsizeof(values), "列表加各元素估计":getsizeof(values)+sum(getsizeof(v) for v in values)} =====')
print({"数组数据字节":array.nbytes,"列表浅大小":getsizeof(values),
       "列表加各元素估计":getsizeof(values)+sum(getsizeof(v) for v in values)})
# nbytes只含元素缓冲区；列表浅大小不含整数对象。两者不能不说明口径就直接比较。
# 距离广播会建立M*N*D的中间差数组，大样本需分块，并非零内存成本。

# 学完先自己回答，再看下面的参考答案：
# 1. 这个知识点解决什么类型的问题？
# 2. 为什么当前案例需要它？
# 3. 每一步代码为什么要在此时出现？
# 4. 如果换一种做法，代价和风险是什么？

# 参考答案：
# 1. 样本两两距离和有口径的性能比较。
# 2. 每名学生都要对每个参考样本比较，不能只配对同位置行。
# 3. 循环确定答案，增轴构造比较维度，再沿特征轴求和，最后实测成本。
# 4. 循环更省中间内存但Python开销大；广播简洁而M*N*D中间结果可能很大。

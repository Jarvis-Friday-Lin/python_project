"""参考答案：找相似样本并实测计算成本"""
# 对应 PDF：11-numpy-full.pdf 第 47—55 页
# 建议先完成 02_exercises.py；下面的实现与该题数据、要求一一对应。

import numpy as np
from timeit import repeat
x=np.array([[0.,0.],[3.,4.]])
y=np.array([[0.,4.],[3.,0.]])
a=np.sqrt(((x[:,None,:]-y[None,:,:])**2).sum(axis=2))
b=np.sqrt(((x.reshape(2,1,2)-y.reshape(1,2,2))**2).sum(axis=2))
c=np.sqrt(((np.expand_dims(x,1)-np.expand_dims(y,0))**2).sum(axis=2))
assert np.allclose(a,[[4,3],[3,4]]) and np.allclose(a,b) and np.allclose(a,c)
x=np.vstack([x,[0,4]])
extended=np.sqrt(((x[:,None,:]-y[None,:,:])**2).sum(axis=2))
print('\n===== extended =====')
print(extended)
assert extended.shape==(3,2) and np.allclose(extended[2],[0,5])
values=list(range(10000))
arr=np.arange(10000)
print('\n===== min(repeat(lambda:[v+1 for v in values],number=20,repeat=3)) =====')
print(min(repeat(lambda:[v+1 for v in values],number=20,repeat=3)))
print('\n===== min(repeat(lambda:arr+1,number=20,repeat=3)) =====')
print(min(repeat(lambda:arr+1,number=20,repeat=3)))

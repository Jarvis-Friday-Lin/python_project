"""参考答案：计算配送站到客户的距离"""
# 对应 PDF：11-numpy-full.pdf 第 47—55 页
# 课件核心：第47—55页：成对欧氏距离、广播、计算效率。
# 扩展：perf_counter计时、argmin沿轴选最近点是扩展；不保证NumPy固定快多少倍。
# 案例数据（据此自行创建对象，不能照抄 examples 的数据）：
# | 类型 | 名称 | x | y |
# |---|---|---|---|
# | 站点 | S1 | 0 | 0 |
# | 站点 | S2 | 6 | 0 |
# | 客户 | C1 | 0 | 8 |
# | 客户 | C2 | 6 | 8 |
# | 客户 | C3 | 3 | 4 |
# 建议先做练习，再逐段对照下面的实现；assert 用于验证结果。

import numpy as np
from time import perf_counter
stations = np.array([[0,0],[6,0]])
clients = np.array([[0,8],[6,8],[3,4]])
diff1 = stations.reshape(2,1,2) - clients.reshape(1,3,2)
diff2 = stations[:,None,:] - clients[None,:,:]
diff3 = np.expand_dims(stations,1) - np.expand_dims(clients,0)
distances = np.sqrt((diff1**2).sum(axis=2))
print('\n===== distances =====')
print(distances)
assert np.allclose(distances, [[8,10,5],[10,8,5]])
assert np.array_equal(diff1,diff2) and np.array_equal(diff1,diff3)
# 扩展：对每一行在客户轴找最小值的位置，0起始的2表示C3。
assert distances.argmin(axis=1).tolist() == [2,2]
values = list(range(10000))
array = np.array(values)
start = perf_counter()
manual = [v*v for v in values]
python_time = perf_counter() - start
start = perf_counter()
batch = array * array
numpy_time = perf_counter() - start
assert np.array_equal(manual,batch)
print('\n===== (python_time, numpy_time) =====')
print((python_time,numpy_time))
# 单次计时含噪声，不能据此断言所有计算任务都快相同倍数。

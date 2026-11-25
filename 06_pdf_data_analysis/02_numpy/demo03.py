import numpy as np


a = np.array(range(24))
print(a)


b = np.array(16)
print(b)


c = np.reshape(a, (2, 2, 6))
d = np.reshape(c, (24,)) # 一维
d = np.reshape(c, [24,]) # 一维
d = np.reshape(c, 24,) # 一维
d = np.reshape(c, -1)
print(d)

d = np.reshape(c, (24,1))
# print(d)

d = np.reshape(c, (1,24)) # 二维
print(d)

d = np.reshape(c, (24)) # 一维
d = np.reshape(c, 24) # 一维
print(d)



arr = np.array([0, 1, 2, 3, 4, 5])

print(arr.reshape(2, 3, order='C'))

print("=" * 20)

print(arr.reshape(2, 3, order='F'))

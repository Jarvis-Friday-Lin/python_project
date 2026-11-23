import numpy as np
a: np.ndarray = np.array([[7, 8], [9, 10], [11, 12]])
# print(a[[0, 1, 2], [1, 0, 1]]) # Output: [ 8 9 12]
a[[0, 1, 2], [1, 0, 1]] = [1, 2, 3]


a[0, 1] = 1


import numpy as np
print(np.arange(5))          # [0 1 2 3 4]
print(np.arange(1,6))        # [1 2 3 4 5]
print(np.arange(1,10,2))     # [1 3 5 7 9]
print(np.arange(0, 1, 0.2))  # [0. 0.2 0.4 0.6 0.8]  ✅ 支持小数，range不行


import numpy as np
a = np.array([[10,20],[30,40]])
print(a.shape)        # (2,2)
print(np.shape(a))    # (2,2)


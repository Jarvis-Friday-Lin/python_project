import numpy as np
A = np.arange(24).reshape(2, 3, 4)   # (2, 3, 4)
B = np.arange(20).reshape(4, 5)      # (4, 5)


print((A @ B))        # (2, 3, 5)  ✅ matmul 支持广播
# print(np.dot(A, B))   # (2, 3, 4, 5) ← dot 不做堆栈广播，结果完全不同
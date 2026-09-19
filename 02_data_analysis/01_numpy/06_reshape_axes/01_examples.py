"""可运行示例：先预测结果，再执行。"""

import numpy as np
matrix = np.arange(12).reshape(3, 4)
print(matrix.T)
print(matrix.sum(axis=0))
print(matrix.sum(axis=1))
print(matrix.ravel())

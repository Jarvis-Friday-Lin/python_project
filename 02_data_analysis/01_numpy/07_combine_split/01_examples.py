"""可运行示例：先预测结果，再执行。"""

import numpy as np
left = np.array([[1], [2]])
right = np.array([[3], [4]])
matrix = np.concatenate([left, right], axis=1)
print(matrix)
print(np.array_split(matrix, 2, axis=0))

"""可运行示例：先预测结果，再执行。"""

import numpy as np
matrix = np.array([[1, 2, 3], [4, 5, 6]])
column_offsets = np.array([[10], [20]])
print(matrix * 2)
print(matrix + column_offsets)

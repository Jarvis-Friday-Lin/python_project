"""可运行示例：先预测结果，再执行。"""

import numpy as np
matrix = np.arange(12).reshape(3, 4)
view = matrix[:2, 1:3]
print(matrix, view, sep="\n")
copied = view.copy()
copied[0, 0] = 999
print(matrix)

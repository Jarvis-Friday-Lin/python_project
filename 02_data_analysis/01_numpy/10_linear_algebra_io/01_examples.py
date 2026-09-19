"""可运行示例：先预测结果，再执行。"""

import numpy as np
a = np.array([[2.0, 1.0], [1.0, 3.0]])
b = np.array([5.0, 6.0])
solution = np.linalg.solve(a, b)
print(solution)
print(a @ solution)

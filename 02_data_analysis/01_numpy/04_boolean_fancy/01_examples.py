"""可运行示例：先预测结果，再执行。"""

import numpy as np
values = np.array([12, 5, 18, 3, 20])
print(values[values >= 10])
print(values[(values >= 10) & (values < 20)])
print(values[[0, 3, 4]])

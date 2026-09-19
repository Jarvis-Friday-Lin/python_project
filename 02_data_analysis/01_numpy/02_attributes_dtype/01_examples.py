"""可运行示例：先预测结果，再执行。"""

import numpy as np
values = np.array([[1, 2], [3, 4]], dtype=np.float64)
print(values.ndim, values.shape, values.size, values.dtype, values.itemsize)
print(values.astype(np.int32))

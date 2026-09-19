"""可运行示例：先预测结果，再执行。"""

import numpy as np
rng = np.random.default_rng(42)
print(rng.integers(1, 7, size=10))
print(rng.normal(loc=100, scale=15, size=5))
print(rng.choice(["A", "B", "C"], size=4, replace=True))

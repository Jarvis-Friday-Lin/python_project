"""可运行示例：先预测结果，再执行。"""

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
rng = np.random.default_rng(42)
values = rng.normal(100, 15, 500)
sns.histplot(values, bins=20, kde=True)
plt.show()

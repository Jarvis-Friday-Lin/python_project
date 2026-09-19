"""可运行示例：先预测结果，再执行。"""

import matplotlib.pyplot as plt
fig, axes = plt.subplots(1, 2, figsize=(9, 3))
axes[0].plot([1, 2, 3], [2, 4, 3])
axes[1].bar(["A", "B"], [5, 8])
fig.tight_layout()
plt.show()

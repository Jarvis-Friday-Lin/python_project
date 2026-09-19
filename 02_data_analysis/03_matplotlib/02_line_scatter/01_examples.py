"""可运行示例：先预测结果，再执行。"""

import matplotlib.pyplot as plt
x = [1, 2, 3, 4]
y = [2, 5, 4, 8]
fig, axes = plt.subplots(1, 2)
axes[0].plot(x, y, marker="o")
axes[1].scatter(x, y, s=60, alpha=0.7)
plt.show()

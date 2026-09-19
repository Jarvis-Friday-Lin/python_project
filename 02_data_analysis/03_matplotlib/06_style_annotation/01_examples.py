"""可运行示例：先预测结果，再执行。"""

import matplotlib.pyplot as plt
x, y = [1, 2, 3, 4], [10, 14, 13, 20]
plt.plot(x, y, color="#2f6f9f", linewidth=2)
plt.annotate("峰值", xy=(4, 20), xytext=(3.2, 18), arrowprops={"arrowstyle": "->"})
plt.show()

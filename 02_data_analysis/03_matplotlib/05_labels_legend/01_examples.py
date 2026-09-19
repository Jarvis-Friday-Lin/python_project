"""可运行示例：先预测结果，再执行。"""

import matplotlib.pyplot as plt
plt.plot([1, 2, 3], [100, 130, 125], label="销售额", marker="o")
plt.title("第一季度销售趋势")
plt.xlabel("月份")
plt.ylabel("销售额（万元）")
plt.grid(alpha=0.3)
plt.legend()
plt.show()

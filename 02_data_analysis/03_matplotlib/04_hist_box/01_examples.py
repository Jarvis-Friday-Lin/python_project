"""可运行示例：先预测结果，再执行。"""

import matplotlib.pyplot as plt
values = [55, 62, 68, 70, 72, 75, 80, 82, 90, 100]
fig, axes = plt.subplots(1, 2)
axes[0].hist(values, bins=5, edgecolor="black")
axes[1].boxplot(values)
plt.show()

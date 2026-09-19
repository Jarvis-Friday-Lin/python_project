"""可运行示例：先预测结果，再执行。"""

import matplotlib.pyplot as plt
import seaborn as sns
sns.set_theme(style="whitegrid", palette="deep")
sns.lineplot(x=[1, 2, 3], y=[2, 5, 4], marker="o")
plt.show()

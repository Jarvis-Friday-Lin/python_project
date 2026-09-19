"""可运行示例：先预测结果，再执行。"""

import matplotlib.pyplot as plt
plt.rcParams["font.sans-serif"] = ["Arial Unicode MS", "SimHei", "DejaVu Sans"]
plt.rcParams["axes.unicode_minus"] = False
plt.plot([1, 2, 3], [-1, 2, 3])
plt.title("中文标题与负数")
plt.show()

"""可运行示例：先预测结果，再执行。"""

import matplotlib.pyplot as plt
categories = ["A", "B", "C"]
online = [10, 15, 12]
offline = [5, 6, 8]
plt.bar(categories, online, label="线上")
plt.bar(categories, offline, bottom=online, label="线下")
plt.legend()
plt.show()

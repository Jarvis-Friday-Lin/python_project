"""可运行示例：先预测结果，再执行。"""

from datetime import datetime
import matplotlib.pyplot as plt
dates = [datetime(2026, m, 1) for m in range(1, 5)]
fig, ax = plt.subplots()
ax.plot(dates, [10, 15, 13, 20], marker="o")
fig.autofmt_xdate()
fig.savefig("matplotlib_example.png", dpi=150, bbox_inches="tight")
print("已保存 matplotlib_example.png")

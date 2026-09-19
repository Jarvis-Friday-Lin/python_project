"""可运行示例：先预测结果，再执行。"""

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
tips = pd.DataFrame({
    "total_bill": [80, 120, 160, 200, 240, 280],
    "tip": [8, 14, 18, 25, 24, 35],
    "time": ["午餐", "午餐", "晚餐", "晚餐", "晚餐", "午餐"],
    "smoker": ["否", "是", "否", "是", "否", "是"],
})
sns.relplot(data=tips, x="total_bill", y="tip", col="time", hue="smoker")
plt.show()

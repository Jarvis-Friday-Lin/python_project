"""可运行示例：先预测结果，再执行。"""

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
tips = pd.DataFrame({
    "total_bill": [80, 120, 160, 200, 240, 280],
    "tip": [8, 14, 18, 25, 24, 35],
    "time": ["Lunch", "Lunch", "Dinner", "Dinner", "Dinner", "Lunch"],
    "sex": ["女", "男", "女", "男", "女", "男"],
})
sns.scatterplot(data=tips, x="total_bill", y="tip", hue="time", style="sex", alpha=0.75)
plt.show()

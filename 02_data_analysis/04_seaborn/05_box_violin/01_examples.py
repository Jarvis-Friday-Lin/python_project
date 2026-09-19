"""可运行示例：先预测结果，再执行。"""

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
tips = pd.DataFrame({
    "day": ["周一", "周一", "周二", "周二", "周三", "周三"],
    "total_bill": [80, 150, 90, 210, 120, 260],
})
sns.violinplot(data=tips, x="day", y="total_bill", inner="quartile")
plt.show()

"""可运行示例：先预测结果，再执行。"""

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
data = pd.DataFrame({"city": ["上海", "北京", "上海", "深圳"], "amount": [100, 200, 300, 180]})
sns.barplot(data=data, x="city", y="amount", errorbar=None)
plt.show()

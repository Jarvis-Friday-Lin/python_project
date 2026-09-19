"""可运行示例：先预测结果，再执行。"""

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
data = pd.DataFrame({"price": [10, 12, 20, 22], "quantity": [8, 7, 4, 3], "amount": [80, 84, 80, 66]})
sns.heatmap(data.corr(numeric_only=True), annot=True, cmap="coolwarm", center=0)
plt.show()

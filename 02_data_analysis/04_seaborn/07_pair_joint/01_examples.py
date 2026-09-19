"""可运行示例：先预测结果，再执行。"""

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
iris = pd.DataFrame({
    "sepal_length": [5.1, 4.9, 6.2, 5.9, 6.5, 6.3],
    "sepal_width": [3.5, 3.0, 3.4, 3.0, 3.0, 2.5],
    "petal_length": [1.4, 1.4, 5.4, 5.1, 5.8, 5.0],
    "species": ["setosa", "setosa", "virginica", "virginica", "virginica", "virginica"],
})
sns.pairplot(iris, hue="species", corner=True)
plt.show()

"""可运行示例：先预测结果，再执行。"""

import numpy as np
values = np.array([10.0, np.nan, 30.0, 40.0])
print(np.isnan(values))
print(np.nanmean(values), np.nanmedian(values), np.nanstd(values))
print(np.nanpercentile(values, [25, 50, 75]))

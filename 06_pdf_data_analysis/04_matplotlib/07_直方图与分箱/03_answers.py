"""参考答案：同一批成绩为什么能画出不同分布"""
# 对应 PDF：14-matplotlib-full.pdf 第 18—19 页
# 建议先完成 02_exercises.py；下面的实现与该题数据、要求一一对应。

import numpy as np
import matplotlib.pyplot as plt
scores=np.array([50,60,65,70,75,80,85,90,95,100])
fig,axes=plt.subplots(1,2)
counts,edges,_=axes[0].hist(scores,bins=[50,70,90,101],edgecolor="black")
density,bounds,_=axes[1].hist(scores,bins=5,density=True,edgecolor="black")
print('\n===== counts =====')
print(counts)
assert counts.tolist()==[3,4,3] and counts.sum()==10
assert np.isclose((density*np.diff(bounds)).sum(),1)
# 箱太少掩盖结构，箱太多使随机波动显眼，应结合样本量与业务区间。
plt.show()

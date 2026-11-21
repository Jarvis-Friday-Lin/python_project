"""参考答案：均值相近的班级也可能很不同"""
# 对应 PDF：14-matplotlib-full.pdf 第 18、20 页
# 建议先完成 02_exercises.py；下面的实现与该题数据、要求一一对应。

import numpy as np
import matplotlib.pyplot as plt
a=[60,65,70,75,80]
b=[60,65,70,75,100]
q1,median,q3=np.percentile(b,[25,50,75])
fig,ax=plt.subplots()
artists=ax.boxplot([a,b],patch_artist=True,medianprops={"color":"red"})
ax.set_xticks([1,2],labels=["Class A","Class B"])
assert (q1,median,q3)==(65,70,75)
assert q3+1.5*(q3-q1)==90
assert list(artists["fliers"][1].get_ydata())==[100]
assert np.subtract(*np.percentile([70,70,70],[75,25]))==0
plt.show()

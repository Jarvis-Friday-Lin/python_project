"""参考答案：学习时长和成绩有没有关系"""
# 对应 PDF：14-matplotlib-full.pdf 第 14 页
# 建议先完成 02_exercises.py；下面的实现与该题数据、要求一一对应。

import numpy as np
import matplotlib.pyplot as plt
fig,ax=plt.subplots()
attendance=np.array([.6,.8,.9,1.])
points=ax.scatter([1,2,3,4],[60,75,80,90],c=attendance,s=attendance*200,cmap="viridis")
fig.colorbar(points,ax=ax,label="Attendance rate")
ax.set(xlabel="Study hours",ylabel="Score",title="Study and attendance")
assert points.get_offsets().shape==(4,2)
assert np.allclose(points.get_array(),attendance)
# 样本少，有其他影响因素，观察到的相关不能直接认定为因果。
plt.show()


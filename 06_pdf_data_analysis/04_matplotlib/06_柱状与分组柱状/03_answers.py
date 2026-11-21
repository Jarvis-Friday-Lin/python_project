"""参考答案：比较城市实际销售额和目标"""
# 对应 PDF：14-matplotlib-full.pdf 第 15—16 页
# 建议先完成 02_exercises.py；下面的实现与该题数据、要求一一对应。

import numpy as np
import matplotlib.pyplot as plt
x=np.arange(3)
actual=np.array([100,200,150])
target=np.array([120,180,160])
fig,axes=plt.subplots(1,2,figsize=(10,4))
axes[0].bar(x-.18,actual,width=.36,label="Actual")
axes[0].bar(x+.18,target,width=.36,label="Target")
axes[0].set_xticks(x,labels=["Shanghai","Beijing","Shenzhen"])
axes[0].legend()
axes[1].barh(["Shanghai","Beijing","Shenzhen"],actual)
assert len(axes[0].patches)==6
assert (actual-target).tolist()==[-20,20,-10]
fig.tight_layout()
plt.show()

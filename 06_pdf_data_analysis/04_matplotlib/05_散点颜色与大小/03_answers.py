"""参考答案：观察车速、耗油量和载重"""
# 对应 PDF：14-matplotlib-full.pdf 第14、23—24页；后两页参考色条
# 课件核心：第14页：scatter的x/y、c、cmap、s；色条参照第23—24页。
# 扩展：Collection对象检查是扩展；不能从观察性散点推断因果。
# 案例数据（据此自行创建对象，不能照抄 examples 的数据）：
# | trip | speed_kmh | fuel_l | load_kg |
# |---|---|---|---|
# | A | 30 | 4.2 | 100 |
# | B | 45 | 4.8 | 200 |
# | C | 60 | 5.6 | 150 |
# | D | 75 | 6.8 | 300 |
# | E | 90 | 8.1 | 250 |
# 建议先做练习，再逐段对照下面的实现；assert 用于验证结果。

import numpy as np
import matplotlib.pyplot as plt
speed, fuel = [30,45,60,75,90], [4.2,4.8,5.6,6.8,8.1]
load = np.array([100,200,150,300,250])
fig, ax = plt.subplots()
# c接收每点的颜色数值，s接收每点面积（平方点），不是直径。
points = ax.scatter(speed,fuel,c=load,cmap='viridis',s=load*0.8)
fig.colorbar(points,ax=ax,label='Load (kg)')
ax.set_xlabel('Speed (km/h)')
ax.set_ylabel('Fuel (L)')
assert points.get_offsets().shape == (5,2)
assert np.allclose(points.get_offsets()[:,0],speed)
assert np.allclose(points.get_offsets()[:,1],fuel)
assert np.array_equal(points.get_array(),load)
assert np.allclose(points.get_sizes(),load*0.8)
# 此样本速度高时油耗也高；不能排除载重、路况等因素，因此不能认定提速必然增加多少油耗。
plt.show()
plt.close(fig)

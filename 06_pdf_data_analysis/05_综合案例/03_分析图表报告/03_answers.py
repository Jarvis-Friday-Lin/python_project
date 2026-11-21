"""参考答案：综合迁移：制作机房用电六图报告"""
# 对应 PDF：11-numpy-full.pdf 第15页；13-pandas-full.pdf 第31—33、45—46页；14-matplotlib-full.pdf 第8—21、25页
# 课件核心：NumPy第15页逐元素算术；Pandas第31—33、45—46页聚合；Matplotlib第8—21、25页多图与保存。
# 扩展：数据一致性校验、对象断言和输出路径为综合扩展；每台设备功率固定2kW是假设。
# 案例数据（据此自行创建对象，不能照抄 examples 的数据）：
# | day | room | devices | hours | energy_kwh |
# |---|---|---|---|---|
# | 1 | A | 2 | 3 | 12 |
# | 1 | B | 3 | 2 | 12 |
# | 2 | A | 2 | 4 | 16 |
# | 2 | B | 3 | 3 | 18 |
# | 3 | A | 2 | 5 | 20 |
# | 3 | B | 3 | 4 | 24 |
# | 4 | A | 2 | 3 | 12 |
# | 4 | B | 3 | 3 | 18 |
# 建议先做练习，再逐段对照下面的实现；assert 用于验证结果。

from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
df = pd.DataFrame({'day':[1,1,2,2,3,3,4,4],'room':['A','B']*4,
                   'devices':[2,3]*4,'hours':[3,2,4,3,5,4,3,3],
                   'energy_kwh':[12,12,16,18,20,24,12,18]})
assert np.allclose(df['devices']*df['hours']*2,df['energy_kwh'])
daily, rooms = df.groupby('day')['energy_kwh'].sum(),df.groupby('room')['energy_kwh'].sum()
fig, axes = plt.subplots(2,3,figsize=(14,8))
axes[0,0].plot(daily.index,daily,marker='o')
axes[0,0].set_title('Daily energy')
axes[0,0].set_xlabel('Day')
axes[0,0].set_ylabel('kWh')
axes[0,1].bar(rooms.index,rooms)
axes[0,1].set_title('Room total')
axes[0,1].set_ylabel('kWh')
points = axes[0,2].scatter(df['hours'],df['energy_kwh'],c=df['devices'],cmap='viridis')
fig.colorbar(points,ax=axes[0,2],label='Devices')
axes[0,2].set_xlabel('Operating hours')
axes[0,2].set_ylabel('kWh')
counts,_,_ = axes[1,0].hist(df['energy_kwh'],bins=[10,15,20,25])
axes[1,0].set_xlabel('kWh per record')
axes[1,0].set_ylabel('Records')
axes[1,1].boxplot([df.loc[df['room'] == name,'energy_kwh'] for name in rooms.index])
axes[1,1].set_xticks([1,2],labels=rooms.index)
axes[1,1].set_ylabel('kWh per record')
axes[1,2].plot(daily.index,daily,label='Actual')
axes[1,2].plot(daily.index,[30]*len(daily),label='Reference')
axes[1,2].fill_between(daily.index,daily,30,alpha=0.3)
axes[1,2].set_xlabel('Day')
axes[1,2].set_ylabel('kWh')
axes[1,2].legend()
assert daily.tolist() == [24,34,44,30] and rooms.to_dict() == {'A':60,'B':72}
assert daily.sum() == rooms.sum() == 132 and counts.tolist() == [3,3,2]
assert list(axes[0,0].lines[0].get_ydata()) == daily.tolist()
fig.tight_layout()
out = Path(__file__).resolve().parent / 'outputs'
out.mkdir(exist_ok=True)
for suffix in ['png','pdf']:
    path = out/f'energy_dashboard.{suffix}'
    fig.savefig(path,dpi=160,bbox_inches='tight')
    assert path.stat().st_size > 0
print("\n===== '4天用电132kWh，房间B为72，比A多12kWh。' =====")
print('4天用电132kWh，房间B为72，比A多12kWh。')
print("\n===== '第3天44kWh最高，比30kWh参考线高14；4天模拟数据不能预测未来。' =====")
print('第3天44kWh最高，比30kWh参考线高14；4天模拟数据不能预测未来。')
plt.show()
plt.close(fig)

"""参考答案：按用电量批量计算电费"""
# 对应 PDF：13-pandas-full.pdf 第 28 页
# 课件核心：第28页：整列与标量、整列之间的逐元素算术。
# 扩展：where用于避免0作分母是扩展；不用apply。
# 案例数据（据此自行创建对象，不能照抄 examples 的数据）：
# | room | kwh | price_per_kwh | service_fee |
# |---|---|---|---|
# | R1 | 50 | 0.6 | 5 |
# | R2 | 80 | 0.7 | 5 |
# | R3 | 0 | 0.6 | 0 |
# 建议先做练习，再逐段对照下面的实现；assert 用于验证结果。

import pandas as pd
import numpy as np
df = pd.DataFrame({'room':['R1','R2','R3'],'kwh':[50,80,0],
                   'price_per_kwh':[0.6,0.7,0.6],'service_fee':[5,5,0]})
df['energy_charge'] = df['kwh'] * df['price_per_kwh']
df['total'] = df['energy_charge'] + df['service_fee']
df['discount_total'] = df['energy_charge'] * 0.9 + df['service_fee']
df['saved'] = df['total'] - df['discount_total']
# 扩展：where(condition)保留满足条件的值，其余替换为缺失，排除零分母。
df['average_unit_cost'] = df['total'] / df['kwh'].where(df['kwh'] != 0)
print('\n===== df.to_markdown(index=False) =====')
print(df.to_markdown(index=False))
assert np.allclose(df['total'],[35,61,0])
assert np.allclose(df['saved'],[3,5.6,0])
assert pd.isna(df.loc[2,'average_unit_cost']) and df.loc[0,'average_unit_cost'] == 0.7

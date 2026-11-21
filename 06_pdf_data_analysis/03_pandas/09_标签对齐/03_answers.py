"""参考答案：对齐两班次不同设备的产量"""
# 对应 PDF：13-pandas-full.pdf 第 14、29—30 页
# 课件核心：第14、29—30页：Series/DataFrame按标签对齐后运算，未匹配位置缺失。
# 扩展：add(fill_value=0)为扩展；仅在确认缺记录表示未生产时补零。
# 案例数据（据此自行创建对象，不能照抄 examples 的数据）：
# | 班次 | device | units |
# |---|---|---|
# | morning | M2 | 30 |
# | morning | M1 | 20 |
# | evening | M3 | 15 |
# | evening | M2 | 25 |
# 建议先做练习，再逐段对照下面的实现；assert 用于验证结果。

import pandas as pd
morning = pd.Series([30,20],index=['M2','M1'])
evening = pd.Series([15,25],index=['M3','M2'])
default = morning + evening
print('\n===== default =====')
print(default)
assert default.loc['M2'] == 55
assert pd.isna(default.loc['M1']) and pd.isna(default.loc['M3'])
assert default.equals(morning + evening.iloc[::-1])
# 扩展：fill_value只补参与加法的一侧缺值，不说明业务上所有缺失都应填0。
daily = morning.add(evening,fill_value=0)
print('\n===== daily =====')
print(daily)
assert daily.to_dict() == {'M1':20,'M2':55,'M3':15}
assert daily.sum() == 90

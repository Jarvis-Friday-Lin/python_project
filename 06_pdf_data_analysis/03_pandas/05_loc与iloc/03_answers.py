"""参考答案：用会员编号与位置提取积分"""
# 对应 PDF：13-pandas-full.pdf 第 6、9、20—22、38—40 页
# 课件核心：第6、9、20—22、38—40页：loc/iloc单行、切片、列表选行列。
# 扩展：at/iat为单标量读取的扩展。
# 案例数据（据此自行创建对象，不能照抄 examples 的数据）：
# | member_id | tier | points |
# |---|---|---|
# | M30 | silver | 120 |
# | M10 | gold | 360 |
# | M40 | basic | 80 |
# | M20 | gold | 240 |
# 建议先做练习，再逐段对照下面的实现；assert 用于验证结果。

import pandas as pd
df = pd.DataFrame({'tier':['silver','gold','basic','gold'],'points':[120,360,80,240]},
                  index=['M30','M10','M40','M20'])
print("\n===== df.loc[['M20', 'M30'], ['points']].to_markdown() =====")
print(df.loc[['M20','M30'],['points']].to_markdown())
assert df.loc['M10','points'] == df.iloc[1,1] == 360
assert df.loc[['M20','M30'],['points']].shape == (2,1)
assert df.loc[['M20','M30'],'points'].tolist() == [240,120]
assert isinstance(df.loc['M10'],pd.Series) and df.loc[['M10']].shape == (1,2)
# 扩展：at[行标签,列标签]和iat[行位置,列位置]都只获取一个标量。
assert df.at['M10','points'] == df.iat[1,1] == 360
assert df.loc['M30':'M40'].equals(df.iloc[0:3])

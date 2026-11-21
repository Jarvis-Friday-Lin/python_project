"""参考答案：筛查图书采购候选清单"""
# 对应 PDF：13-pandas-full.pdf 第 10、23、39—40 页
# 课件核心：第10、23、39—40页：比较条件、&、|、~和指定输出列。
# 扩展：isin/between是扩展便捷方法，可用比较与逻辑运算代替。
# 案例数据（据此自行创建对象，不能照抄 examples 的数据）：
# | book | subject | price | copies |
# |---|---|---|---|
# | B1 | science | 45 | 2 |
# | B2 | history | 70 | 1 |
# | B3 | science | 80 | 0 |
# | B4 | art | 35 | 4 |
# | B5 | history | 60 | 0 |
# 建议先做练习，再逐段对照下面的实现；assert 用于验证结果。

import pandas as pd
df = pd.DataFrame({'book':['B1','B2','B3','B4','B5'],
                   'subject':['science','history','science','art','history'],
                   'price':[45,70,80,35,60],'copies':[2,1,0,4,0]})
science = df.loc[(df['subject'] == 'science') & (df['price'] <= 60)]
missing = df.loc[((df['subject'] == 'science') | (df['subject'] == 'history')) & (df['copies'] == 0), ['book','price']]
other = df.loc[~(df['subject'] == 'science')]
range_rows = df.loc[(df['price'] >= 40) & (df['price'] <= 70)]
print('\n===== science.to_markdown(index=False) =====')
print(science.to_markdown(index=False))
print('\n===== missing.to_markdown(index=False) =====')
print(missing.to_markdown(index=False))
print('\n===== other.to_markdown(index=False) =====')
print(other.to_markdown(index=False))
print('\n===== range_rows.to_markdown(index=False) =====')
print(range_rows.to_markdown(index=False))
assert science['book'].tolist() == ['B1'] and missing['book'].tolist() == ['B3','B5']
assert other['book'].tolist() == ['B2','B4','B5']
# 扩展：isin(values)判断是否属于集合；between(left,right)默认两端包含。
shortcut = df.loc[df['subject'].isin(['science','history']) & (df['copies'] == 0), ['book','price']]
assert missing.equals(shortcut)
assert range_rows.equals(df.loc[df['price'].between(40,70)])
assert range_rows['book'].tolist() == ['B1','B2','B5']
assert df.loc[df['price'] < 10,['book','price']].shape == (0,2)

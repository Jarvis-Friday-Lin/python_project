"""参考答案：从不同来源拼出展馆客流表"""
# 对应 PDF：13-pandas-full.pdf 第 13—17 页
# 课件核心：第13—17页：字典列表、列字典、二维数组、Series按索引建表。
# 扩展：DataFrame.equals用于验证等价，属检查补充。
# 案例数据（据此自行创建对象，不能照抄 examples 的数据）：
# | hall | visitors | capacity |
# |---|---|---|
# | H1 | 120 | 150 |
# | H2 | 85 | 100 |
# | H3 | 60 | 80 |
# | tickets补充 | H1=110，H3=55 | H2未提供 |
# 建议先做练习，再逐段对照下面的实现；assert 用于验证结果。

import pandas as pd
rows = [{'hall':'H1','visitors':120,'capacity':150},
        {'hall':'H2','visitors':85,'capacity':100},{'hall':'H3','visitors':60,'capacity':80}]
by_rows = pd.DataFrame(rows)
by_columns = pd.DataFrame({'hall':['H1','H2','H3'],'visitors':[120,85,60],'capacity':[150,100,80]})
assert by_rows.equals(by_columns)
numeric = pd.DataFrame([[120,150],[85,100],[60,80]],
                       index=['H1','H2','H3'],columns=['visitors','capacity'])
aligned = pd.DataFrame({'visitors':pd.Series([120,85,60],index=['H1','H2','H3']),
                       'tickets':pd.Series([110,55],index=['H1','H3'])})
print('\n===== numeric.to_markdown() =====')
print(numeric.to_markdown())
print('\n===== aligned.to_markdown() =====')
print(aligned.to_markdown())
assert numeric.shape == (3,2) and numeric.loc['H2','capacity'] == 100
assert pd.isna(aligned.loc['H2','tickets']) and aligned.loc['H3','tickets'] == 55
# Series创建表时按标签对齐，不是把第二份Series的第二项放到第二行。

"""参考答案：按书架统计借阅与归还"""
# 对应 PDF：13-pandas-full.pdf 第 31—33 页
# 课件核心：第31—33页：mean/std/min/max/sum及DataFrame按列聚合。
# 扩展：agg、axis=1、count/size、min_count为统计口径扩展。
# 案例数据（据此自行创建对象，不能照抄 examples 的数据）：
# | shelf | borrowed | returned |
# |---|---|---|
# | A | 12 | 9 |
# | B | 8 | 8 |
# | C | 16 | 10 |
# 建议先做练习，再逐段对照下面的实现；assert 用于验证结果。

import pandas as pd
df = pd.DataFrame({'shelf':['A','B','C'],'borrowed':[12,8,16],'returned':[9,8,10]})
numeric = df[['borrowed','returned']]
summary = numeric.agg(['mean','std','min','max','sum'])
print('\n===== summary.to_markdown() =====')
print(summary.to_markdown())
df['outstanding'] = df['borrowed'] - df['returned']
print('\n===== df.to_markdown(index=False) =====')
print(df.to_markdown(index=False))
assert summary.loc['sum'].tolist() == [36,27]
assert df['outstanding'].tolist() == [3,0,6]
assert numeric.sum(axis=1).tolist() == [21,16,26]
changed = numeric.astype(float)
changed.loc[2,'returned'] = float('nan')
assert changed['returned'].count() == 2 and changed.size == 6
# min_count要求至少有多少有效值才给出总和，避免把未知总量误写成0。
assert pd.isna(pd.Series([None,None],dtype=float).sum(min_count=1))
# std默认ddof=1，为样本标准差，与NumPy默认ddof=0不同。

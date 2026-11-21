"""参考答案：不同用途下整理出行费用缺失"""
# 对应 PDF：13-pandas-full.pdf 第 43—44 页
# 课件核心：第43—44页：dropna与fillna，用有效列均值填补。
# 扩展：subset/how及填补标记为清洗规则扩展；0是有效免费行程。
# 案例数据（据此自行创建对象，不能照抄 examples 的数据）：
# | trip | fare | minutes |
# |---|---|---|
# | T1 | 20 | 30 |
# | T2 | None | 40 |
# | T3 | 40 | None |
# | T4 | None | None |
# | T5 | 0 | 10 |
# 建议先做练习，再逐段对照下面的实现；assert 用于验证结果。

import pandas as pd
df = pd.DataFrame({'trip':['T1','T2','T3','T4','T5'],
                   'fare':[20,None,40,None,0],'minutes':[30,40,None,None,10]})
print('\n===== df.dropna().to_markdown(index=False) =====')
print(df.dropna().to_markdown(index=False))
print("\n===== df.dropna(subset=['fare']).to_markdown(index=False) =====")
print(df.dropna(subset=['fare']).to_markdown(index=False))
assert df.dropna()['trip'].tolist() == ['T1','T5']
assert df.dropna(subset=['fare'])['trip'].tolist() == ['T1','T3','T5']
filled = df.copy()
filled['fare_estimated'] = filled['fare'].isna()
mean_fare = filled['fare'].mean()
filled['fare'] = filled['fare'].fillna(mean_fare)
print('\n===== filled.to_markdown(index=False) =====')
print(filled.to_markdown(index=False))
assert mean_fare == 20 and filled['fare'].tolist() == [20,20,40,20,0]
assert filled['minutes'].isna().sum() == 2
assert filled.loc[filled['fare_estimated'],'trip'].tolist() == ['T2','T4']
assert df.dropna(subset=['fare','minutes'],how='all')['trip'].tolist() == ['T1','T2','T3','T5']
# how='all'只删除所选字段全缺的行；默认how='any'是任意缺失就删。

"""参考答案：第一次接收设备巡检表"""
# 对应 PDF：13-pandas-full.pdf 第 18—20 页；补充head/info/describe用于检查
# 课件核心：第18—20页：columns、index、values、取列。
# 扩展：head/info/describe/to_numpy和检查属性为扩展；None表示真缺失，不是字符串。
# 案例数据（据此自行创建对象，不能照抄 examples 的数据）：
# | device | room | hours |
# |---|---|---|
# | D1 | A | 10 |
# | D2 | B | 20 |
# | D3 | A | 30 |
# | D4 | A | None |
# | D5 | C | 40 |
# 建议先做练习，再逐段对照下面的实现；assert 用于验证结果。

import pandas as pd
import numpy as np
df = pd.DataFrame({'device':['D1','D2','D3','D4','D5'],
                   'room':['A','B','A','A','C'],'hours':[10,20,30,None,40]})
print('\n===== df.columns =====')
print(df.columns)
print('\n===== df.index =====')
print(df.index)
# 扩展：head(n)看前n行；info()直接打印结构，返回None，不用print包裹。
print('\n===== df.head(3).to_markdown(index=False) =====')
print(df.head(3).to_markdown(index=False))
print('\n===== df.info() =====')
df.info()
summary = df.describe(include='all')
print('\n===== summary.to_markdown() =====')
print(summary.to_markdown())
numeric = df[['hours']].to_numpy()
print('\n===== numeric =====')
print(numeric)
assert df.shape == (5,3) and numeric.shape == (5,1)
assert np.isnan(numeric).sum() == 1
assert summary.loc['count','hours'] == 4 and summary.loc['mean','hours'] == 25
assert summary.loc['unique','room'] == 3 and summary.loc['top','room'] == 'A'
assert summary.loc['count','room'] == 5 and summary.loc['freq','room'] == 3
# hours有5行却只有4个有效值；mean不把缺失当0。A房间出现3次最多。

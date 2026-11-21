"""参考答案：区分设备读数缺测与非法文本"""
# 对应 PDF：13-pandas-full.pdf 第 41—42 页；to_numeric与可空整数为实用补充
# 课件核心：第41—42页：None/NaN、isnull/notnull与布尔筛选。
# 扩展：to_numeric(errors=coerce/raise)为类型清洗扩展；None是真缺失，带引号者为字符串。
# 案例数据（据此自行创建对象，不能照抄 examples 的数据）：
# | device | raw_reading |
# |---|---|
# | A | "12.5" |
# | B | "离线" |
# | C | None |
# | D | "0" |
# | E | "18" |
# 建议先做练习，再逐段对照下面的实现；assert 用于验证结果。

import pandas as pd
df = pd.DataFrame({'device':['A','B','C','D','E'],
                   'raw_reading':['12.5','离线',None,'0','18']})
assert df['raw_reading'].isnull().sum() == 1
# coerce将无法解析的非数值文本变成缺失，但原字段保留用于区分来源。
df['reading'] = pd.to_numeric(df['raw_reading'],errors='coerce')
bad = df.loc[df['raw_reading'].notnull() & df['reading'].isnull(),'device']
print('\n===== df.to_markdown(index=False) =====')
print(df.to_markdown(index=False))
print('\n===== bad =====')
print(bad)
assert bad.tolist() == ['B'] and df['reading'].isna().sum() == 2
assert df.loc[df['reading'] == 0,'device'].tolist() == ['D']
valid = pd.to_numeric(df.loc[df['reading'].notna(),'raw_reading'],errors='raise')
assert valid.tolist() == [12.5,0,18]
# raise的含义是“遇到非法值报错”，合法数字文本当然能成功；12.5有小数，不能无损转为整数。

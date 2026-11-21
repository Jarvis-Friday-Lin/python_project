"""参考答案：修正场馆容量并整理字段"""
# 对应 PDF：13-pandas-full.pdf 第 8、24—26、39 页
# 课件核心：第8、24—26、39页：loc赋值、新增列、drop与rename。
# 扩展：copy保护输入是实用补充，避免把重新赋值误认为就地修改。
# 案例数据（据此自行创建对象，不能照抄 examples 的数据）：
# | hall | booked | capacity | temp |
# |---|---|---|---|
# | H1 | 45 | 50 | x |
# | H2 | 70 | 60 | x |
# | H3 | 20 | 40 | x |
# 建议先做练习，再逐段对照下面的实现；assert 用于验证结果。

import pandas as pd
original = pd.DataFrame({'hall':['H1','H2','H3'],'booked':[45,70,20],
                         'capacity':[50,60,40],'temp':['x','x','x']})
clean = original.copy()
clean.loc[clean['hall'] == 'H2','capacity'] = 80
clean['remaining'] = clean['capacity'] - clean['booked']
# drop/rename默认返回新表，接收返回值，避免误以为调用后原表必然改变。
clean = clean.drop(columns=['temp']).rename(columns={'booked':'reserved'})
print('\n===== clean.to_markdown(index=False) =====')
print(clean.to_markdown(index=False))
assert clean['remaining'].tolist() == [5,10,20]
assert original.loc[1,'capacity'] == 60 and 'temp' in original
assert 'temp' not in clean and 'booked' not in clean and 'reserved' in clean
assert clean['reserved'].tolist() == [45,70,20]

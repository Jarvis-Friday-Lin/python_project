"""参考答案：用商品库存理解一列与整张表"""
# 对应 PDF：13-pandas-full.pdf 第2—5、12—13、20、31—32页；筛选复习第10、23页
# 课件核心：第2—5、12—13、20、31—32页：Series/DataFrame、取列、统计。
# 扩展：shape为结果检查补充；筛选复习第10、23页，不要求高级API。
# 案例数据（据此自行创建对象，不能照抄 examples 的数据）：
# | product | category | stock |
# |---|---|---|
# | 铅笔 | 文具 | 12 |
# | 笔记本 | 文具 | 4 |
# | 水杯 | 日用 | 8 |
# | 纸巾 | 日用 | 0 |
# 建议先做练习，再逐段对照下面的实现；assert 用于验证结果。

import pandas as pd
df = pd.DataFrame({'product':['铅笔','笔记本','水杯','纸巾'],
                   'category':['文具','文具','日用','日用'],'stock':[12,4,8,0]})
# index给每个值加商品标签；name是整列的名字，而不是某个商品名。
stock = pd.Series([12,4,8,0],index=['铅笔','笔记本','水杯','纸巾'],name='stock')
print('\n===== stock =====')
print(stock)
print('\n===== stock.sum() =====')
print(stock.sum())
low = df.loc[df['stock'] <= 4, ['product','category']]
print('\n===== low.to_markdown(index=False) =====')
print(low.to_markdown(index=False))
assert stock.sum() == 24 and stock.name == 'stock'
assert low['product'].tolist() == ['笔记本','纸巾']
assert isinstance(df['stock'],pd.Series) and df['stock'].shape == (4,)
assert isinstance(df[['stock']],pd.DataFrame) and df[['stock']].shape == (4,1)
# 单列有sum等列运算；整表保留补货识别所需的多个字段。

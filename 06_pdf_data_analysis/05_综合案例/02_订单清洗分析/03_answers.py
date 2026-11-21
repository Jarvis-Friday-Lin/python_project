"""参考答案：综合迁移：核查快递重量记录"""
# 对应 PDF：13-pandas-full.pdf 第23—26、34—36、41—46页综合
# 课件核心：Pandas第23—26、34—36、41—46页：筛选、缺失、分组、导出。
# 扩展：to_numeric、duplicated和互斥原因分类为扩展；优先级：重复>未签收>原始缺失>非法文本>非正重量。
# 案例数据（据此自行创建对象，不能照抄 examples 的数据）：
# | parcel_id | zone | weight_raw | signed |
# |---|---|---|---|
# | P1 | East | "2.5" | yes |
# | P2 | West | "1.5" | yes |
# | P1 | East | "2.5" | yes |
# | P3 | East | "损坏" | yes |
# | P4 | West | "-1" | yes |
# | P5 | North | "4" | no |
# | P6 | East | None | yes |
# 建议先做练习，再逐段对照下面的实现；assert 用于验证结果。

from pathlib import Path
import pandas as pd
df = pd.DataFrame({'parcel_id':['P1','P2','P1','P3','P4','P5','P6'],
                   'zone':['East','West','East','East','West','North','East'],
                   'weight_raw':['2.5','1.5','2.5','损坏','-1','4',None],
                   'signed':['yes','yes','yes','yes','yes','no','yes']})
df['weight'] = pd.to_numeric(df['weight_raw'],errors='coerce')
df['reason'] = ''
# 按优先级逐项赋值，只给尚未归类的记录填原因，避免后一个条件覆盖前一个原因。
rules = [(df.duplicated('parcel_id',keep='first'),'重复'),
         (df['signed'] != 'yes','未签收'),(df['weight_raw'].isna(),'原始缺失'),
         (df['weight'].isna(),'非法文本'),(df['weight'] <= 0,'非正重量')]
for mask, reason in rules:
    df.loc[(df['reason'] == '') & mask,'reason'] = reason
valid, issues = df.loc[df['reason'] == ''].copy(),df.loc[df['reason'] != ''].copy()
summary = valid.groupby('zone').agg(weight=('weight','sum'),parcels=('parcel_id','size')).reset_index()
print('\n===== summary.to_markdown(index=False) =====')
print(summary.to_markdown(index=False))
print('\n===== issues.to_markdown(index=False) =====')
print(issues.to_markdown(index=False))
assert valid['parcel_id'].tolist() == ['P1','P2'] and valid['weight'].sum() == 4
assert len(valid) == 2 and len(issues) == 5 and len(valid)+len(issues) == len(df)
assert issues['reason'].tolist() == ['重复','非法文本','非正重量','未签收','原始缺失']
assert summary.set_index('zone')['weight'].to_dict() == {'East':2.5,'West':1.5}
out = Path(__file__).resolve().parent / 'outputs'
out.mkdir(exist_ok=True)
for name, table in [('valid_parcels',valid),('parcel_issues',issues),('zone_summary',summary)]:
    table.to_csv(out/f'{name}.csv',index=False)
    assert (out/f'{name}.csv').stat().st_size > 0

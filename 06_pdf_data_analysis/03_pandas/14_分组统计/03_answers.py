"""参考答案：按科室汇总维修工单"""
# 对应 PDF：13-pandas-full.pdf 第 45—46 页
# 课件核心：第45—46页：groupby、遍历分组、组内mean/sum、reset_index。
# 扩展：agg/count/size的比较为扩展；0工时有效、None未登记。
# 案例数据（据此自行创建对象，不能照抄 examples 的数据）：
# | ticket | team | hours |
# |---|---|---|
# | W1 | electrical | 2 |
# | W2 | plumbing | 3 |
# | W3 | electrical | 4 |
# | W4 | plumbing | None |
# | W5 | electrical | 0 |
# 建议先做练习，再逐段对照下面的实现；assert 用于验证结果。

import pandas as pd
df = pd.DataFrame({'ticket':['W1','W2','W3','W4','W5'],
                   'team':['electrical','plumbing','electrical','plumbing','electrical'],
                   'hours':[2,3,4,None,0]})
grouped = df.groupby('team')
for key, part in grouped:
    print('\n===== key =====')
    print(key)
    print('\n===== part.to_markdown(index=False) =====')
    print(part.to_markdown(index=False))
    print("\n===== (part['hours'].sum(), part['hours'].mean()) =====")
    print((part['hours'].sum(),part['hours'].mean()))
# 扩展：命名聚合把每个输出列的来源与方法写清楚。
summary = grouped.agg(total_hours=('hours','sum'),average_hours=('hours','mean'),
                      valid_hours=('hours','count'),tickets=('ticket','size')).reset_index()
print('\n===== summary.to_markdown(index=False) =====')
print(summary.to_markdown(index=False))
result = summary.set_index('team')
assert result.loc['electrical'].tolist() == [6,2,3,3]
assert result.loc['plumbing'].tolist() == [3,3,1,2]
# count排除缺失；size计行数；0工时会参与有效值计数和均值分母。

"""参考答案：从借阅原始记录到分类汇总"""
# 对应 PDF：13-pandas-full.pdf 第 20—46 页综合
# 课件核心：第20—26、31—36、41—46页：取列、筛选、统计、缺失、分组、CSV导出。
# 扩展：to_numeric与问题原因标记为扩展；任务不依赖原orders.csv。
# 案例数据（据此自行创建对象，不能照抄 examples 的数据）：
# | record_id | category | pages_raw | returned |
# |---|---|---|---|
# | L1 | science | "120" | yes |
# | L2 | history | "80" | yes |
# | L3 | science | "200" | yes |
# | L4 | art | "未知" | yes |
# | L5 | history | "60" | no |
# | L6 | art | "-10" | yes |
# 建议先做练习，再逐段对照下面的实现；assert 用于验证结果。

from pathlib import Path
import pandas as pd
df = pd.DataFrame({'record_id':['L1','L2','L3','L4','L5','L6'],
                   'category':['science','history','science','art','history','art'],
                   'pages_raw':['120','80','200','未知','60','-10'],
                   'returned':['yes','yes','yes','yes','no','yes']})
df['pages'] = pd.to_numeric(df['pages_raw'],errors='coerce')
df['reason'] = ''
df.loc[df['pages'].isna(),'reason'] = '非法页数'
df.loc[df['pages'] < 0,'reason'] = '负页数'
df.loc[df['returned'] != 'yes','reason'] = '未归还'
valid, issues = df.loc[df['reason'] == ''].copy(), df.loc[df['reason'] != ''].copy()
summary = valid.groupby('category')['pages'].agg(['sum','mean']).reset_index()
print('\n===== summary.to_markdown(index=False) =====')
print(summary.to_markdown(index=False))
print('\n===== issues.to_markdown(index=False) =====')
print(issues.to_markdown(index=False))
assert valid['record_id'].tolist() == ['L1','L2','L3']
assert len(valid)+len(issues) == len(df) == 6
assert summary.set_index('category')['sum'].to_dict() == {'history':80,'science':320}
assert summary.set_index('category')['mean'].to_dict() == {'history':80,'science':160}
assert issues['reason'].tolist() == ['非法页数','未归还','负页数']
out = Path(__file__).resolve().parent / 'outputs'
out.mkdir(exist_ok=True)
summary.to_csv(out/'library_summary.csv',index=False)
issues.to_csv(out/'library_issues.csv',index=False)
# 保留原文本与原因，方便追溯；不把无法解析的页数静默填成0。

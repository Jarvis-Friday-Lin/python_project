"""参考答案：综合迁移：候选人的技能画像"""
# 对应 PDF：11-numpy-full.pdf 第17—21、37—51页；13-pandas-full.pdf 第13、20、31—36页
# 课件核心：NumPy第17—21、37—51页的权重计算/中心化/成对距离；Pandas第13、20、31—33页建表与统计。
# 扩展：sort_values(kind="stable")和CSV路径为综合扩展；技能分数尺度相同，仅为模拟，不作真实招聘评估。
# 案例数据（据此自行创建对象，不能照抄 examples 的数据）：
# | name | coding | reasoning | communication |
# |---|---|---|---|
# | 安宁 | 80 | 60 | 90 |
# | 白杨 | 70 | 90 | 70 |
# | 程遥 | 90 | 70 | 80 |
# | 丁可 | 80 | 60 | 90 |
# | 参考画像R1 | 80 | 60 | 90 |
# | 参考画像R2 | 70 | 90 | 70 |
# | 权重 | 0.4 | 0.4 | 0.2 |
# 建议先做练习，再逐段对照下面的实现；assert 用于验证结果。

from pathlib import Path
import numpy as np
import pandas as pd
df = pd.DataFrame({'name':['安宁','白杨','程遥','丁可'],'coding':[80,70,90,80],
                   'reasoning':[60,90,70,60],'communication':[90,70,80,90]})
skills = df[['coding','reasoning','communication']].to_numpy()
weights = np.array([0.4,0.4,0.2])
df['weighted'] = skills @ weights
centered = skills-skills.mean(axis=0)
references = np.array([[80,60,90],[70,90,70]])
distances = np.sqrt(((skills[:,None,:]-references[None,:,:])**2).sum(axis=2))
df['distance_R1'],df['distance_R2'] = distances[:,0],distances[:,1]
ranked = df.sort_values('weighted',ascending=False,kind='stable')
print('\n===== ranked.to_markdown(index=False) =====')
print(ranked.to_markdown(index=False))
print('\n===== distances =====')
print(distances)
assert np.allclose(df['weighted'],[74,78,80,74])
assert ranked['name'].tolist() == ['程遥','白杨','安宁','丁可']
assert distances.shape == (4,2) and distances[0,0] == distances[3,0] == distances[1,1] == 0
assert np.allclose(centered.mean(axis=0),0)
out = Path(__file__).resolve().parent / 'outputs'
out.mkdir(exist_ok=True)
ranked.to_csv(out/'candidate_report.csv',index=False)
assert (out/'candidate_report.csv').stat().st_size > 0
# 距离只表示同尺度特征接近程度，不说明某候选人一定更适合实际岗位。

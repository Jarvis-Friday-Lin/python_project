"""案例驱动示例：同一缺失表可以有不同清洗结果"""
# 对应 PDF：13-pandas-full.pdf 第 43—44 页
# 任务：为工资统计选择可解释的缺失处理方案。
# 删除行、填均值、填固定值各有含义，不能为了表格好看全部补0。
# 案例数据：
# | name | salary | experience |
# |---|---:|---:|
# | A | 100 | 2 |
# | B | 缺失 | 5 |
# | C | 300 | 缺失 |
# | D | 缺失 | 缺失 |
# 先看整体路线：
# 第 1 步：先统计每列缺失数。
# 第 2 步：比较按任一列、指定列、全缺失和有效数门槛删除。
# 第 3 步：按列分别填补，再比较统计与样本量。

import pandas as pd
data=pd.DataFrame({"name":["A","B","C","D"],"salary":[100,None,300,None],"experience":[2,5,None,None]})
print('\n===== data.isna().sum() =====')
print(data.isna().sum())
print('\n===== data.dropna().to_markdown(index=False) =====')
print(data.dropna().to_markdown(index=False))
# subset限定哪些列决定是否删行；不关心的缺失不应误删。
print('\n===== data.dropna(subset=["salary"]).to_markdown(index=False) =====')
print(data.dropna(subset=["salary"]).to_markdown(index=False))
print('\n===== data.dropna(subset=["salary","experience"],how="all").to_markdown(index=False) =====')
print(data.dropna(subset=["salary","experience"],how="all").to_markdown(index=False))
# thresh=2要求这两列至少2个有效值；不能与how同时使用。
print('\n===== data.dropna(subset=["salary","experience"],thresh=2).to_markdown(index=False) =====')
print(data.dropna(subset=["salary","experience"],thresh=2).to_markdown(index=False))
# 每列独立定策略：salary均值200，experience缺失保留。
filled=data.fillna({"salary":data["salary"].mean()})
print('\n===== filled.to_markdown(index=False) =====')
print(filled.to_markdown(index=False))
# 填补会改变分布与有效样本量；填入的值不是新观测，需保留标记。
filled["salary_imputed"]=data["salary"].isna()
print('\n===== filled.to_markdown(index=False) =====')
print(filled.to_markdown(index=False))
assert len(data.dropna(subset=["salary"]))==2
assert filled["salary"].tolist()==[100,200,300,200]
# 全缺失列均值仍缺失，fillna(mean)不能神奇恢复不存在的信息。
# axis=1改为删除列：有缺失的salary/experience都消失，只剩name。
print('\n===== data.dropna(axis=1).to_markdown(index=False) =====')
print(data.dropna(axis=1).to_markdown(index=False))
# 可以按中位数填补，或显式填固定标记；-1在此只是待核查标记，不能参与工资均值。
print('\n===== data.fillna({"salary":data["salary"].median()}).to_markdown(index=False) =====')
print(data.fillna({"salary":data["salary"].median()}).to_markdown(index=False))
print('\n===== data.fillna({"salary":-1}).to_markdown(index=False) =====')
print(data.fillna({"salary":-1}).to_markdown(index=False))
# ffill/bfill借用相邻记录填值，只适合有明确顺序且允许继承的序列。
# 员工工资不能借上一名员工的数值；这里另用连续温度测量作对比。
temperature=pd.Series([20.,None,None,23.])
print('\n===== temperature.ffill(limit=1) =====')
print(temperature.ffill(limit=1))
print('\n===== temperature.bfill(limit=1) =====')
print(temperature.bfill(limit=1))
# limit=1限制一次连续缺口最多填1格，不表示把所有缺失都填上。
assert temperature.ffill(limit=1).isna().sum()==1

# 学完先自己回答，再看下面的参考答案：
# 1. 这个知识点解决什么类型的问题？
# 2. 为什么当前案例需要它？
# 3. 每一步代码为什么要在此时出现？
# 4. 如果换一种做法，代价和风险是什么？

# 参考答案：
# 1. 选择可解释的缺失处理策略。
# 2. 工资分析未必要求经验完整，统一dropna会损失可用工资。
# 3. 先计数明确损失，再比较删除范围，最后按列填补并标记来源。
# 4. 填0简单但虚构零工资；删行可能有选择偏差，均值填补会压低波动。

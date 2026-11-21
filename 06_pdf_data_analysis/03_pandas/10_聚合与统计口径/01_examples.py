"""案例驱动示例：列统计、行统计与缺失计数"""
# 对应 PDF：13-pandas-full.pdf 第 31—33 页
# 任务：统计两名员工工资、奖金与收入。
# DataFrame默认按列汇总；混合文本列应先选数值列，不能指望所有统计自动理解业务。
# 案例数据：
# | name | salary | bonus |
# |---|---:|---:|
# | A | 100 | 10 |
# | B | 200 | 30 |
# 先看整体路线：
# 第 1 步：手工计算总工资作为基准。
# 第 2 步：分别对Series和数值DataFrame求聚合。
# 第 3 步：解释axis、ddof、count与size。

import pandas as pd
data=pd.DataFrame({"name":["A","B"],"salary":[100,200],"bonus":[10,30]})
print('\n===== sum(data["salary"]) =====')
print(sum(data["salary"]))
print('\n===== data["salary"].sum() =====')
print(data["salary"].sum())
numbers=data[["salary","bonus"]]
print('\n===== numbers.mean(axis=0) =====')
print(numbers.mean(axis=0))
print('\n===== numbers.sum(axis=1) =====')
print(numbers.sum(axis=1))
# agg可以一次列出多种统计；得到的行名是统计函数名。
print('\n===== numbers.agg(["sum","mean","min","max","std"]).to_markdown() =====')
print(numbers.agg(["sum","mean","min","max","std"]).to_markdown())
# Pandas std默认ddof=1，NumPy默认ddof=0；比较前统一口径。
print('\n===== numbers.std(ddof=0) =====')
print(numbers.std(ddof=0))
modified=numbers.copy()
modified.loc[1,"bonus"]=None
print('\n===== modified.count() =====')
print(modified.count())
print('\n===== modified.size =====')
print(modified.size)
# count按列数非缺失格子，size是整张表格子总数，不忽略缺失。
# 全缺失列sum默认0可能误导；min_count=1要求至少有一个有效值。
print('\n===== pd.Series([None,None],dtype=float).sum(min_count=1) =====')
print(pd.Series([None,None],dtype=float).sum(min_count=1))
assert numbers.sum(axis=1).tolist()==[110,230]

# 学完先自己回答，再看下面的参考答案：
# 1. 这个知识点解决什么类型的问题？
# 2. 为什么当前案例需要它？
# 3. 每一步代码为什么要在此时出现？
# 4. 如果换一种做法，代价和风险是什么？

# 参考答案：
# 1. 将多个记录压缩成可解释的统计。
# 2. 工资平均与每人收入沿不同轴计算，缺失也影响统计口径。
# 3. 先选数值列，再明确轴和缺失策略，最后解释统计输出。
# 4. 手工统计易核算小数据；默认求和或标准差口径不明会导致误读。

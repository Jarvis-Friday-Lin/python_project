"""案例驱动示例：有标签的成绩与学生表"""
# 对应 PDF：13-pandas-full.pdf 第 2—5、12 页
# Pandas 是面向表格数据处理与分析的库。Series 表示带标签的一维数据，DataFrame 表示有行列的二维表。
# 任务：计算Python平均分，找到>=85分的学生，并保留姓名和城市。
# 案例数据：
# | name | city | score |
# |---|---|---:|
# | 小林 | 上海 | 95 |
# | 小周 | 北京 | 84 |
# | 小陈 | 上海 | 90 |
# | 小李 | 深圳 | 75 |
# 先看整体路线：
# 第 1 步：先用字典列表完成平均和筛选。
# 第 2 步：把一列成绩变成Series，把整份记录变成DataFrame。
# 第 3 步：逐项比较类型、标签、形状与筛选结果。

import pandas as pd
rows=[{"name":"小林","city":"上海","score":95},{"name":"小周","city":"北京","score":84},
      {"name":"小陈","city":"上海","score":90},{"name":"小李","city":"深圳","score":75}]
print('\n===== sum(row["score"] for row in rows)/len(rows) =====')
print(sum(row["score"] for row in rows)/len(rows))
print('\n===== [row for row in rows if row["score"]>=85] =====')
print([row for row in rows if row["score"]>=85])
# 列表写法没错，但取列、统计、筛选分别维护遍历；字段增加后需要继续组合逻辑。
# data是实际值，index给每个值姓名标签，name是整列名称，三者含义不同。
scores=pd.Series(data=[95,84,90,75],index=["小林","小周","小陈","小李"],name="Python")
print('\n===== scores =====')
print(scores)
print('\n===== (scores.index.tolist(),scores.name,scores.shape) =====')
print((scores.index.tolist(),scores.name,scores.shape))
# DataFrame从字典列表创建：每个字典是一行，相同键名形成同一列。
data=pd.DataFrame(rows)
print('\n===== data.to_markdown(index=False) =====')
print(data.to_markdown(index=False))
print('\n===== type(data).__name__ =====')
print(type(data).__name__)
print('\n===== data["score"].mean() =====')
print(data["score"].mean())
# data["score"]返回Series；data[["score"]]返回只有一列的DataFrame。
print('\n===== (data["score"].shape,data[["score"]].shape) =====')
print((data["score"].shape,data[["score"]].shape))
# loc[行条件,列选择]，这里未指定列所以保留整行字段。
print('\n===== data.loc[data["score"]>=85].to_markdown(index=False) =====')
print(data.loc[data["score"]>=85].to_markdown(index=False))
assert data["score"].mean()==86
assert data.loc[data["score"]>=85,"name"].tolist()==["小林","小陈"]

# 学完先自己回答，再看下面的参考答案：
# 1. 这个知识点解决什么类型的问题？
# 2. 为什么当前案例需要它？
# 3. 每一步代码为什么要在此时出现？
# 4. 如果换一种做法，代价和风险是什么？

# 参考答案：
# 1. 带字段含义的列与表的分析。
# 2. 筛选结果要保留姓名城市，而平均分只需要一列。
# 3. 先以基础语法建立基准，再构造对象，取列统计后用行条件保留记录。
# 4. 列表字典依赖手动遍历；Pandas集中表达表格操作，但必须理解索引和返回类型。

"""案例驱动示例：接到一张表先检查什么"""
# 对应 PDF：13-pandas-full.pdf 第 18—20 页；补充head/info/describe用于检查
# 任务：在计算学生平均分前检查表结构、字段类型和描述统计。
# 这些检查回答“我实际拿到什么”，不只是为了多打印几次。
# 案例数据：
# | name | city | score |
# |---|---|---:|
# | 小林 | 上海 | 95 |
# | 小周 | 北京 | 84 |
# | 小陈 | 上海 | 90 |
# | 小李 | 深圳 | 75 |
# 先看整体路线：
# 第 1 步：查看head和shape确定对象规模。
# 第 2 步：读取列名、索引、类型，再用info核对。
# 第 3 步：解释describe的混合类型结果，并只将数值列转成数组。

import pandas as pd
data=pd.DataFrame({"name":["小林","小周","小陈","小李"],"city":["上海","北京","上海","深圳"],"score":[95,84,90,75]})
# head(n=5)返回前n行；本表仅4行，所以默认返回全部。
print('\n===== data.head().to_markdown(index=False) =====')
print(data.head().to_markdown(index=False))
print('\n===== data.shape =====')
print(data.shape)
print('\n===== data.columns.tolist() =====')
print(data.columns.tolist())
print('\n===== data.index.tolist() =====')
print(data.index.tolist())
print('\n===== data.dtypes =====')
print(data.dtypes)
# info()直接输出列数、非空数、dtype，返回None，不要写print(data.info())。
print('\n===== data.info() =====')
data.info()
print('\n===== data.describe(include="all").to_markdown() =====')
print(data.describe(include="all").to_markdown())
# count是不缺失个数；文本列unique是不同值数量、top/freq是最常见值及频数。
# score列mean=86，std默认样本标准差(ddof=1)，25%/50%/75%是分位数。
# 某列不适用的指标显示NaN，比如文本列没有mean，数字列没有top。
array=data[["score"]].to_numpy()
print('\n===== array =====')
print(array)
# 整张混合表转数组通常为object，姓名不会自动变成数值编码。
print('\n===== data.to_numpy().dtype =====')
print(data.to_numpy().dtype)
assert data.shape==(4,3)
assert data.describe(include="all").loc["unique","city"]==3

# 学完先自己回答，再看下面的参考答案：
# 1. 这个知识点解决什么类型的问题？
# 2. 为什么当前案例需要它？
# 3. 每一步代码为什么要在此时出现？
# 4. 如果换一种做法，代价和风险是什么？

# 参考答案：
# 1. 了解表规模、字段类型、缺失情况和统计分布。
# 2. 成绩必须是数字，城市重复不是异常，要先读懂数据。
# 3. 先看样本再核对结构，确认类型后才解释统计并转数组。
# 4. 直接计算可能对错误类型或错误列操作；检查能发现问题，但抽样不能证明全表无错。

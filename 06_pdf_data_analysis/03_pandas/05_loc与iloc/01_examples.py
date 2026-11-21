"""案例驱动示例：按身份与按位置选行列"""
# 对应 PDF：13-pandas-full.pdf 第 6、9、20—22、38—40 页
# 任务：使用学生姓名为索引，查询指定学生与成绩列。
# loc写标签，iloc写位置；选择结果可能是标量、Series或DataFrame。
# 案例数据：
# | name | city | score |
# |---|---|---:|
# | 小林 | 上海 | 95 |
# | 小周 | 北京 | 84 |
# | 小陈 | 上海 | 90 |
# | 小李 | 深圳 | 75 |
# 先看整体路线：
# 第 1 步：建立姓名索引并取单值。
# 第 2 步：比较单行单列与列表选择的返回类型。
# 第 3 步：练习切片和不连续多选，核对边界。

import pandas as pd
data=pd.DataFrame({"city":["上海","北京","上海","深圳"],"score":[95,84,90,75]},index=["小林","小周","小陈","小李"])
# loc[行标签,列标签]；iloc[行位置,列位置]，两个轴用逗号分开。
print('\n===== data.loc["小周","score"] =====')
print(data.loc["小周","score"])
print('\n===== data.iloc[1,1] =====')
print(data.iloc[1,1])
print('\n===== data.loc["小周"] =====')
print(data.loc["小周"])
print('\n===== data.loc[["小周"]].to_markdown() =====')
print(data.loc[["小周"]].to_markdown())
print('\n===== data["score"] =====')
print(data["score"])
print('\n===== data[["score"]].to_markdown() =====')
print(data[["score"]].to_markdown())
# 有序且唯一标签时loc切片包括末标签；iloc切片不包括末位置。
print('\n===== data.loc["小林":"小陈",["city","score"]].to_markdown() =====')
print(data.loc["小林":"小陈",["city","score"]].to_markdown())
print('\n===== data.iloc[:2,:].to_markdown() =====')
print(data.iloc[:2,:].to_markdown())
print('\n===== data.loc[["小李","小林"],["score"]].to_markdown() =====')
print(data.loc[["小李","小林"],["score"]].to_markdown())
# at/iat是取单个标量的便捷接口，与loc/iloc多选接口用途不同。
print('\n===== data.at["小林","score"] =====')
print(data.at["小林","score"])
print('\n===== data.iat[0,1] =====')
print(data.iat[0,1])
assert isinstance(data.loc["小周"],pd.Series)
assert data.loc[["小周"]].shape==(1,2)
# 不用“iloc['小周']”，位置接口不接受人名标签。

# 学完先自己回答，再看下面的参考答案：
# 1. 这个知识点解决什么类型的问题？
# 2. 为什么当前案例需要它？
# 3. 每一步代码为什么要在此时出现？
# 4. 如果换一种做法，代价和风险是什么？

# 参考答案：
# 1. 按标签或位置精确选取数据并控制结果形状。
# 2. 学生身份不会因为行顺序变动而改变。
# 3. 先建索引再确定选择依据，随后比较单选多选，最后看边界与类型。
# 4. 按位置简短但重排后身份可能变；按标签可靠但要求索引含义明确。

"""案例驱动示例：类型转换与缺失值"""

# 案例任务：
# 报名表的年龄包含数字、未知和空白，成绩也有缺失。

# ===== 第一步：先用已经学过的基础语法解决案例 =====
# 任务已经明确，接下来先用列表、字典、循环和算术运算完成它。
# 先看整体路线：
# 第 1 步：先查看 dtype 和 isna 统计，不要把缺失直接当成 0。
# 第 2 步：用 to_numeric 的 errors 参数把非法文本转为可识别的缺失。
# 第 3 步：根据业务决定删除、保留或用中位数填补。
# 第 4 步：比较处理前后的行数、缺失量和统计结果。
# 顺序不能随意交换：先准备并理解输入，才能进行后续转换、分析和检查。

raw_values = ["18", "未知", None]
values = []
for value in raw_values:
    try:
        values.append(float(value))
    except (TypeError, ValueError):
        values.append(None)
print("逐个转换后的值：", values)

# 对不用 Pandas 方案的评价：
# 上面的对照代码可以得到结果，但它把很多工作留给我们自己：也可以逐个值 try/except；但规则分散且难以统计影响。Pandas 的转换、NaN 和填补方法能批量处理并保留缺失语义。所以我们自然会问：有没有一种现成的数据对象，能把这些重复工作统一起来？有，Pandas 的“类型转换与缺失值”正是为这类表格问题准备的。接下来先用最小步骤试用它，每一步都看清楚输入、输出和为什么要继续下一步。

# ===== 第二步：使用 Pandas 的实现 =====
# 具体函数的入参、关键字参数和返回值，放在每个调用的上一行或下一行说明。
# 进入代码前先确认：本节是在处理哪种表格对象？核心方法要解决什么问题？输入是什么，返回结果的形状会怎样变化？
# 本节是在处理哪种表格对象？主要处理带行索引和列名的 DataFrame，部分方法会先取出其中一列 Series。
# 核心方法要解决什么问题？解决“类型转换与缺失值”这一类表格分析任务：识别空值、选择删除或填补策略，并使用稳健转换。
# 输入是什么，返回结果的形状会怎样变化？输入是案例中的原始表格；主要方法的参数和返回结果如下：to_numeric(arg, errors=...) 把 arg 转为数值，errors='coerce' 把无法转换的值变为 NaN；isna() 统计缺失，fillna(value) 用 value 填补。每个方法都返回结果，除非显式赋回原列，否则不会自动修改原表。
# 第 1 步：先查看 dtype 和 isna 统计，不要把缺失直接当成 0。
# 为什么：先查看 dtype 和缺失，是因为处理策略取决于问题是类型错误、真正缺失还是业务上的未知。
# 调用提示：to_numeric(arg, errors=...) 把 arg 转为数值，errors='coerce' 把无法转换的值变为 NaN；isna() 统计缺失，fillna(value) 用 value 填补。每个方法都返回结果，除非显式赋回原列，否则不会自动修改原表。
import pandas as pd
data = pd.DataFrame({"age": ["18", "错误", None], "score": [90, None, 80]})
# to_numeric 的 errors="coerce" 会把无法转换的文本变成 NaN，而不是让程序直接报错。
data["age"] = pd.to_numeric(data["age"], errors="coerce")
# median() 求中位数；fillna(中位数) 用统计值补齐 score 的缺失项。
data["score"] = data["score"].fillna(data["score"].median())
print('\n===== data.to_markdown(index=False) =====')
print(data.to_markdown(index=False))
print('\n===== data.isna().sum() =====')
print(data.isna().sum())

# 类型与缺失值的常用变体：查看、删除、填充和不同错误策略。
print("\n===== isna / notna =====")
print(data.isna())
print(data.notna())
print("\n===== dropna(subset=...) =====")
# dropna(subset=["score"]) 只删除 score 缺失的行，不会把数值重新转回整数。
# score 原本包含 None/NaN，Pandas 为了同时容纳整数和缺失值，通常会把这一列提升为 float，所以看到 90.0、80.0 是正常的。
print(data.dropna(subset=["score"]))
# age 经过 to_numeric(errors="coerce") 后，"错误" 变成 NaN，同样可能导致这一列显示为浮点数。
print(data.dropna(subset=["age"]))
print("\n===== fillna(标量) =====")
print(data["score"].fillna(0))
print("\n===== to_numeric(errors='ignore') 对比 =====")
# 注意：前面已经用 errors="coerce" 把“错误”转换成 NaN；现在再用 errors="raise"，检查的是已经清洗过的列，所以不会报错。
print(pd.to_numeric(data["age"], errors="raise"))
# 如果要观察 errors="raise" 的报错，必须对仍含有非法文本的原始数据执行转换。
raw_age = pd.Series(["18", "错误", None])
# print(pd.to_numeric(raw_age, errors="raise"))  # 会因为“错误”无法转换而抛出 ValueError
print(pd.to_numeric(data["age"], errors="coerce"))

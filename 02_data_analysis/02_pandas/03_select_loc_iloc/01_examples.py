"""案例驱动示例：选择数据：loc 与 iloc"""

# 案例任务：
# 从订单明细中找出上海订单，并只交付编号、商品和金额三列。

# ===== 第一步：先用已经学过的基础语法解决案例 =====
# 任务已经明确，接下来先用列表、字典、循环和算术运算完成它。
# 先看整体路线：
# 第 1 步：先明确需要的列名和筛选条件，避免先打印整张大表。
# 第 2 步：使用 loc 按标签和条件选择，观察返回结果的行列数。
# 第 3 步：使用 iloc 取前两行，比较位置选择和标签选择的差异。
# 第 4 步：检查选择结果是否保留原索引，并验证没有误取列。
# 顺序不能随意交换：先准备并理解输入，才能进行后续转换、分析和检查。

rows = [
    {"order_id": "S001", "city": "上海", "amount": 798},
    {"order_id": "S002", "city": "北京", "amount": 387},
]
selected = [row for row in rows if row["city"] == "上海"]
print("列表筛选：", selected)
print("列表位置切片：", rows[:1])

# 对不用 Pandas 方案的评价：
# 上面的对照代码可以得到结果，但它把很多工作留给我们自己：也可以用 for 循环逐行判断或先转成列表；但代码更长、容易漏列。loc/iloc 的优势是表达清晰、批量操作和结果形状可预测。所以我们自然会问：有没有一种现成的数据对象，能把这些重复工作统一起来？有，Pandas 的“选择数据：loc 与 iloc”正是为这类表格问题准备的。接下来先用最小步骤试用它，每一步都看清楚输入、输出和为什么要继续下一步。

# ===== 第二步：使用 Pandas 的实现 =====
# 具体函数的入参、关键字参数和返回值，放在每个调用的上一行或下一行说明。
# 进入代码前先确认：本节是在处理哪种表格对象？核心方法要解决什么问题？输入是什么，返回结果的形状会怎样变化？
# 本节是在处理哪种表格对象？主要处理带行索引和列名的 DataFrame，部分方法会先取出其中一列 Series。
# 核心方法要解决什么问题？解决“选择数据：loc 与 iloc”这一类表格分析任务：按标签或整数位置选择行列，并避免含糊的链式索引。
# 输入是什么，返回结果的形状会怎样变化？输入是案例中的原始表格；主要方法的参数和返回结果如下：loc[行条件, 列标签] 按标签选择，行条件可以是标签或布尔 Series；iloc[行位置, 列位置] 按整数位置选择。loc 的列参数可写一个列名或列名列表，结果可能是 Series 或 DataFrame。
# 第 1 步：先明确需要的列名和筛选条件，避免先打印整张大表。
# 为什么：先列出需要的字段和条件，是为了把业务需求翻译成最小结果集，减少误取和内存浪费。
# 调用提示：loc[行条件, 列标签] 按标签选择，行条件可以是标签或布尔 Series；iloc[行位置, 列位置] 按整数位置选择。loc 的列参数可写一个列名或列名列表，结果可能是 Series 或 DataFrame。
import pandas as pd
data = pd.DataFrame({"name": ["甲", "乙", "丙"], "score": [88, 95, 76]})
# loc[行条件, 列标签] 按标签选择；这里的行条件会保留 score >= 80 的行，列列表只保留 name 和 score。
# 返回值是 DataFrame，因为我们选择了多列；如果只写 data.loc[条件, "name"]，结果会是 Series。
print('\n===== data.loc[data["score"] >= 80, ["name", "score"]].to_markdown(index=False) =====')
print(data.loc[data["score"] >= 80, ["name", "score"]].to_markdown(index=False))
# iloc[行位置, 列位置] 按整数位置选择；:2 表示第 0、1 行，: 表示保留所有列。
# iloc 的切片终点不包含 2，返回仍是 DataFrame，因为这里保留了二维表结构。
print('\n===== data.iloc[:2, :].to_markdown(index=False) =====')
print(data.iloc[:2, :].to_markdown(index=False))

# loc/iloc 的常用变体：选单列、选多列、选单行和切片。
one_column = data.loc[:, "score"] if "score" in data.columns else data.loc[:, "city"]
many_columns = data.loc[:, ["name", "score"]] if "name" in data.columns else data.loc[:, ["city", "amount"]]
first_row = data.iloc[0]
first_two_rows = data.iloc[:2, :]
print("\n===== 单列 Series =====")
print(one_column)
print("\n===== 多列 DataFrame =====")
print(many_columns)
print("\n===== iloc[0] 单行 =====")
print(first_row)
print("\n===== iloc[:2, :] 前两行 =====")
print(first_two_rows)

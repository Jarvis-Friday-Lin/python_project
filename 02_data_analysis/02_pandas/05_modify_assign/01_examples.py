"""案例驱动示例：新增、修改与删除列"""

# 案例任务：
# 订单只有 price 和 quantity，需要增加 amount、折扣金额和等级。

# ===== 第一步：先用已经学过的基础语法解决案例 =====
# 任务已经明确，接下来先用列表、字典、循环和算术运算完成它。
# 先看整体路线：
# 第 1 步：先写出业务公式，明确金额单位和折扣口径。
# 第 2 步：通过新列赋值构造 amount，不修改原始 price 和 quantity。
# 第 3 步：用 loc 按条件填写等级，观察缺省行如何处理。
# 第 4 步：抽查一笔订单，用手算结果验证派生列。
# 顺序不能随意交换：先准备并理解输入，才能进行后续转换、分析和检查。

rows = [{"price": 100, "quantity": 2}, {"price": 50, "quantity": 1}]
for row in rows:
    row["amount"] = row["price"] * row["quantity"]
    row["level"] = "高" if row["amount"] >= 100 else "普通"
print("逐行新增字段：", rows)

# 对不用 Pandas 方案的评价：
# 上面的对照代码可以得到结果，但它把很多工作留给我们自己：也可以逐行循环计算并 append 字典；但速度慢、代码冗长且容易改错原数据。列运算和 loc 是向量化、可审计的表达。所以我们自然会问：有没有一种现成的数据对象，能把这些重复工作统一起来？有，Pandas 的“新增、修改与删除列”正是为这类表格问题准备的。接下来先用最小步骤试用它，每一步都看清楚输入、输出和为什么要继续下一步。

# ===== 第二步：使用 Pandas 的实现 =====
# 具体函数的入参、关键字参数和返回值，放在每个调用的上一行或下一行说明。
# 进入代码前先确认：本节是在处理哪种表格对象？核心方法要解决什么问题？输入是什么，返回结果的形状会怎样变化？
# 本节是在处理哪种表格对象？主要处理带行索引和列名的 DataFrame，部分方法会先取出其中一列 Series。
# 核心方法要解决什么问题？解决“新增、修改与删除列”这一类表格分析任务：以显式赋值或 assign 构造派生字段，并正确删除数据。
# 输入是什么，返回结果的形状会怎样变化？输入是案例中的原始表格；主要方法的参数和返回结果如下：给 data[列名] 赋值可以新增或覆盖整列，右侧可为标量或等长 Series；loc[行条件, 列名] 只更新指定行列，返回赋值后的表需要再次检查。
# 第 1 步：先写出业务公式，明确金额单位和折扣口径。
# 为什么：先写公式，是为了让派生字段有明确业务口径，避免把代码结果误当成正确结果。
# 调用提示：给 data[列名] 赋值可以新增或覆盖整列，右侧可为标量或等长 Series；loc[行条件, 列名] 只更新指定行列，返回赋值后的表需要再次检查。
import pandas as pd
data = pd.DataFrame({"price": [10, 20], "quantity": [3, 2]})
# 用列名赋值会新增 amount；右侧是逐行相乘得到的 Series，长度与 data 行数一致。
data["amount"] = data["price"] * data["quantity"]
# loc[行条件, 列名] 只给满足条件的行写入 level，其余行暂时保持缺失。
data.loc[data["amount"] >= 40, "level"] = "高"
# fillna(value) 用 value 填补缺失等级，返回新 Series，需要重新赋回原列。
data["level"] = data["level"].fillna("普通")
print('\n===== data.to_markdown(index=False) =====')
print(data.to_markdown(index=False))

# 新增和修改列的常用变体：直接赋值、assign、条件赋值和删除列。
data_copy = data.assign(total=data["price"] * data["quantity"])
print("\n===== assign 新增列 =====")
print(data_copy)
data_copy.loc[data_copy["total"] >= 100, "tag"] = "高"
data_copy["tag"] = data_copy["tag"].fillna("普通")
print("\n===== loc 条件修改 =====")
print(data_copy)
remaining = data_copy.drop(columns=["tag"])
print("\n===== drop(columns=...) 删除列 =====")
print(remaining)

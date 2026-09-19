"""案例驱动示例：merge、join 与 concat"""

# 案例任务：
# 把订单表的 customer_id 与客户表匹配，并合并两个月订单。

# ===== 第一步：先用已经学过的基础语法解决案例 =====
# 任务已经明确，接下来先用列表、字典、循环和算术运算完成它。
# 先看整体路线：
# 第 1 步：先检查两张表连接键的类型和唯一性。
# 第 2 步：使用 left merge 保留全部订单，再检查未匹配客户。
# 第 3 步：使用 concat 沿行拼接结构相同的月份表。
# 第 4 步：比较连接前后行数，排查意外重复和丢失。
# 顺序不能随意交换：先准备并理解输入，才能进行后续转换、分析和检查。

orders = [{"customer_id": 1, "amount": 100}, {"customer_id": 2, "amount": 200}]
customers = [{"customer_id": 1, "name": "甲"}, {"customer_id": 2, "name": "乙"}]
customer_map = {row["customer_id"]: row for row in customers}
merged = [{**order, **customer_map.get(order["customer_id"], {})} for order in orders]
print("字典关联：", merged)
print("列表拼接：", orders + orders)

# 对不用 Pandas 方案的评价：
# 上面的对照代码可以得到结果，但它把很多工作留给我们自己：也可以写嵌套循环查找客户或手工复制文件；但复杂度高且容易重复。merge/concat 使用明确连接语义，并可用 validate 检查关系。所以我们自然会问：有没有一种现成的数据对象，能把这些重复工作统一起来？有，Pandas 的“merge、join 与 concat”正是为这类表格问题准备的。接下来先用最小步骤试用它，每一步都看清楚输入、输出和为什么要继续下一步。

# ===== 第二步：使用 Pandas 的实现 =====
# 具体函数的入参、关键字参数和返回值，放在每个调用的上一行或下一行说明。
# 进入代码前先确认：本节是在处理哪种表格对象？核心方法要解决什么问题？输入是什么，返回结果的形状会怎样变化？
# 本节是在处理哪种表格对象？主要处理带行索引和列名的 DataFrame，部分方法会先取出其中一列 Series。
# 核心方法要解决什么问题？解决“merge、join 与 concat”这一类表格分析任务：根据键横向关联表格或沿轴拼接同构数据。
# 输入是什么，返回结果的形状会怎样变化？输入是案例中的原始表格；主要方法的参数和返回结果如下：merge(right, on=..., how=..., indicator=...) 把 right 表按连接键合并，how 决定保留哪边记录，indicator 增加匹配状态；concat(objs, ignore_index=True) 沿轴拼接表列表，ignore_index 重建行号。
# 第 1 步：先检查两张表连接键的类型和唯一性。
# 为什么：先检查键，是为了避免类型不同导致全部匹配失败，或键不唯一导致行数意外膨胀。
# 调用提示：merge(right, on=..., how=..., indicator=...) 把 right 表按连接键合并，how 决定保留哪边记录，indicator 增加匹配状态；concat(objs, ignore_index=True) 沿轴拼接表列表，ignore_index 重建行号。
import pandas as pd
orders = pd.DataFrame({"customer_id": [1, 2], "amount": [100, 200]})
customers = pd.DataFrame({"customer_id": [1, 2], "name": ["甲", "乙"]})
# merge 按 customer_id 连接两张表；how="left" 保留全部订单，validate 检查连接关系。
print('\n===== orders.merge(customers, on="customer_id", how="left", validate="many_to_one").to_markdown(index=False) =====')
print(orders.merge(customers, on="customer_id", how="left", validate="many_to_one").to_markdown(index=False))
# concat 沿行方向拼接表；ignore_index=True 重新生成连续索引。
print('\n===== pd.concat([orders, orders], ignore_index=True).to_markdown(index=False) =====')
print(pd.concat([orders, orders], ignore_index=True).to_markdown(index=False))

# 表连接的常用变体：inner、left、right、outer，以及按行和按列拼接。
print("\n===== inner merge =====")
print(orders.merge(customers, on="customer_id", how="inner"))
print("\n===== outer merge + indicator =====")
print(orders.merge(customers, on="customer_id", how="outer", indicator=True))
print("\n===== concat 按行 =====")
print(pd.concat([orders, orders], axis=0, ignore_index=True))
print("\n===== concat 按列 =====")
print(pd.concat([orders.reset_index(drop=True), customers[["name"]]], axis=1))

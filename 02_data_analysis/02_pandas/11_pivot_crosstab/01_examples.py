"""案例驱动示例：透视表与交叉表"""

# 案例任务：
# 制作城市×商品类别销售额汇报矩阵。

# ===== 第一步：先用已经学过的基础语法解决案例 =====
# 任务已经明确，接下来先用列表、字典、循环和算术运算完成它。
# 先看整体路线：
# 第 1 步：确认行变量、列变量、数值变量和聚合方式。
# 第 2 步：使用 pivot_table 把长表重塑成矩阵。
# 第 3 步：用 crosstab 另算订单数量，比较金额和数量的区别。
# 第 4 步：检查空白组合是没有数据还是被填成了 0。
# 顺序不能随意交换：先准备并理解输入，才能进行后续转换、分析和检查。

rows = [{"city": "上海", "product": "A", "amount": 100}, {"city": "上海", "product": "B", "amount": 200}]
pivot = {}
for row in rows:
    pivot.setdefault(row["city"], {})
    pivot[row["city"]][row["product"]] = pivot[row["city"]].get(row["product"], 0) + row["amount"]
print("嵌套字典透视：", pivot)

# 对不用 Pandas 方案的评价：
# 上面的对照代码可以得到结果，但它把很多工作留给我们自己：也可以手工创建二维字典；但要自己补齐组合、聚合和排序。pivot_table/crosstab 直接表达表格重塑意图，便于复核。所以我们自然会问：有没有一种现成的数据对象，能把这些重复工作统一起来？有，Pandas 的“透视表与交叉表”正是为这类表格问题准备的。接下来先用最小步骤试用它，每一步都看清楚输入、输出和为什么要继续下一步。

# ===== 第二步：使用 Pandas 的实现 =====
# 具体函数的入参、关键字参数和返回值，放在每个调用的上一行或下一行说明。
# 进入代码前先确认：本节是在处理哪种表格对象？核心方法要解决什么问题？输入是什么，返回结果的形状会怎样变化？
# 本节是在处理哪种表格对象？主要处理带行索引和列名的 DataFrame，部分方法会先取出其中一列 Series。
# 核心方法要解决什么问题？解决“透视表与交叉表”这一类表格分析任务：把长表重塑为汇总矩阵，比较分类变量关系。
# 输入是什么，返回结果的形状会怎样变化？输入是案例中的原始表格；主要方法的参数和返回结果如下：pivot_table(data, values=..., index=..., columns=..., aggfunc=..., fill_value=...) 把长表重塑为汇总矩阵；values 是要统计的值，index/columns 定义行列维度，aggfunc 定义聚合方法。
# 第 1 步：确认行变量、列变量、数值变量和聚合方式。
# 为什么：先确定行、列、值和聚合方式，是因为透视表的每个单元格都必须有明确统计口径。
# 调用提示：pivot_table(data, values=..., index=..., columns=..., aggfunc=..., fill_value=...) 把长表重塑为汇总矩阵；values 是要统计的值，index/columns 定义行列维度，aggfunc 定义聚合方法。
import pandas as pd
data = pd.DataFrame({"city": ["上海", "上海", "北京"], "product": ["A", "B", "A"], "amount": [100, 200, 150]})
# pivot_table 按 index/columns 重塑表格，values 是要汇总的列，aggfunc="sum" 指定求和。
print('\n===== pd.pivot_table(data, values="amount", index="city", columns="product", aggfunc="sum", fill_value=0).to_markdown() =====')
print(pd.pivot_table(data, values="amount", index="city", columns="product", aggfunc="sum", fill_value=0).to_markdown())
# crosstab 统计两个分类字段的频数，这里回答“每个城市有多少种商品记录”。
print('\n===== pd.crosstab(data["city"], data["product"]).to_markdown() =====')
print(pd.crosstab(data["city"], data["product"]).to_markdown())

# 重塑表格的常用变体：pivot_table、crosstab、margins 和 melt。
print("\n===== pivot_table 多种聚合 =====")
print(pd.pivot_table(data, values="amount", index="city", columns="product", aggfunc=["sum", "mean"], fill_value=0))
print("\n===== crosstab normalize =====")
print(pd.crosstab(data["city"], data["product"], normalize="index"))
print("\n===== melt 宽表转长表 =====")
wide = pd.DataFrame({"city": ["上海", "北京"], "A": [100, 150], "B": [200, 80]})
print(wide.melt(id_vars="city", var_name="product", value_name="amount"))

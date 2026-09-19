"""案例驱动示例：条件筛选与 query"""

# 案例任务：
# 运营人员要找出上海或北京、数量至少 2 且单价大于 100 的订单。

# ===== 第一步：先用已经学过的基础语法解决案例 =====
# 任务已经明确，接下来先用列表、字典、循环和算术运算完成它。
# 先看整体路线：
# 第 1 步：把自然语言拆成三个独立的布尔条件。
# 第 2 步：分别打印每个条件，确认每一行得到 True 或 False。
# 第 3 步：使用括号和位运算符组合条件，再与 query 写法对照。
# 第 4 步：检查结果为空和条件边界值时的表现。
# 顺序不能随意交换：先准备并理解输入，才能进行后续转换、分析和检查。

rows = [
    {"city": "上海", "quantity": 2, "price": 399},
    {"city": "北京", "quantity": 1, "price": 899},
]
selected = [row for row in rows if row["city"] in {"上海", "北京"} and row["quantity"] >= 2 and row["price"] > 100]
print("列表多条件筛选：", selected)

# 对不用 Pandas 方案的评价：
# 上面的对照代码可以得到结果，但它把很多工作留给我们自己：也可以用 for 循环和 if 拼出新列表；但难以组合复杂条件且丢失列标签。Pandas 掩码/query 能保留表结构并让条件可检查。所以我们自然会问：有没有一种现成的数据对象，能把这些重复工作统一起来？有，Pandas 的“条件筛选与 query”正是为这类表格问题准备的。接下来先用最小步骤试用它，每一步都看清楚输入、输出和为什么要继续下一步。

# ===== 第二步：使用 Pandas 的实现 =====
# 具体函数的入参、关键字参数和返回值，放在每个调用的上一行或下一行说明。
# 进入代码前先确认：本节是在处理哪种表格对象？核心方法要解决什么问题？输入是什么，返回结果的形状会怎样变化？
# 本节是在处理哪种表格对象？主要处理带行索引和列名的 DataFrame，部分方法会先取出其中一列 Series。
# 核心方法要解决什么问题？解决“条件筛选与 query”这一类表格分析任务：组合多个条件，并处理字符串和集合成员判断。
# 输入是什么，返回结果的形状会怎样变化？输入是案例中的原始表格；主要方法的参数和返回结果如下：isin(values) 判断每行值是否属于 values；query(expr) 接收条件字符串并返回筛选后的 DataFrame。多个布尔 Series 要用括号配合 &、|、~，因为它们是逐行运算。
# 第 1 步：把自然语言拆成三个独立的布尔条件。
# 为什么：先拆成独立条件，是为了让每个条件都能单独检查，避免一条长表达式隐藏错误。
# 调用提示：isin(values) 判断每行值是否属于 values；query(expr) 接收条件字符串并返回筛选后的 DataFrame。多个布尔 Series 要用括号配合 &、|、~，因为它们是逐行运算。
import pandas as pd
data = pd.DataFrame({"city": ["上海", "北京", "上海"], "amount": [500, 1200, 1800]})
# 先把条件拆开：每个比较表达式都会生成一列 True/False，便于单独检查。
is_shanghai = data["city"] == "上海"
is_expensive = data["amount"] >= 1000
# & 表示逐行“并且”；两侧条件必须分别加括号，不能写 Python 的 and。
selected_and = data[is_shanghai & is_expensive]
print('\n===== selected_and.to_markdown(index=False) =====')
print(selected_and.to_markdown(index=False))
# | 表示逐行“或者”；~ 表示逐行取反，可以组合出“上海或金额达标”“不是上海”等条件。
selected_or = data[(data["city"] == "上海") | (data["amount"] >= 1000)]
selected_not = data[~(data["city"] == "上海")]
print('\n===== selected_or.to_markdown(index=False) =====')
print(selected_or.to_markdown(index=False))
print('\n===== selected_not.to_markdown(index=False) =====')
print(selected_not.to_markdown(index=False))
# isin(values) 判断每行是否属于 values 列表，适合“城市在多个候选值中”的场景。
selected_cities = data[data["city"].isin(["上海", "北京"])]
print('\n===== selected_cities.to_markdown(index=False) =====')
print(selected_cities.to_markdown(index=False))
# between(left, right, inclusive=...) 判断区间；inclusive="both" 表示包含两端。
selected_range = data[data["amount"].between(500, 1500, inclusive="both")]
print('\n===== selected_range.to_markdown(index=False) =====')
print(selected_range.to_markdown(index=False))
# query 接收字符串条件，列名可以直接写在字符串中；适合条件较长时提高可读性。
selected_query = data.query("city == '上海' and amount >= 1000")
print('\n===== selected_query.to_markdown(index=False) =====')
print(selected_query.to_markdown(index=False))

# 条件筛选的常用变体：单条件、多个条件、集合、区间和缺失值。
print("\n===== 单条件 =====")
print(data[data["amount"] >= 1000].to_markdown(index=False))
print("\n===== isin 集合 =====")
print(data[data["city"].isin(["上海", "北京"])].to_markdown(index=False))
print("\n===== between 区间 =====")
print(data[data["amount"].between(500, 1500)].to_markdown(index=False))
print("\n===== isna / notna =====")
print(data[data["amount"].notna()].to_markdown(index=False))

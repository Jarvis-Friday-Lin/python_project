"""案例驱动示例：map、apply 与 transform"""

# 案例任务：
# 计算每笔订单占所在城市总销售额的比例。

# ===== 第一步：先用已经学过的基础语法解决案例 =====
# 任务已经明确，接下来先用列表、字典、循环和算术运算完成它。
# 先看整体路线：
# 第 1 步：先按城市计算总额，再思考如何把城市结果对齐回每一行。
# 第 2 步：用 transform 生成与原表等长的城市总额列。
# 第 3 步：相除得到比例，并按城市检查比例之和。
# 第 4 步：说明为什么这里不能随意用 apply 替代 transform。
# 顺序不能随意交换：先准备并理解输入，才能进行后续转换、分析和检查。

rows = [{"group": "A", "score": 80}, {"group": "A", "score": 100}, {"group": "B", "score": 70}]
totals = {}
for row in rows:
    totals[row["group"]] = totals.get(row["group"], 0) + row["score"]
for row in rows:
    row["ratio"] = row["score"] / totals[row["group"]]
print("逐行回填比例：", rows)

# 对不用 Pandas 方案的评价：
# 上面的对照代码可以得到结果，但它把很多工作留给我们自己：也可以循环计算每组平均数再逐行回填；但容易发生索引错位。transform 保持原长度，适合把组级指标安全返回明细表。所以我们自然会问：有没有一种现成的数据对象，能把这些重复工作统一起来？有，Pandas 的“map、apply 与 transform”正是为这类表格问题准备的。接下来先用最小步骤试用它，每一步都看清楚输入、输出和为什么要继续下一步。

# ===== 第二步：使用 Pandas 的实现 =====
# 具体函数的入参、关键字参数和返回值，放在每个调用的上一行或下一行说明。
# 进入代码前先确认：本节是在处理哪种表格对象？核心方法要解决什么问题？输入是什么，返回结果的形状会怎样变化？
# 本节是在处理哪种表格对象？主要处理带行索引和列名的 DataFrame，部分方法会先取出其中一列 Series。
# 核心方法要解决什么问题？解决“map、apply 与 transform”这一类表格分析任务：根据输入输出形状选择自定义转换方式，优先使用向量化操作。
# 输入是什么，返回结果的形状会怎样变化？输入是案例中的原始表格；主要方法的参数和返回结果如下：apply(func) 可按行或列执行自定义函数，返回形状取决于 func；transform(func) 也接收规则，但保证结果与原表等长，适合把分组指标对齐回明细行。
# 第 1 步：先按城市计算总额，再思考如何把城市结果对齐回每一行。
# 为什么：先算每组总量，是因为每笔订单的比例分母取决于它所在的城市或组别。
# 调用提示：apply(func) 可按行或列执行自定义函数，返回形状取决于 func；transform(func) 也接收规则，但保证结果与原表等长，适合把分组指标对齐回明细行。
import pandas as pd
data = pd.DataFrame({"group": ["A", "A", "B"], "score": [80, 100, 70]})
# transform("mean") 计算组均值，但返回长度与原表相同，所以可以安全赋回新列。
data["group_mean"] = data.groupby("group")["score"].transform("mean")
# 逐行相减得到每条记录相对本组均值的差异。
data["difference"] = data["score"] - data["group_mean"]
print('\n===== data.to_markdown(index=False) =====')
print(data.to_markdown(index=False))

# 自定义处理的常用变体：map 逐元素、apply 按行/列、transform 保持原长度。
data["level"] = data["score"].map(lambda value: "优秀" if value >= 90 else "普通")
print("\n===== Series.map =====")
print(data)
print("\n===== DataFrame.apply(axis=1) =====")
print(data.apply(lambda row: row["score"] - row["group_mean"], axis=1))
print("\n===== groupby.transform =====")
print(data.groupby("group")["score"].transform("mean"))

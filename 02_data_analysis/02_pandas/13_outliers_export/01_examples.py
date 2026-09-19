"""案例驱动示例：异常值处理与导出"""

# 案例任务：
# 标记异常金额，调查原因后把结果交付给同事。

# ===== 第一步：先用已经学过的基础语法解决案例 =====
# 任务已经明确，接下来先用列表、字典、循环和算术运算完成它。
# 先看整体路线：
# 第 1 步：先计算金额的 Q1、Q3 和 IQR，不急着删除记录。
# 第 2 步：生成 is_outlier 布尔列，保留原金额方便复核。
# 第 3 步：查看异常订单的商品、城市和日期，区分错误与真实大单。
# 第 4 步：把带标记的结果导出到 outputs，原始 datasets 文件不动。
# 顺序不能随意交换：先准备并理解输入，才能进行后续转换、分析和检查。

values = [10, 11, 12, 13, 100]
ordered = sorted(values)
q1, q3 = ordered[1], ordered[3]
iqr = q3 - q1
outliers = [value for value in values if value > q3 + 1.5 * iqr]
print("手工标记异常值：", outliers)

# 对不用 Pandas 方案的评价：
# 上面的对照代码可以得到结果，但它把很多工作留给我们自己：也可以凭经验写固定阈值或直接删除最大值；但不可迁移且可能误删真实大单。IQR 标记加业务复核更稳健，导出新文件更安全。所以我们自然会问：有没有一种现成的数据对象，能把这些重复工作统一起来？有，Pandas 的“异常值处理与导出”正是为这类表格问题准备的。接下来先用最小步骤试用它，每一步都看清楚输入、输出和为什么要继续下一步。

# ===== 第二步：使用 Pandas 的实现 =====
# 具体函数的入参、关键字参数和返回值，放在每个调用的上一行或下一行说明。
# 进入代码前先确认：本节是在处理哪种表格对象？核心方法要解决什么问题？输入是什么，返回结果的形状会怎样变化？
# 本节是在处理哪种表格对象？主要处理带行索引和列名的 DataFrame，部分方法会先取出其中一列 Series。
# 核心方法要解决什么问题？解决“异常值处理与导出”这一类表格分析任务：用 IQR 等规则标记异常值，并保存清洗结果而不覆盖原始数据。
# 输入是什么，返回结果的形状会怎样变化？输入是案例中的原始表格；主要方法的参数和返回结果如下：quantile(q) 返回 q 位置的分位数，q 通常在 0 到 1 之间；to_csv(path, index=False) 把结果写到 path，index=False 表示不把索引另写成一列。
# 第 1 步：先计算金额的 Q1、Q3 和 IQR，不急着删除记录。
# 为什么：先计算 IQR，是因为需要一个相对稳健、可解释的标记规则，而不是凭肉眼删除。
# 调用提示：quantile(q) 返回 q 位置的分位数，q 通常在 0 到 1 之间；to_csv(path, index=False) 把结果写到 path，index=False 表示不把索引另写成一列。
import pandas as pd
values = pd.Series([10, 11, 12, 13, 100])
# quantile([0.25, 0.75]) 一次取得 Q1、Q3；IQR 是两者之差。
q1, q3 = values.quantile([0.25, 0.75])
iqr = q3 - q1
# 布尔条件标记异常值；这里先标记，不直接删除，方便后续业务复核。
mask = (values < q1 - 1.5 * iqr) | (values > q3 + 1.5 * iqr)
result = pd.DataFrame({"value": values, "is_outlier": mask})
print('\n===== result.to_markdown(index=False) =====')
print(result.to_markdown(index=False))

# 异常值与导出的常用变体：上下界、布尔标记、clip 截断和不同导出格式。
lower = q1 - 1.5 * iqr
upper = q3 + 1.5 * iqr
print("\n===== IQR 上下界 =====")
print(lower, upper)
print("\n===== clip 截断极端值 =====")
print(values.clip(lower=lower, upper=upper))
print("\n===== to_csv 参数 =====")
print("to_csv(path, index=False) 会导出 CSV，index=False 不写索引列。")

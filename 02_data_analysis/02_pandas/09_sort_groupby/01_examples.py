"""案例驱动示例：排序、分组与聚合"""

# 案例任务：
# 制作各城市销售排名，包含订单数、总额、平均额和最大单笔。

# ===== 第一步：先用已经学过的基础语法解决案例 =====
# 任务已经明确，接下来先用列表、字典、循环和算术运算完成它。
# 先看整体路线：
# 第 1 步：先明确分组字段和每个指标的统计口径。
# 第 2 步：groupby 后使用 agg 一次计算多个指标。
# 第 3 步：按 total 降序排序，给结果增加排名或序号。
# 第 4 步：同时报告样本量，避免只看平均数造成误判。
# 顺序不能随意交换：先准备并理解输入，才能进行后续转换、分析和检查。

rows = [{"city": "上海", "amount": 100}, {"city": "上海", "amount": 300}, {"city": "北京", "amount": 200}]
groups = {}
for row in rows:
    groups.setdefault(row["city"], []).append(row["amount"])
summary = [{"city": city, "total": sum(values)} for city, values in groups.items()]
print("手工分组汇总：", sorted(summary, key=lambda row: row["total"], reverse=True))

# 对不用 Pandas 方案的评价：
# 上面的对照代码可以得到结果，但它把很多工作留给我们自己：也可以先把每个城市分成多个列表再循环统计；但指标增加后重复代码很多。groupby/agg 能统一定义多个指标并保持结果表结构。所以我们自然会问：有没有一种现成的数据对象，能把这些重复工作统一起来？有，Pandas 的“排序、分组与聚合”正是为这类表格问题准备的。接下来先用最小步骤试用它，每一步都看清楚输入、输出和为什么要继续下一步。

# ===== 第二步：使用 Pandas 的实现 =====
# 具体函数的入参、关键字参数和返回值，放在每个调用的上一行或下一行说明。
# 进入代码前先确认：本节是在处理哪种表格对象？核心方法要解决什么问题？输入是什么，返回结果的形状会怎样变化？
# 本节是在处理哪种表格对象？主要处理带行索引和列名的 DataFrame，部分方法会先取出其中一列 Series。
# 核心方法要解决什么问题？解决“排序、分组与聚合”这一类表格分析任务：使用 split-apply-combine 思路计算分组统计。
# 输入是什么，返回结果的形状会怎样变化？输入是案例中的原始表格；主要方法的参数和返回结果如下：groupby(by, as_index=False) 按 by 分组，as_index=False 让分组键保留为普通列；agg 用命名关键字定义每个输出指标，例如 total=('amount','sum')，返回汇总 DataFrame。
# 第 1 步：先明确分组字段和每个指标的统计口径。
# 为什么：先定义指标，是为了避免把订单数、金额总和和平均金额混成一个没有意义的数字。
# 调用提示：groupby(by, as_index=False) 按 by 分组，as_index=False 让分组键保留为普通列；agg 用命名关键字定义每个输出指标，例如 total=('amount','sum')，返回汇总 DataFrame。
import pandas as pd
data = pd.DataFrame({"city": ["上海", "北京", "上海"], "amount": [100, 200, 300]})
# groupby("city") 按城市分组；as_index=False 让 city 继续作为普通列保留。
summary = data.groupby("city", as_index=False).agg(
    # agg 中每个命名参数定义一个输出列：原列 amount 使用 size/sum/mean 计算不同指标。
    orders=("amount", "size"),
    total=("amount", "sum"),
    average=("amount", "mean"),
)
print('\n===== summary.sort_values("total", ascending=False).to_markdown(index=False) =====')
print(summary.sort_values("total", ascending=False).to_markdown(index=False))

# 排序和分组的常用变体：升降序、取前几名、计数和多指标聚合。
print("\n===== sort_values 多列排序 =====")
print(data.sort_values(["amount", "city"], ascending=[False, True]))
print("\n===== nlargest 取前几名 =====")
print(data.nlargest(2, "amount"))
print("\n===== groupby.size 计数 =====")
print(data.groupby("city").size())
print("\n===== groupby.agg 多指标 =====")
print(data.groupby("city", as_index=False).agg(total=("amount", "sum"), average=("amount", "mean")))

"""案例驱动示例：日期时间处理"""

# 案例任务：
# 统计 sales.csv 每月订单数和销售额。

# ===== 第一步：先用已经学过的基础语法解决案例 =====
# 任务已经明确，接下来先用列表、字典、循环和算术运算完成它。
# 先看整体路线：
# 第 1 步：把 date 从字符串解析为 datetime，并检查无效日期。
# 第 2 步：用 dt 访问器提取月份或生成 Period。
# 第 3 步：按 month 分组并聚合订单数、销售额。
# 第 4 步：按时间顺序排序，确认月份没有按字符串字典序排列。
# 顺序不能随意交换：先准备并理解输入，才能进行后续转换、分析和检查。

from datetime import datetime
dates = [datetime.strptime(value, "%Y-%m-%d") for value in ["2026-01-03", "2026-02-14"]]
months = {}
for value in dates:
    key = value.strftime("%Y-%m")
    months[key] = months.get(key, 0) + 1
print("手工按月计数：", months)

# 对不用 Pandas 方案的评价：
# 上面的对照代码可以得到结果，但它把很多工作留给我们自己：也可以切字符串的前 7 位得到月份；但遇到格式变化、无效日期和时区就会失败。datetime/dt 提供可靠的时间运算和时间粒度。所以我们自然会问：有没有一种现成的数据对象，能把这些重复工作统一起来？有，Pandas 的“日期时间处理”正是为这类表格问题准备的。接下来先用最小步骤试用它，每一步都看清楚输入、输出和为什么要继续下一步。

# ===== 第二步：使用 Pandas 的实现 =====
# 具体函数的入参、关键字参数和返回值，放在每个调用的上一行或下一行说明。
# 进入代码前先确认：本节是在处理哪种表格对象？核心方法要解决什么问题？输入是什么，返回结果的形状会怎样变化？
# 本节是在处理哪种表格对象？主要处理带行索引和列名的 DataFrame，部分方法会先取出其中一列 Series。
# 核心方法要解决什么问题？解决“日期时间处理”这一类表格分析任务：解析日期、提取组成部分、计算时间差并按时间索引。
# 输入是什么，返回结果的形状会怎样变化？输入是案例中的原始表格；主要方法的参数和返回结果如下：to_datetime(arg, errors=...) 把 arg 转为日期时间；dt.to_period(freq) 按 freq='M' 提取月份周期；groupby(by) 按 by 指定的字段分组。日期解析失败时要先决定是否转成 NaT。
# 第 1 步：把 date 从字符串解析为 datetime，并检查无效日期。
# 为什么：先统一日期类型，是因为字符串排序可能按字符顺序而不是时间顺序，日期加减也无法可靠进行。
# 调用提示：to_datetime(arg, errors=...) 把 arg 转为日期时间；dt.to_period(freq) 按 freq='M' 提取月份周期；groupby(by) 按 by 指定的字段分组。日期解析失败时要先决定是否转成 NaT。
import pandas as pd
data = pd.DataFrame({"date": ["2026-01-01", "2026-02-15"]})
# to_datetime 把字符串解析为日期时间，返回可使用 dt 访问器的 Series。
data["date"] = pd.to_datetime(data["date"])
# dt.to_period("M") 把日期转换为月份周期，便于按月统计。
data["month"] = data["date"].dt.to_period("M")
# 两个日期相减得到 Timedelta，再用 dt.days 取出天数整数。
data["days_from_start"] = (data["date"] - data["date"].min()).dt.days
print('\n===== data.to_markdown(index=False) =====')
print(data.to_markdown(index=False))

# 日期时间的常用变体：解析、提取组成部分、格式化和日期差。
print("\n===== dt.year / dt.month / dt.day =====")
print(data["date"].dt.year)
print(data["date"].dt.month)
print(data["date"].dt.day)
print("\n===== dt.strftime() =====")
print(data["date"].dt.strftime("%Y-%m"))
print("\n===== 日期范围筛选 =====")
print(data[data["date"].between("2026-01-01", "2026-02-28")])

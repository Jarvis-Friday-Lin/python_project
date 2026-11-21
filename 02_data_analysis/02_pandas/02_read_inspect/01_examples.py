"""案例驱动示例：读取与观察数据"""

# 案例任务：
# 接手 sales.csv，向主管汇报这份数据能否用于销售分析。

# ===== 第一步：先用已经学过的基础语法解决案例 =====
# 任务已经明确，接下来先用列表、字典、循环和算术运算完成它。
# 先看整体路线：
# 第 1 步：使用 read_csv 把文件加载为 DataFrame，先不做任何清洗。
# 第 2 步：用 head、shape、columns 和 info 检查结构，再用 isna 统计空值。
# 第 3 步：用 describe 查看数值字段范围，判断金额、数量是否被正确识别。
# 第 4 步：把发现的问题写成检查清单，决定下一节要清洗什么。
# 顺序不能随意交换：先准备并理解输入，才能进行后续转换、分析和检查。

import csv
from pathlib import Path
path = Path(__file__).resolve().parents[2] / "datasets" / "sales.csv"

print(path)

with path.open(encoding="utf-8", newline="") as file:
    rows = list(csv.DictReader(file))
print("csv 行数：", len(rows))
print("csv 列名：", list(rows[0]) if rows else [])

# 对不用 Pandas 方案的评价：
# 上面的对照代码可以得到结果，但它把很多工作留给我们自己：也可以用 csv 模块逐行读取或手工打开 Excel；但需要自己处理类型、缺失和汇总。Pandas 能一次得到结构检查、统计摘要和后续分析对象。所以我们自然会问：有没有一种现成的数据对象，能把这些重复工作统一起来？有，Pandas 的“读取与观察数据”正是为这类表格问题准备的。接下来先用最小步骤试用它，每一步都看清楚输入、输出和为什么要继续下一步。

# ===== 第二步：使用 Pandas 的实现 =====
# 具体函数的入参、关键字参数和返回值，放在每个调用的上一行或下一行说明。
# 进入代码前先确认：本节是在处理哪种表格对象？核心方法要解决什么问题？输入是什么，返回结果的形状会怎样变化？
# 本节是在处理哪种表格对象？主要处理带行索引和列名的 DataFrame，部分方法会先取出其中一列 Series。
# 核心方法要解决什么问题？解决“读取与观察数据”这一类表格分析任务：读取 CSV/Excel 后先检查形状、列、类型、样例和统计摘要。
# 输入是什么，返回结果的形状会怎样变化？输入是案例中的原始表格；主要方法的参数和返回结果如下：read_csv(path, ...) 用来把 CSV 文件读成 DataFrame，path 是文件路径；head(n) 返回前 n 行，info() 汇报列名、非空数量和 dtype，describe(include=...) 返回统计摘要。它们都用于先认识数据，而不是直接开始计算。
# 第 1 步：使用 read_csv 把文件加载为 DataFrame，先不做任何清洗。
# 为什么：先读取文件，是因为分析对象还在磁盘上，内存中没有 DataFrame 就无法使用 Pandas 的检查能力。
# 调用提示：read_csv(path, ...) 用来把 CSV 文件读成 DataFrame，path 是文件路径；head(n) 返回前 n 行，info() 汇报列名、非空数量和 dtype，describe(include=...) 返回统计摘要。它们都用于先认识数据，而不是直接开始计算。
from pathlib import Path
import pandas as pd
path = Path(__file__).resolve().parents[2] / "datasets" / "sales.csv"
data = pd.read_csv(path)
print('\n===== data.head().to_markdown(index=False) =====')
print(data.head().to_markdown(index=False))
# info() 会直接把列名、非空数量和 dtype 打印出来；它主要用于检查结构，返回值本身是 None。
print('\n===== data.info() =====')
data.info()
# describe() 默认偏重数值列；include="all" 才会同时概览 price、quantity 等数值列和 city、product 等文本列。
# count：非缺失值数量；unique：不同值数量；top：出现次数最多的值；freq：top 出现的次数。
# mean/std/min/25%/50%/75%/max：数值列的平均值、标准差、最小值、四分位数、中位数、四分之三位数和最大值。
# 文本列在这些数值统计位置会显示 NaN，这是“该统计不适用于文本”的意思，不是原数据凭空多了缺失。
print('\n===== data.describe(include="all") =====')
print(data.describe(include="all"))

# 常用读取与观察方式：同一个任务不只有一种 API。
# read_csv 的 usecols 只读指定列，nrows 只读前几行，parse_dates 尝试把日期列直接解析为日期。
sample = pd.read_csv(path, usecols=["order_id", "city", "price"], nrows=3)
print("\n===== pd.read_csv(usecols=..., nrows=...) =====")
print(sample)
# head(n) 看开头，tail(n) 看结尾，sample(n, random_state=...) 随机抽样且可复现。
print("\n===== data.tail(2) =====")
print(data.tail(2))
print("\n===== data.sample(2, random_state=42) =====")
print(data.sample(2, random_state=42))
# shape、columns、dtypes、isna().sum() 分别回答大小、字段、类型和缺失数量。
print("\n===== data.shape / data.columns / data.dtypes / data.isna().sum() =====")
print(data.shape)
print(data.columns.tolist())
print(data.dtypes)
print(data.isna().sum())

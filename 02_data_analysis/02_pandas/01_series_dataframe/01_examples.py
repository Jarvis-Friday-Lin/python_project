"""案例驱动示例：Series 与 DataFrame

阅读顺序：
1. 先运行“不用 Pandas”的代码，观察它怎样完成任务。
2. 阅读评价，理解这种写法的维护成本。
3. 再运行 Pandas 代码，比较对象、步骤和结果。
4. 最后修改一处输入，确认结论不是巧合。

"""
# Pandas 是什么：它是一个建立在 Python 之上的开源数据分析库。
# Python 本身提供列表、字典和循环；Pandas 在此基础上提供更适合表格数据的 Series、DataFrame 以及批量计算、筛选和清洗方法。
# 我们今天的教务处任务就是一个典型例子：数据有行、有列、有字段含义，还要重复进行统计和筛选。
# 先用基础语法完成一次，再观察为什么 Pandas 能让同类工作更清楚、更容易扩展。

# 案例任务：
# 教务处要找出 Python 成绩不低于 85 分的学生，并计算全班平均分。

# ===== 第一步：先用已经学过的基础语法解决案例 =====
# 任务已经明确，接下来先用列表、字典、循环和算术运算完成它。

# 先用已经学过的列表和字典保存案例数据：每个字典是一名学生的一行记录。
# 现在先不急着学习 Pandas，而是问：只靠基础语法，这个任务能不能完成？
# 先看整体路线：第 1 步取出成绩，第 2 步根据成绩计算平均分，第 3 步逐行筛选达标学生。
# 之所以按这个顺序，是因为后面的计算需要先有 scores，筛选则需要回到完整的 students 记录中。
students = [
    {"name": "小林", "class": "一班", "python": 95},
    {"name": "小周", "class": "一班", "python": 84},
    {"name": "小陈", "class": "二班", "python": 90},
    {"name": "小李", "class": "二班", "python": 75},
]
# 第 1 步：先取出所有 Python 成绩。
# 为什么：平均分只针对 python 这一列，字典不会自动把它变成一列，所以要自己按键名取值。
scores = [row["python"] for row in students]

# 第 2 步：把成绩相加，再除以人数，得到平均分。
# 为什么：这是我们在基础语法阶段已经学过的 sum 和 len；先完成任务，再观察代码代价。
average_score = sum(scores) / len(scores)
print("列表平均分：", average_score)

# 第 3 步：逐行判断成绩是否达到 85 分，并保留整条学生记录。
# 为什么：只保留分数会丢掉姓名和班级，所以筛选结果仍然应该是字典列表。
qualified = []
for row in students:
    if row["python"] >= 85:
        qualified.append(row)
print("列表筛选：", qualified)

# 对不用 Pandas 方案的评价：
# 上面的列表和字典代码确实能完成任务，但如果数据从 4 条变成 4 万条，你就得继续往列表里加记录；如果字段从 python 增加到 math、english，平均分、筛选和字段对应也要自己维护。这样代码会越来越长，也不容易扩展。有没有更好的办法？有。Pandas 里的 Series 专门表示带标签的一列数据，DataFrame 专门表示带列名的二维表。我们先用最小例子看看它们长什么样，再把它们放回当前成绩案例中。

# ===== 第二步：使用 Pandas 的实现 =====
# 具体函数的入参、关键字参数和返回值，放在每个调用的上一行或下一行说明。
# 进入代码前先确认：本节是在处理哪种表格对象？核心方法要解决什么问题？输入是什么，返回结果的形状会怎样变化？
# 本节是在处理哪种表格对象？主要处理一维 Series 和二维 DataFrame：Series 表示一列，DataFrame 表示完整表格。
# 核心方法要解决什么问题？解决带标签数据的选择、整列统计和完整记录筛选，减少列表、字典和循环的手工维护。
# 输入是什么，返回结果的形状会怎样变化？输入是一列成绩或多列学生记录；选择单列返回 Series，选择多列或筛选整行返回 DataFrame，mean() 返回一个数值。
import pandas as pd

# Series 像 Excel 的一列：每个值除了内容，还有一个 index 标签和可选的 name。
# DataFrame 像 Excel 的一张表：有 index 行标签、columns 列名和二维 values。
# 先理解这两个对象，后面才知道为什么一列适合统计、整张表适合筛选完整记录。

# 第 1 步：先把“一列成绩”变成 Series。
# 为什么：基础语法方案需要我们手工循环取 python；Series 可以把“成绩”和“学生标签”放在同一个对象里。
# pd.Series(data, index=..., name=...)：data 是位置参数，index/name 是关键字参数。
# data 是真正保存的值；index 为每个值提供标签；name 给这一列命名；返回值是 Series。
# data 和 index 长度必须一致，否则一个值无法对应一个标签。
scores_series = pd.Series([88, 95, 82], index=["甲", "乙", "丙"], name="成绩")
print("\n===== 观察 Series =====")
print("scores_series：")
print("\n===== Series 数据 =====")
print(scores_series)
print("\n===== 检查 Series 的组成 =====")
print("\n===== Series 类型 =====")
print("类型：", type(scores_series).__name__)
print("\n===== Series 索引 =====")
print("索引：", scores_series.index.tolist())
print("\n===== Series 名称 =====")
print("名称：", scores_series.name)

# 第 2 步：案例还要保留姓名、班级和多门成绩，所以一列不够，需要 DataFrame。
# 为什么：DataFrame(data=...) 接收字典时，键成为列名，列表成为列值；所有列表长度必须一致。
# data= 是关键字参数；省略名字也能运行，但显式写出更容易读懂。返回值是二维 DataFrame。

# 中文表格在不同终端中的宽度可能显示不齐；这两个全局选项只影响显示，不会改变数据本身。
pd.set_option("display.unicode.east_asian_width", True)
pd.set_option("display.unicode.ambiguous_as_wide", True)

students = pd.DataFrame(data={
    "name": ["小林", "小周", "小陈", "小李"],
    "class": ["一班", "一班", "二班", "二班"],
    "math": [92, 76, 85, 68],
    "python": [95, 84, 90, 75],
})
print("\n===== 观察 DataFrame =====")
print(students)

# to_markdown(index=False) 把 DataFrame 转成 Markdown 表格文本，方便复制到笔记或报告。
# index=False 是关键字参数，表示不把 Pandas 的行索引额外输出成一列。
# 本节优先使用 Markdown 格式观察表格；如果本机尚未安装 tabulate，再单独改成 print(students) 即可。
print("\n===== 使用 Markdown 格式观察 DataFrame =====")
print(students.to_markdown(index=False))

# shape 返回 (行数, 列数)，columns 返回列标签；先检查它们，是为了确认字段没有错位。
print("\n===== 检查 DataFrame 结构 =====")
print("形状：", students.shape)
print("\n===== DataFrame 列名 =====")
print("列名：", students.columns.tolist())

# 第 3 步：对比单层和双层方括号，理解返回对象不同。
# students["python"]：传入一个列名字符串，返回 Series，适合对一列求平均。
python_scores_series = students["python"]
print("\n===== 比较单层和双层方括号 =====")
print("单层选择类型：", type(python_scores_series).__name__)
# students[["python"]]：传入“列名列表”，返回仍是 DataFrame，适合保留二维表形状。
python_scores_frame = students[["python"]]
print("\n===== 双层方括号选择类型 =====")
print("双层选择类型：", type(python_scores_frame).__name__)

# mean() 用来求平均值；这里没有必填参数，返回一个数值。
# Series 已经知道这一列的全部值，所以不必再手写 sum(...) / len(...)。
average_score = python_scores_series.mean()
print("\n===== 计算平均分 =====")
print("全班 Python 平均分：", average_score)

# 第 4 步：根据成绩条件筛选，但保留整行信息。
# python_scores_series >= 85 会产生布尔 Series；每个 True/False 与原表的一行对齐。
# loc[行条件, 列选择] 按标签选择数据；只写一个条件时表示筛选行，返回 DataFrame。
qualified = students.loc[python_scores_series >= 85]
print("\n===== 筛选完整达标记录 =====")
print("Python 成绩不低于 85 分的学生：")
print("\n===== 达标学生表 =====")
print(qualified)

# 同一个筛选也可以写成 students[students["python"] >= 85]；loc 更明确地表达了“按标签筛选”。
qualified_short = students.loc[students["python"] >= 85, ["name", "python"]]
print("\n===== 筛选指定列 =====")
print("只保留姓名和 Python 成绩：")
print("\n===== 指定列结果 =====")
print(qualified_short)

# 最后手算 (95 + 84 + 90 + 75) / 4，验证平均分没有错位。
assert average_score == (95 + 84 + 90 + 75) / 4

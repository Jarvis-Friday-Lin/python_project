"""案例驱动示例：用基础语法完成一次成绩分析"""
# 基础准备/综合应用：为三份 PDF 的学习提供衔接。
# 任务：找出 Python 成绩不低于 85 分的学生，并算出平均分。
# 我们先确认列表、字典、条件、循环和推导式能否独立完成任务。这是后面比较工具的起点。
# 案例数据：
# | name | python |
# |---|---:|
# | 小林 | 95 |
# | 小周 | 84 |
# | 小陈 | 90 |
# | 小李 | 75 |
# 先看整体路线：
# 第 1 步：先用字典表示一名学生，列表保存全体学生。
# 第 2 步：遍历记录，同时累计总分和筛选学生。
# 第 3 步：再写成推导式，核对结果而不是只比较长短。

students = [{"name": "小林", "python": 95}, {"name": "小周", "python": 84},
            {"name": "小陈", "python": 90}, {"name": "小李", "python": 75}]
total = 0
selected = []
for row in students:
    # row 是一条字典记录；用键名取值，而不是按字段排列猜测位置。
    total += row["python"]
    if row["python"] >= 85:
        selected.append(row)
average = total / len(students)
print('\n===== average =====')
print(average)
print('\n===== selected =====')
print(selected)

# 循环已验证正确，下面才能理解推导式压缩了哪些重复步骤。
scores = [row["python"] for row in students]
print('\n===== sum(scores) / len(scores) =====')
print(sum(scores) / len(scores))
# >= 包含边界 85，> 则不包含；真实需求中的“不低于”不能随意替换。
assert average == 86
assert [row["name"] for row in selected] == ["小林", "小陈"]

# 学完先自己回答，再看下面的参考答案：
# 1. 这个知识点解决什么类型的问题？
# 2. 为什么当前案例需要它？
# 3. 每一步代码为什么要在此时出现？
# 4. 如果换一种做法，代价和风险是什么？

# 参考答案：
# 1. 按记录存储、遍历、累计与条件筛选。
# 2. 学生不仅有分数，还有姓名，所以用字典保留关联。
# 3. 先存数据，再累计筛选，最后知道总人数后才能计算平均分。
# 4. 推导式更短但复杂条件难读；多列统计继续手写会增加重复逻辑。

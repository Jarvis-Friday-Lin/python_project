"""案例驱动示例：Series 与 DataFrame"""
# Pandas 是什么：它是一个建立在 Python 之上的开源数据分析库。
# Python 本身提供列表、字典和循环；Pandas 在此基础上提供更适合表格数据的 Series、DataFrame 以及批量计算、筛选和清洗方法。
# 我们今天的教务处任务就是一个典型例子：数据有行、有列、有字段含义，还要重复进行统计和筛选。
# 先用基础语法完成一次，再观察为什么 Pandas 能让同类工作更清楚、更容易扩展。

# 案例任务：
# 教务处要找出 Python 成绩不低于 85 分的学生，并计算全班平均分。

# name	class	python
# 小林	一班	    95
# 小周	一班	    84
# 小陈	二班	    90
# 小李	二班	    75

# 用历史的手段，python基础语法如何解决

students = [
    {"name":"小林", "class":"一班", "python": 95},
    {"name":"小周", "class":"一班", "python": 84},
    {"name":"小陈", "class":"二班", "python": 90},
    {"name":"小李", "class":"二班", "python": 75},
]

# 代码语法糖，每个编程语言，除了我们普通学的语法，为了【简便写法】出了一些语法糖，row["python"] for row in students对语法糖写法
# 就是一种简便的写法，远离跟原本的写法一模一样
sources = [row["python"] for row in students]
avg = sum(sources) / len(sources)
print(avg)
# 等价于下面这3行代码
# sources = []
# for row in students:
#     # students是一个列表，我的row是这个列表中的一个元素，这个元素是什么类型？dict类型
#     # print(type(row))
#     sources.append(row["python"])

filters = []
for row in students:
    if row["python"] > 85:
        filters.append(row)

print(filters)

print("=================下面为pandas知识=========")
# Serise、DataFrame

import pandas as pd


print("=================Series=========")
sss = pd.Series(data=[95, 90, 88], index=["小林", "小周", "小李"], name = "python")
print(sss)
print(type(sss))
print(sss.index.tolist())
print(sss.name)

print("=================DataFrame=========")
ddd = pd.DataFrame(data = {
    "name" : ["小林", "小周", "小陈", "小李"],
    "class" : ["一班", "一班", "二班", "二班"],
    "python" : [95, 84, 90, 75]
})
# }, index=["a", "b", "c", "d"])
print(ddd)
print(ddd.shape)
print(type(ddd))
print(ddd.columns.tolist())

python_source = ddd["python"]
# 计算平均值的方法
print(python_source.mean())
filters = ddd.loc[python_source > 85]
print(filters)






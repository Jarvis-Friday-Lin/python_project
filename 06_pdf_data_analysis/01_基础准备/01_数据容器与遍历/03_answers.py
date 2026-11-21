"""参考答案：图书借阅记录的统计与催还"""
# 基础准备/综合应用：为三份 PDF 的学习提供衔接。
# 课件核心：为 NumPy 数组和 Pandas 记录表准备列表、字典、循环的前置知识。
# 扩展：本节均为前置补充，三份课件没有系统讲解基础容器。
# 案例数据（据此自行创建对象，不能照抄 examples 的数据）：
# | reader | borrowed |
# |---|---|
# | 林同学 | 2 |
# | 陈同学 | 5 |
# | 赵同学 | 0 |
# | 王同学 | 1 |
# 建议先做练习，再逐段对照下面的实现；assert 用于验证结果。

def summarize(records):
    total = sum(row['borrowed'] for row in records)
    return total, total / len(records) if records else None

records = [{'reader': '林同学', 'borrowed': 2}, {'reader': '陈同学', 'borrowed': 5},
           {'reader': '赵同学', 'borrowed': 0}, {'reader': '王同学', 'borrowed': 1}]
total, average = summarize(records)
reminders = [{'reader': row['reader'], 'return_books': row['borrowed'] - 2}
             for row in records if row['borrowed'] >= 3]
print('\n===== (total, average) =====')
print((total, average))
print('\n===== reminders =====')
print(reminders)
assert (total, average) == (8, 2)
assert reminders == [{'reader': '陈同学', 'return_books': 3}]
assert summarize([]) == (0, None)
# 空列表没有人数作为分母，因此人均值不存在；0 表示有读者但无人借阅。

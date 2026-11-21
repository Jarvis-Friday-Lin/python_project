"""参考答案：用基础语法完成一次成绩分析"""
# 基础准备/综合应用：为三份 PDF 的学习提供衔接。
# 建议先完成 02_exercises.py；下面的实现与该题数据、要求一一对应。

students = [{"name": "小林", "python": 95}, {"name": "小周", "python": 84},
            {"name": "小陈", "python": 90}, {"name": "小李", "python": 75}]
assert sum(row["python"] for row in students) / len(students) == 86
assert [row["name"] for row in students if row["python"] >= 85] == ["小林", "小陈"]
students[1]["python"] = 85
print('\n===== [row["name"] for row in students if row["python"] >= 85] =====')
print([row["name"] for row in students if row["python"] >= 85])
assert sum(row["python"] for row in students) / len(students) == 86.25
empty = []
result = sum(empty) / len(empty) if empty else "没有成绩"
print('\n===== result =====')
print(result)
assert result == "没有成绩"

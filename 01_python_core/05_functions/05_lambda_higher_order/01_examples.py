"""可运行示例：先预测结果，再执行。"""

students = [("甲", 88), ("乙", 95), ("丙", 81)]
ordered = sorted(students, key=lambda item: item[1], reverse=True)
print(ordered)

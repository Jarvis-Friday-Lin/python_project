"""可运行示例：先预测结果，再执行。"""

student = {"name": "小林", "score": 90}
student["age"] = 18
print(student.get("city", "未知"))
for key, value in student.items():
    print(key, value)

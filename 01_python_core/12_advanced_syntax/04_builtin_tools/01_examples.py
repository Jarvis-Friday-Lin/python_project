"""可运行示例：先预测结果，再执行。"""

names = ["甲", "乙"]
scores = [90, 85]
for index, (name, score) in enumerate(zip(names, scores), 1):
    print(index, name, score)

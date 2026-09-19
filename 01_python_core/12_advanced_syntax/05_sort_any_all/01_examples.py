"""可运行示例：先预测结果，再执行。"""

records = [{"name": "甲", "score": 80}, {"name": "乙", "score": 95}]
print(sorted(records, key=lambda row: row["score"], reverse=True))
print(any(row["score"] >= 90 for row in records))
print(all(row["score"] >= 60 for row in records))

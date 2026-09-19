"""可运行示例：先预测结果，再执行。"""

score = 86
if score >= 90:
    level = "优秀"
elif score >= 60:
    level = "合格"
else:
    level = "待提高"
print(level)

"""可运行示例：先预测结果，再执行。"""

total = 0
for number in range(1, 6):
    total += number
print(total)
for index, name in enumerate(["甲", "乙"], start=1):
    print(index, name)

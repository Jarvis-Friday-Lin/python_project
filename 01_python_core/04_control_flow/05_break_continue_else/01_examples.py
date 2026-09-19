"""可运行示例：先预测结果，再执行。"""

numbers = [2, 4, 7, 8]
for number in numbers:
    if number % 2:
        print("找到奇数：", number)
        break
else:
    print("没有奇数")

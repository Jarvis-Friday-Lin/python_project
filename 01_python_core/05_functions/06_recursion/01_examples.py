"""可运行示例：先预测结果，再执行。"""

def factorial(number):
    if number <= 1:
        return 1
    return number * factorial(number - 1)

print(factorial(5))

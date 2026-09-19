"""可运行示例：先预测结果，再执行。"""

def countdown(start):
    while start > 0:
        yield start
        start -= 1
print(list(countdown(3)))

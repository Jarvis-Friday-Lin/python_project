"""可运行示例：先预测结果，再执行。"""

count = 100
def outer():
    count = 0
    def increase():
        nonlocal count
        count += 1
        return count
    return increase

counter = outer()
print(counter(), counter())

"""可运行示例：先预测结果，再执行。"""

def greet(name, message="你好"):
    return f"{message}，{name}"

print(greet("小林"))
print(greet(name="小林", message="早上好"))

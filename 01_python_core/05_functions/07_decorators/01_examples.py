"""可运行示例：先预测结果，再执行。"""

from functools import wraps
def log_call(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"调用 {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

@log_call
def add(a, b):
    return a + b
print(add(2, 3))

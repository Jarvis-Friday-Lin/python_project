"""装饰器基础：参考答案。

这份答案演示核心写法。练习任务通常还有其他正确实现；请重点比较思路。
"""


def main():
    # 先运行本答案，再逐行对照自己的实现。
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


if __name__ == "__main__":
    main()

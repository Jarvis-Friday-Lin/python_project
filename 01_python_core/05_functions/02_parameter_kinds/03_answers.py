"""位置、关键字与默认参数：参考答案。

这份答案演示核心写法。练习任务通常还有其他正确实现；请重点比较思路。
"""


def main():
    # 先运行本答案，再逐行对照自己的实现。
    def greet(name, message="你好"):
        return f"{message}，{name}"

    print(greet("小林"))
    print(greet(name="小林", message="早上好"))


if __name__ == "__main__":
    main()

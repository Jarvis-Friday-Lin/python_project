"""类型检查与类型转换：参考答案。

这份答案演示核心写法。练习任务通常还有其他正确实现；请重点比较思路。
"""


def main():
    # 先运行本答案，再逐行对照自己的实现。
    text = "42"
    number = int(text)
    print(number + 8)
    print(type(number))
    print(isinstance(number, int))


if __name__ == "__main__":
    main()

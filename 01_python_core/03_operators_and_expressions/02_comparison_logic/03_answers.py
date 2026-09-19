"""比较、逻辑与短路求值：参考答案。

这份答案演示核心写法。练习任务通常还有其他正确实现；请重点比较思路。
"""


def main():
    # 先运行本答案，再逐行对照自己的实现。
    age = 20
    has_ticket = True
    can_enter = age >= 18 and has_ticket
    print(can_enter)
    print(1 < age < 100)  # Python 支持链式比较


if __name__ == "__main__":
    main()

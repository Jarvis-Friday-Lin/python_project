"""集合与 frozenset：参考答案。

这份答案演示核心写法。练习任务通常还有其他正确实现；请重点比较思路。
"""


def main():
    # 先运行本答案，再逐行对照自己的实现。
    a = {1, 2, 3}
    b = {3, 4}
    print(a | b)  # 并集
    print(a & b)  # 交集
    print(a - b)  # 差集


if __name__ == "__main__":
    main()

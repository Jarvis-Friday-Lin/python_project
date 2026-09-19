"""布尔值与 None：参考答案。

这份答案演示核心写法。练习任务通常还有其他正确实现；请重点比较思路。
"""


def main():
    # 先运行本答案，再逐行对照自己的实现。
    is_active = True
    result = None
    print(bool(0), bool(""), bool([]))  # 都是假值
    print(result is None)


if __name__ == "__main__":
    main()

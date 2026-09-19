"""成员运算符与身份运算符：参考答案。

这份答案演示核心写法。练习任务通常还有其他正确实现；请重点比较思路。
"""


def main():
    # 先运行本答案，再逐行对照自己的实现。
    colors = ["red", "blue"]
    print("red" in colors)
    a = [1, 2]
    b = [1, 2]
    print(a == b)  # True：内容相等
    print(a is b)  # False：不是同一个列表


if __name__ == "__main__":
    main()

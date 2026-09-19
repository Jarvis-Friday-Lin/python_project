"""Lambda 与高阶函数：参考答案。

这份答案演示核心写法。练习任务通常还有其他正确实现；请重点比较思路。
"""


def main():
    # 先运行本答案，再逐行对照自己的实现。
    students = [("甲", 88), ("乙", 95), ("丙", 81)]
    ordered = sorted(students, key=lambda item: item[1], reverse=True)
    print(ordered)


if __name__ == "__main__":
    main()

"""条件分支：参考答案。

这份答案演示核心写法。练习任务通常还有其他正确实现；请重点比较思路。
"""


def main():
    # 先运行本答案，再逐行对照自己的实现。
    score = 86
    if score >= 90:
        level = "优秀"
    elif score >= 60:
        level = "合格"
    else:
        level = "待提高"
    print(level)


if __name__ == "__main__":
    main()

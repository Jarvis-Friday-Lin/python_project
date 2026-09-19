"""for 循环与 range：参考答案。

这份答案演示核心写法。练习任务通常还有其他正确实现；请重点比较思路。
"""


def main():
    # 先运行本答案，再逐行对照自己的实现。
    total = 0
    for number in range(1, 6):
        total += number
    print(total)
    for index, name in enumerate(["甲", "乙"], start=1):
        print(index, name)


if __name__ == "__main__":
    main()

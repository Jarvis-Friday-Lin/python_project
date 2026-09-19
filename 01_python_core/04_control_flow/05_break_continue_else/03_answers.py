"""break、continue 与循环 else：参考答案。

这份答案演示核心写法。练习任务通常还有其他正确实现；请重点比较思路。
"""


def main():
    # 先运行本答案，再逐行对照自己的实现。
    numbers = [2, 4, 7, 8]
    for number in numbers:
        if number % 2:
            print("找到奇数：", number)
            break
    else:
        print("没有奇数")


if __name__ == "__main__":
    main()

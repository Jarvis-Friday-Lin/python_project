"""递归：参考答案。

这份答案演示核心写法。练习任务通常还有其他正确实现；请重点比较思路。
"""


def main():
    # 先运行本答案，再逐行对照自己的实现。
    def factorial(number):
        if number <= 1:
            return 1
        return number * factorial(number - 1)

    print(factorial(5))


if __name__ == "__main__":
    main()

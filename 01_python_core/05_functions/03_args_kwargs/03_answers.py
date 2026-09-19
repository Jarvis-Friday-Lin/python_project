"""可变参数与参数解包：参考答案。

这份答案演示核心写法。练习任务通常还有其他正确实现；请重点比较思路。
"""


def main():
    # 先运行本答案，再逐行对照自己的实现。
    def report(title, *scores, **info):
        print(title, sum(scores) / len(scores))
        print(info)

    values = [80, 90, 100]
    report("成绩", *values, name="小林")


if __name__ == "__main__":
    main()

"""定义问题与检查数据质量：参考答案。

这份答案演示核心写法。练习任务通常还有其他正确实现；请重点比较思路。
"""


def main():
    # 先运行本答案，再逐行对照自己的实现。
    questions = [
        "哪个城市销售额最高？",
        "各月销售趋势如何？",
        "哪些订单金额可能异常？",
    ]
    for index, question in enumerate(questions, 1):
        print(index, question)


if __name__ == "__main__":
    main()

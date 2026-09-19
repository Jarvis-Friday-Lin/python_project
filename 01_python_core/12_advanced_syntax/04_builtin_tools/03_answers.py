"""enumerate、zip、map、filter：参考答案。

这份答案演示核心写法。练习任务通常还有其他正确实现；请重点比较思路。
"""


def main():
    # 先运行本答案，再逐行对照自己的实现。
    names = ["甲", "乙"]
    scores = [90, 85]
    for index, (name, score) in enumerate(zip(names, scores), 1):
        print(index, name, score)


if __name__ == "__main__":
    main()

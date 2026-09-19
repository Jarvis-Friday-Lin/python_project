"""柱状图与堆积柱状图：参考答案。

这份答案演示核心写法。练习任务通常还有其他正确实现；请重点比较思路。
"""


def main():
    # 先运行本答案，再逐行对照自己的实现。
    import matplotlib.pyplot as plt
    categories = ["A", "B", "C"]
    online = [10, 15, 12]
    offline = [5, 6, 8]
    plt.bar(categories, online, label="线上")
    plt.bar(categories, offline, bottom=online, label="线下")
    plt.legend()
    plt.show()


if __name__ == "__main__":
    main()

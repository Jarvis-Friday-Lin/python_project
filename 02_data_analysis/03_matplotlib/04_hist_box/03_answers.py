"""直方图与箱线图：参考答案。

这份答案演示核心写法。练习任务通常还有其他正确实现；请重点比较思路。
"""


def main():
    # 先运行本答案，再逐行对照自己的实现。
    import matplotlib.pyplot as plt
    values = [55, 62, 68, 70, 72, 75, 80, 82, 90, 100]
    fig, axes = plt.subplots(1, 2)
    axes[0].hist(values, bins=5, edgecolor="black")
    axes[1].boxplot(values)
    plt.show()


if __name__ == "__main__":
    main()

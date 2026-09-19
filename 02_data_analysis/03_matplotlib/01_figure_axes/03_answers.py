"""Figure 与 Axes：参考答案。

这份答案演示核心写法。练习任务通常还有其他正确实现；请重点比较思路。
"""


def main():
    # 先运行本答案，再逐行对照自己的实现。
    import matplotlib.pyplot as plt
    fig, axes = plt.subplots(1, 2, figsize=(9, 3))
    axes[0].plot([1, 2, 3], [2, 4, 3])
    axes[1].bar(["A", "B"], [5, 8])
    fig.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()

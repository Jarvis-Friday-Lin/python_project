"""折线图与散点图：参考答案。

这份答案演示核心写法。练习任务通常还有其他正确实现；请重点比较思路。
"""


def main():
    # 先运行本答案，再逐行对照自己的实现。
    import matplotlib.pyplot as plt
    x = [1, 2, 3, 4]
    y = [2, 5, 4, 8]
    fig, axes = plt.subplots(1, 2)
    axes[0].plot(x, y, marker="o")
    axes[1].scatter(x, y, s=60, alpha=0.7)
    plt.show()


if __name__ == "__main__":
    main()

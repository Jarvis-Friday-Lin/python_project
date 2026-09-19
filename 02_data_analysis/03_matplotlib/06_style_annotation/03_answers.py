"""颜色、样式与标注：参考答案。

这份答案演示核心写法。练习任务通常还有其他正确实现；请重点比较思路。
"""


def main():
    # 先运行本答案，再逐行对照自己的实现。
    import matplotlib.pyplot as plt
    x, y = [1, 2, 3, 4], [10, 14, 13, 20]
    plt.plot(x, y, color="#2f6f9f", linewidth=2)
    plt.annotate("峰值", xy=(4, 20), xytext=(3.2, 18), arrowprops={"arrowstyle": "->"})
    plt.show()


if __name__ == "__main__":
    main()

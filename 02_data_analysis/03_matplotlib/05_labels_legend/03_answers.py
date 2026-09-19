"""标题、坐标轴、图例与网格：参考答案。

这份答案演示核心写法。练习任务通常还有其他正确实现；请重点比较思路。
"""


def main():
    # 先运行本答案，再逐行对照自己的实现。
    import matplotlib.pyplot as plt
    plt.plot([1, 2, 3], [100, 130, 125], label="销售额", marker="o")
    plt.title("第一季度销售趋势")
    plt.xlabel("月份")
    plt.ylabel("销售额（万元）")
    plt.grid(alpha=0.3)
    plt.legend()
    plt.show()


if __name__ == "__main__":
    main()

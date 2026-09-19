"""主题与调色板：参考答案。

这份答案演示核心写法。练习任务通常还有其他正确实现；请重点比较思路。
"""


def main():
    # 先运行本答案，再逐行对照自己的实现。
    import matplotlib.pyplot as plt
    import seaborn as sns
    sns.set_theme(style="whitegrid", palette="deep")
    sns.lineplot(x=[1, 2, 3], y=[2, 5, 4], marker="o")
    plt.show()


if __name__ == "__main__":
    main()

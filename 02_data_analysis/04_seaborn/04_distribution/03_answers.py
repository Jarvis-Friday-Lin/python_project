"""分布图：histplot 与 kdeplot：参考答案。

这份答案演示核心写法。练习任务通常还有其他正确实现；请重点比较思路。
"""


def main():
    # 先运行本答案，再逐行对照自己的实现。
    import matplotlib.pyplot as plt
    import numpy as np
    import seaborn as sns
    rng = np.random.default_rng(42)
    values = rng.normal(100, 15, 500)
    sns.histplot(values, bins=20, kde=True)
    plt.show()


if __name__ == "__main__":
    main()

"""分类图：bar、count 与 point：参考答案。

这份答案演示核心写法。练习任务通常还有其他正确实现；请重点比较思路。
"""


def main():
    # 先运行本答案，再逐行对照自己的实现。
    import matplotlib.pyplot as plt
    import pandas as pd
    import seaborn as sns
    data = pd.DataFrame({"city": ["上海", "北京", "上海", "深圳"], "amount": [100, 200, 300, 180]})
    sns.barplot(data=data, x="city", y="amount", errorbar=None)
    plt.show()


if __name__ == "__main__":
    main()

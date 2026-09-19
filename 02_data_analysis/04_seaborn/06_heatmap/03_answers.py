"""热力图：参考答案。

这份答案演示核心写法。练习任务通常还有其他正确实现；请重点比较思路。
"""


def main():
    # 先运行本答案，再逐行对照自己的实现。
    import matplotlib.pyplot as plt
    import pandas as pd
    import seaborn as sns
    data = pd.DataFrame({"price": [10, 12, 20, 22], "quantity": [8, 7, 4, 3], "amount": [80, 84, 80, 66]})
    sns.heatmap(data.corr(numeric_only=True), annot=True, cmap="coolwarm", center=0)
    plt.show()


if __name__ == "__main__":
    main()

"""箱线图与小提琴图：参考答案。

这份答案演示核心写法。练习任务通常还有其他正确实现；请重点比较思路。
"""


def main():
    # 先运行本答案，再逐行对照自己的实现。
    import matplotlib.pyplot as plt
    import pandas as pd
    import seaborn as sns
    tips = pd.DataFrame({
        "day": ["周一", "周一", "周二", "周二", "周三", "周三"],
        "total_bill": [80, 150, 90, 210, 120, 260],
    })
    sns.violinplot(data=tips, x="day", y="total_bill", inner="quartile")
    plt.show()


if __name__ == "__main__":
    main()

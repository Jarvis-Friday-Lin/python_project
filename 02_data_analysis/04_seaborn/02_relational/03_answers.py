"""关系图：scatterplot 与 lineplot：参考答案。

这份答案演示核心写法。练习任务通常还有其他正确实现；请重点比较思路。
"""


def main():
    # 先运行本答案，再逐行对照自己的实现。
    import matplotlib.pyplot as plt
    import pandas as pd
    import seaborn as sns
    tips = pd.DataFrame({
        "total_bill": [80, 120, 160, 200, 240, 280],
        "tip": [8, 14, 18, 25, 24, 35],
        "time": ["Lunch", "Lunch", "Dinner", "Dinner", "Dinner", "Lunch"],
        "sex": ["女", "男", "女", "男", "女", "男"],
    })
    sns.scatterplot(data=tips, x="total_bill", y="tip", hue="time", style="sex", alpha=0.75)
    plt.show()


if __name__ == "__main__":
    main()

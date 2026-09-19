"""日期坐标与保存图片：参考答案。

这份答案演示核心写法。练习任务通常还有其他正确实现；请重点比较思路。
"""


def main():
    # 先运行本答案，再逐行对照自己的实现。
    from datetime import datetime
    import matplotlib.pyplot as plt
    dates = [datetime(2026, m, 1) for m in range(1, 5)]
    fig, ax = plt.subplots()
    ax.plot(dates, [10, 15, 13, 20], marker="o")
    fig.autofmt_xdate()
    fig.savefig("matplotlib_example.png", dpi=150, bbox_inches="tight")
    print("已保存 matplotlib_example.png")


if __name__ == "__main__":
    main()

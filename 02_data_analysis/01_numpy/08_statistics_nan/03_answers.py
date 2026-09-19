"""统计函数与缺失值：参考答案。

这份答案演示核心写法。练习任务通常还有其他正确实现；请重点比较思路。
"""


def main():
    # 先运行本答案，再逐行对照自己的实现。
    import numpy as np
    values = np.array([10.0, np.nan, 30.0, 40.0])
    print(np.isnan(values))
    print(np.nanmean(values), np.nanmedian(values), np.nanstd(values))
    print(np.nanpercentile(values, [25, 50, 75]))


if __name__ == "__main__":
    main()

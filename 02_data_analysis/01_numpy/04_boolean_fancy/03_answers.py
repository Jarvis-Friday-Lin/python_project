"""布尔索引与花式索引：参考答案。

这份答案演示核心写法。练习任务通常还有其他正确实现；请重点比较思路。
"""


def main():
    # 先运行本答案，再逐行对照自己的实现。
    import numpy as np
    values = np.array([12, 5, 18, 3, 20])
    print(values[values >= 10])
    print(values[(values >= 10) & (values < 20)])
    print(values[[0, 3, 4]])


if __name__ == "__main__":
    main()

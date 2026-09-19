"""形状变换、转置与轴：参考答案。

这份答案演示核心写法。练习任务通常还有其他正确实现；请重点比较思路。
"""


def main():
    # 先运行本答案，再逐行对照自己的实现。
    import numpy as np
    matrix = np.arange(12).reshape(3, 4)
    print(matrix.T)
    print(matrix.sum(axis=0))
    print(matrix.sum(axis=1))
    print(matrix.ravel())


if __name__ == "__main__":
    main()

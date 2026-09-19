"""数组拼接与拆分：参考答案。

这份答案演示核心写法。练习任务通常还有其他正确实现；请重点比较思路。
"""


def main():
    # 先运行本答案，再逐行对照自己的实现。
    import numpy as np
    left = np.array([[1], [2]])
    right = np.array([[3], [4]])
    matrix = np.concatenate([left, right], axis=1)
    print(matrix)
    print(np.array_split(matrix, 2, axis=0))


if __name__ == "__main__":
    main()

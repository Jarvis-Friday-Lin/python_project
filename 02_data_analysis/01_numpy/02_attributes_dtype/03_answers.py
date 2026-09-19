"""数组属性与 dtype：参考答案。

这份答案演示核心写法。练习任务通常还有其他正确实现；请重点比较思路。
"""


def main():
    # 先运行本答案，再逐行对照自己的实现。
    import numpy as np
    values = np.array([[1, 2], [3, 4]], dtype=np.float64)
    print(values.ndim, values.shape, values.size, values.dtype, values.itemsize)
    print(values.astype(np.int32))


if __name__ == "__main__":
    main()

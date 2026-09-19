"""线性代数与文件保存：参考答案。

这份答案演示核心写法。练习任务通常还有其他正确实现；请重点比较思路。
"""


def main():
    # 先运行本答案，再逐行对照自己的实现。
    import numpy as np
    a = np.array([[2.0, 1.0], [1.0, 3.0]])
    b = np.array([5.0, 6.0])
    solution = np.linalg.solve(a, b)
    print(solution)
    print(a @ solution)


if __name__ == "__main__":
    main()

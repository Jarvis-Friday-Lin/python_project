"""随机数生成器：参考答案。

这份答案演示核心写法。练习任务通常还有其他正确实现；请重点比较思路。
"""


def main():
    # 先运行本答案，再逐行对照自己的实现。
    import numpy as np
    rng = np.random.default_rng(42)
    print(rng.integers(1, 7, size=10))
    print(rng.normal(loc=100, scale=15, size=5))
    print(rng.choice(["A", "B", "C"], size=4, replace=True))


if __name__ == "__main__":
    main()

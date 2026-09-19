"""推导式与生成器表达式：参考答案。

这份答案演示核心写法。练习任务通常还有其他正确实现；请重点比较思路。
"""


def main():
    # 先运行本答案，再逐行对照自己的实现。
    squares = [n * n for n in range(10) if n % 2 == 0]
    mapping = {n: n * n for n in range(3)}
    lazy_total = sum(n * n for n in range(1000))
    print(squares, mapping, lazy_total)


if __name__ == "__main__":
    main()

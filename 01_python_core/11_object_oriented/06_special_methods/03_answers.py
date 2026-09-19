"""特殊方法与运算符重载：参考答案。

这份答案演示核心写法。练习任务通常还有其他正确实现；请重点比较思路。
"""


def main():
    # 先运行本答案，再逐行对照自己的实现。
    class Vector:
        def __init__(self, x, y): self.x, self.y = x, y
        def __repr__(self): return f"Vector({self.x}, {self.y})"
        def __add__(self, other): return Vector(self.x + other.x, self.y + other.y)
    print(Vector(1, 2) + Vector(3, 4))


if __name__ == "__main__":
    main()

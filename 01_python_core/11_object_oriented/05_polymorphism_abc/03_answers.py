"""多态与抽象类：参考答案。

这份答案演示核心写法。练习任务通常还有其他正确实现；请重点比较思路。
"""


def main():
    # 先运行本答案，再逐行对照自己的实现。
    from abc import ABC, abstractmethod
    class Shape(ABC):
        @abstractmethod
        def area(self): ...
    class Square(Shape):
        def __init__(self, side): self.side = side
        def area(self): return self.side ** 2
    print(Square(3).area())


if __name__ == "__main__":
    main()

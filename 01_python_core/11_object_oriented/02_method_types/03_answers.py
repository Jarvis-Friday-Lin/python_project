"""实例方法、类方法与静态方法：参考答案。

这份答案演示核心写法。练习任务通常还有其他正确实现；请重点比较思路。
"""


def main():
    # 先运行本答案，再逐行对照自己的实现。
    class Temperature:
        def __init__(self, celsius): self.celsius = celsius
        @classmethod
        def from_fahrenheit(cls, value): return cls((value - 32) * 5 / 9)
        @staticmethod
        def is_freezing(value): return value <= 0
    temp = Temperature.from_fahrenheit(32)
    print(temp.celsius, Temperature.is_freezing(temp.celsius))


if __name__ == "__main__":
    main()

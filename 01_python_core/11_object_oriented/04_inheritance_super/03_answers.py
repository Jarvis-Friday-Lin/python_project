"""继承、重写与 super：参考答案。

这份答案演示核心写法。练习任务通常还有其他正确实现；请重点比较思路。
"""


def main():
    # 先运行本答案，再逐行对照自己的实现。
    class Animal:
        def __init__(self, name): self.name = name
        def speak(self): return "..."
    class Dog(Animal):
        def speak(self): return f"{self.name}: 汪"
    print(Dog("豆豆").speak())


if __name__ == "__main__":
    main()

"""类、对象与构造方法：参考答案。

这份答案演示核心写法。练习任务通常还有其他正确实现；请重点比较思路。
"""


def main():
    # 先运行本答案，再逐行对照自己的实现。
    class Student:
        school = "Python 学院"  # 类属性
        def __init__(self, name, score):
            self.name = name      # 实例属性
            self.score = score
        def introduce(self):
            return f"我是{self.name}，成绩{self.score}"

    print(Student("小林", 90).introduce())


if __name__ == "__main__":
    main()

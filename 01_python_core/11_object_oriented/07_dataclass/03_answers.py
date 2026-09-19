"""dataclass 数据类：参考答案。

这份答案演示核心写法。练习任务通常还有其他正确实现；请重点比较思路。
"""


def main():
    # 先运行本答案，再逐行对照自己的实现。
    from dataclasses import dataclass, field
    @dataclass
    class Student:
        name: str
        scores: list[int] = field(default_factory=list)
        def average(self): return sum(self.scores) / len(self.scores)
    print(Student("小林", [80, 90, 100]))


if __name__ == "__main__":
    main()

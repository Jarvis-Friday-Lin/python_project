"""基础类型注解：参考答案。

这份答案演示核心写法。练习任务通常还有其他正确实现；请重点比较思路。
"""


def main():
    # 先运行本答案，再逐行对照自己的实现。
    def average(values: list[float]) -> float:
        return sum(values) / len(values)
    name: str = "小林"
    result: float | None = average([80.0, 90.0])
    print(name, result)


if __name__ == "__main__":
    main()

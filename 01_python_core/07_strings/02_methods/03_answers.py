"""查找、替换、拆分与连接：参考答案。

这份答案演示核心写法。练习任务通常还有其他正确实现；请重点比较思路。
"""


def main():
    # 先运行本答案，再逐行对照自己的实现。
    raw = "  apple,banana,orange  "
    cleaned = raw.strip()
    fruits = cleaned.split(",")
    print(" | ".join(fruits))
    print(cleaned.replace("banana", "pear"))


if __name__ == "__main__":
    main()

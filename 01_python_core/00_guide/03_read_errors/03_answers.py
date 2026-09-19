"""阅读错误与调试步骤：参考答案。

这份答案演示核心写法。练习任务通常还有其他正确实现；请重点比较思路。
"""


def main():
    # 先运行本答案，再逐行对照自己的实现。
    values = ["10", "20", "错误"]
    for text in values:
        try:
            print(int(text))
        except ValueError as error:
            print(f"无法转换 {text!r}：{error}")


if __name__ == "__main__":
    main()

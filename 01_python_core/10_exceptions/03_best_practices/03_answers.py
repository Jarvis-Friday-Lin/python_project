"""异常处理最佳实践：参考答案。

这份答案演示核心写法。练习任务通常还有其他正确实现；请重点比较思路。
"""


def main():
    # 先运行本答案，再逐行对照自己的实现。
    def parse_count(text):
        try:
            return int(text)
        except ValueError as error:
            raise ValueError(f"数量必须是整数，收到：{text!r}") from error

    try:
        parse_count("abc")
    except ValueError as error:
        print(error)


if __name__ == "__main__":
    main()

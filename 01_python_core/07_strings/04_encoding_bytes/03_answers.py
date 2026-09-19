"""Unicode、编码与 bytes：参考答案。

这份答案演示核心写法。练习任务通常还有其他正确实现；请重点比较思路。
"""


def main():
    # 先运行本答案，再逐行对照自己的实现。
    text = "你好，Python"
    data = text.encode("utf-8")
    restored = data.decode("utf-8")
    print(data)
    print(restored)


if __name__ == "__main__":
    main()

"""字符串、转义与切片：参考答案。

这份答案演示核心写法。练习任务通常还有其他正确实现；请重点比较思路。
"""


def main():
    # 先运行本答案，再逐行对照自己的实现。
    text = "Python"
    print(text[0], text[-1], text[1:4], text[::-1])
    path = r"C:\new\test"  # 生成文件中保留反斜杠，演示原始字符串
    print(path)


if __name__ == "__main__":
    main()

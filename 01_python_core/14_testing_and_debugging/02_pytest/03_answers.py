"""pytest 入门：参考答案。

这份答案演示核心写法。练习任务通常还有其他正确实现；请重点比较思路。
"""


def main():
    # 先运行本答案，再逐行对照自己的实现。
    # 安装 pytest 后运行：pytest 当前文件
    def divide(a, b): return a / b
    def test_divide():
        assert divide(6, 3) == 2
    print("pytest 示例已定义")


if __name__ == "__main__":
    main()

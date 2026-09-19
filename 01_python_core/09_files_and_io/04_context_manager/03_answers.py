"""上下文管理器：参考答案。

这份答案演示核心写法。练习任务通常还有其他正确实现；请重点比较思路。
"""


def main():
    # 先运行本答案，再逐行对照自己的实现。
    class Managed:
        def __enter__(self):
            print("获取资源")
            return self
        def __exit__(self, exc_type, exc, traceback):
            print("释放资源")

    with Managed():
        print("使用资源")


if __name__ == "__main__":
    main()

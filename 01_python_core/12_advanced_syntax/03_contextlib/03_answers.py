"""contextlib：参考答案。

这份答案演示核心写法。练习任务通常还有其他正确实现；请重点比较思路。
"""


def main():
    # 先运行本答案，再逐行对照自己的实现。
    from contextlib import contextmanager
    @contextmanager
    def managed_resource():
        print("打开")
        try: yield "资源"
        finally: print("关闭")
    with managed_resource() as value: print(value)


if __name__ == "__main__":
    main()

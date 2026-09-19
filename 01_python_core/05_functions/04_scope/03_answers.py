"""作用域、global 与 nonlocal：参考答案。

这份答案演示核心写法。练习任务通常还有其他正确实现；请重点比较思路。
"""


def main():
    # 先运行本答案，再逐行对照自己的实现。
    count = 100
    def outer():
        count = 0
        def increase():
            nonlocal count
            count += 1
            return count
        return increase

    counter = outer()
    print(counter(), counter())


if __name__ == "__main__":
    main()

"""f-string 与格式化：参考答案。

这份答案演示核心写法。练习任务通常还有其他正确实现；请重点比较思路。
"""


def main():
    # 先运行本答案，再逐行对照自己的实现。
    name, score, rate = "小林", 93.456, 0.875
    print(f"{name:<8}{score:>8.2f}{rate:>8.1%}")
    amount = 1234567.8
    print(f"金额：{amount:,.2f}")


if __name__ == "__main__":
    main()

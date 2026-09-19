"""正则表达式基础：参考答案。

这份答案演示核心写法。练习任务通常还有其他正确实现；请重点比较思路。
"""


def main():
    # 先运行本答案，再逐行对照自己的实现。
    import re
    text = "订单 A102，金额 299 元"
    numbers = re.findall(r"\d+", text)
    order = re.search(r"[A-Z]\d+", text)
    print(numbers, order.group() if order else None)


if __name__ == "__main__":
    main()

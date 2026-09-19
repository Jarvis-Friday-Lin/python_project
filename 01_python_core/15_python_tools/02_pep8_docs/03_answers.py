"""PEP 8、命名与文档字符串：参考答案。

这份答案演示核心写法。练习任务通常还有其他正确实现；请重点比较思路。
"""


def main():
    # 先运行本答案，再逐行对照自己的实现。
    def calculate_total(price: float, quantity: int) -> float:
        """计算订单总价。

        Args:
            price: 单件价格。
            quantity: 商品数量。
        Returns:
            未折扣的订单总价。
        """
        return price * quantity
    print(calculate_total(12.5, 3))


if __name__ == "__main__":
    main()

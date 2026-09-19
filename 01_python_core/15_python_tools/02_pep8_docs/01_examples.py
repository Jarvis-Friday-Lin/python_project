"""可运行示例：先预测结果，再执行。"""

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

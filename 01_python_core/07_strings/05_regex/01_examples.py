"""可运行示例：先预测结果，再执行。"""

import re
text = "订单 A102，金额 299 元"
numbers = re.findall(r"\d+", text)
order = re.search(r"[A-Z]\d+", text)
print(numbers, order.group() if order else None)

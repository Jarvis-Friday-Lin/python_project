"""可运行示例：先预测结果，再执行。"""

squares = [n * n for n in range(10) if n % 2 == 0]
mapping = {n: n * n for n in range(3)}
lazy_total = sum(n * n for n in range(1000))
print(squares, mapping, lazy_total)

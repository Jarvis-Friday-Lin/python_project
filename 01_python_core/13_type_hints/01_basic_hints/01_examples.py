"""可运行示例：先预测结果，再执行。"""

def average(values: list[float]) -> float:
    return sum(values) / len(values)
name: str = "小林"
result: float | None = average([80.0, 90.0])
print(name, result)

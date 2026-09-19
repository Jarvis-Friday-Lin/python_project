"""可运行示例：先预测结果，再执行。"""

class Temperature:
    def __init__(self, celsius): self.celsius = celsius
    @classmethod
    def from_fahrenheit(cls, value): return cls((value - 32) * 5 / 9)
    @staticmethod
    def is_freezing(value): return value <= 0
temp = Temperature.from_fahrenheit(32)
print(temp.celsius, Temperature.is_freezing(temp.celsius))

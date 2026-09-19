"""可运行示例：先预测结果，再执行。"""

class Animal:
    def __init__(self, name): self.name = name
    def speak(self): return "..."
class Dog(Animal):
    def speak(self): return f"{self.name}: 汪"
print(Dog("豆豆").speak())

"""可运行示例：先预测结果，再执行。"""

class Student:
    school = "Python 学院"  # 类属性
    def __init__(self, name, score):
        self.name = name      # 实例属性
        self.score = score
    def introduce(self):
        return f"我是{self.name}，成绩{self.score}"

print(Student("小林", 90).introduce())

"""可运行示例：先预测结果，再执行。"""

from dataclasses import dataclass, field
@dataclass
class Student:
    name: str
    scores: list[int] = field(default_factory=list)
    def average(self): return sum(self.scores) / len(self.scores)
print(Student("小林", [80, 90, 100]))

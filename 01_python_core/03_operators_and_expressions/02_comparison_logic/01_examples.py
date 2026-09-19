"""可运行示例：先预测结果，再执行。"""

age = 20
has_ticket = True
can_enter = age >= 18 and has_ticket
print(can_enter)
print(1 < age < 100)  # Python 支持链式比较

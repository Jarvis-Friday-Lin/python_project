"""可运行示例：先预测结果，再执行。"""

class Account:
    def __init__(self, balance=0): self._balance = balance
    @property
    def balance(self): return self._balance
    def deposit(self, amount):
        if amount <= 0: raise ValueError("金额必须为正数")
        self._balance += amount
account = Account(100)
account.deposit(50)
print(account.balance)

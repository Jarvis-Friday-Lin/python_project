"""封装与 property：参考答案。

这份答案演示核心写法。练习任务通常还有其他正确实现；请重点比较思路。
"""


def main():
    # 先运行本答案，再逐行对照自己的实现。
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


if __name__ == "__main__":
    main()

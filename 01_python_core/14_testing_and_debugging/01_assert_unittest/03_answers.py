"""assert 与 unittest：参考答案。

这份答案演示核心写法。练习任务通常还有其他正确实现；请重点比较思路。
"""


def main():
    # 先运行本答案，再逐行对照自己的实现。
    import unittest
    def add(a, b): return a + b
    class AddTests(unittest.TestCase):
        def test_positive(self): self.assertEqual(add(2, 3), 5)
    if __name__ == "__main__": unittest.main()


if __name__ == "__main__":
    main()

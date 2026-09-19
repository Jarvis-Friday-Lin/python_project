"""可运行示例：先预测结果，再执行。"""

import unittest
def add(a, b): return a + b
class AddTests(unittest.TestCase):
    def test_positive(self): self.assertEqual(add(2, 3), 5)
if __name__ == "__main__": unittest.main()

"""可运行示例：先预测结果，再执行。"""

# 安装 pytest 后运行：pytest 当前文件
def divide(a, b): return a / b
def test_divide():
    assert divide(6, 3) == 2
print("pytest 示例已定义")

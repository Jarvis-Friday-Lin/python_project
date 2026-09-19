"""可运行示例：先预测结果，再执行。"""

text = "你好，Python"
data = text.encode("utf-8")
restored = data.decode("utf-8")
print(data)
print(restored)

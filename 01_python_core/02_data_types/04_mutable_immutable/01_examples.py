"""可运行示例：先预测结果，再执行。"""

first = [1, 2]
second = first
second.append(3)  # 修改的是二者共同引用的列表
print(first)
text = "hi"
text = text + "!"  # 创建新字符串并重新绑定

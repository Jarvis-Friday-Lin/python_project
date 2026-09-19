"""可运行示例：先预测结果，再执行。"""

text = "12a"
try:
    number = int(text)
except ValueError as error:
    print("不是合法整数：", error)
else:
    print(number)
finally:
    print("转换结束")

"""可运行示例：先预测结果，再执行。"""

values = ["10", "20", "错误"]
for text in values:
    try:
        print(int(text))
    except ValueError as error:
        print(f"无法转换 {text!r}：{error}")

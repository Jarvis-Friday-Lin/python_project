"""可运行示例：先预测结果，再执行。"""

questions = [
    "哪个城市销售额最高？",
    "各月销售趋势如何？",
    "哪些订单金额可能异常？",
]
for index, question in enumerate(questions, 1):
    print(index, question)

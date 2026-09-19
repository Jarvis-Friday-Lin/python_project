"""可运行示例：先预测结果，再执行。"""

def report(title, *scores, **info):
    print(title, sum(scores) / len(scores))
    print(info)

values = [80, 90, 100]
report("成绩", *values, name="小林")

"""参考答案：读懂函数、关键字参数、属性与方法"""
# 基础准备/综合应用：为三份 PDF 的学习提供衔接。
# 建议先完成 02_exercises.py；下面的实现与该题数据、要求一一对应。

def average(scores, digits=1):
    # 空集合不存在平均分，用 None 表示未得到结果，而不是伪造零分。
    return round(sum(scores) / len(scores), digits) if scores else None
scores = [80, 90, 100]
print('\n===== average(scores) =====')
print(average(scores))
print('\n===== average(scores=scores, digits=2) =====')
print(average(scores=scores, digits=2))
assert average(scores) == average(scores=scores, digits=2) == 90
assert average([]) is None

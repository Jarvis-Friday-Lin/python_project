"""案例驱动示例：读懂函数、关键字参数、属性与方法"""
# 基础准备/综合应用：为三份 PDF 的学习提供衔接。
# 任务：把 3 名学生的成绩格式化为可读结果。
# 调用看似相似，参数、属性和方法却承担不同工作；先用自己的小函数理解，再读库的接口。
# 案例数据：
# | name | score |
# |---|---:|
# | 小林 | 80 |
# | 小周 | 90 |
# | 小陈 | 100 |
# 先看整体路线：
# 第 1 步：定义返回平均分的函数，区分输入与返回。
# 第 2 步：用位置和关键字传参，观察默认值。
# 第 3 步：借列表、字典理解属性和方法的调用形式。

def average(scores, digits=1):
    # scores 是必填位置参数；digits 有默认值，也能用 digits=2 明确传入。
    # return 把结果交还调用处，与 print 显示到屏幕不同。
    return round(sum(scores) / len(scores), digits)

scores = [80, 90, 100]
result = average(scores)
print('\n===== result =====')
print(result)
print('\n===== average(scores, digits=2) =====')
print(average(scores, digits=2))
# 列表的 append 是绑定在对象上的方法，需要括号才能执行。
scores.append(95)
print('\n===== scores =====')
print(scores)
# 后面 ndarray.shape 是属性（状态）；ndarray.mean() 是方法（做计算）。
# 类型注解是说明，不会自动转换输入类型或校验数据。
def label(name: str, score: float) -> str:
    return f"{name}：{score:.1f} 分"
print('\n===== label(name="小林", score=80) =====')
print(label(name="小林", score=80))
assert result == 90

# 学完先自己回答，再看下面的参考答案：
# 1. 这个知识点解决什么类型的问题？
# 2. 为什么当前案例需要它？
# 3. 每一步代码为什么要在此时出现？
# 4. 如果换一种做法，代价和风险是什么？

# 参考答案：
# 1. 理解一个调用收到了什么、返回了什么。
# 2. 后面每个库函数都有参数和返回值，不能只照抄。
# 3. 先定义函数，再提供数据调用，最后检查返回值，避免混淆返回和打印。
# 4. 把所有计算直接写在 print 里简单，但不利于复用结果与检查。

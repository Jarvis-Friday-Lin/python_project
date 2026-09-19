"""变量与命名规范：参考答案。

这份答案演示核心写法。练习任务通常还有其他正确实现；请重点比较思路。
"""


def main():
    # 先运行本答案，再逐行对照自己的实现。
    student_name = "小林"
    age = 18
    age = age + 1  # 右侧先计算，再把新结果绑定给 age
    print(student_name, age)


if __name__ == "__main__":
    main()

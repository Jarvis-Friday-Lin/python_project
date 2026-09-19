"""可变对象与不可变对象：参考答案。

这份答案演示核心写法。练习任务通常还有其他正确实现；请重点比较思路。
"""


def main():
    # 先运行本答案，再逐行对照自己的实现。
    first = [1, 2]
    second = first
    second.append(3)  # 修改的是二者共同引用的列表
    print(first)
    text = "hi"
    text = text + "!"  # 创建新字符串并重新绑定


if __name__ == "__main__":
    main()

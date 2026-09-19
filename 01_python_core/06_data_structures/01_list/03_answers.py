"""列表：参考答案。

这份答案演示核心写法。练习任务通常还有其他正确实现；请重点比较思路。
"""


def main():
    # 先运行本答案，再逐行对照自己的实现。
    values = [3, 1, 2]
    values.append(4)
    values[0] = 30
    print(values[1:3])
    print(sorted(values))  # 返回新列表
    values.sort()          # 原地排序


if __name__ == "__main__":
    main()

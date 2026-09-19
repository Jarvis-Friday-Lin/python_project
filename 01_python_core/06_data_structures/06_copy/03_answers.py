"""浅拷贝与深拷贝：参考答案。

这份答案演示核心写法。练习任务通常还有其他正确实现；请重点比较思路。
"""


def main():
    # 先运行本答案，再逐行对照自己的实现。
    from copy import copy, deepcopy
    original = [[1], [2]]
    shallow = copy(original)
    deep = deepcopy(original)
    shallow[0].append(9)
    print(original, shallow, deep)


if __name__ == "__main__":
    main()

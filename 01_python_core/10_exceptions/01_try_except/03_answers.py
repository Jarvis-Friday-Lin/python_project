"""try、except、else 与 finally：参考答案。

这份答案演示核心写法。练习任务通常还有其他正确实现；请重点比较思路。
"""


def main():
    # 先运行本答案，再逐行对照自己的实现。
    text = "12a"
    try:
        number = int(text)
    except ValueError as error:
        print("不是合法整数：", error)
    else:
        print(number)
    finally:
        print("转换结束")


if __name__ == "__main__":
    main()

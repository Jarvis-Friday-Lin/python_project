"""结构化模式匹配：参考答案。

这份答案演示核心写法。练习任务通常还有其他正确实现；请重点比较思路。
"""


def main():
    # 先运行本答案，再逐行对照自己的实现。
    command = "start"
    match command:
        case "start":
            print("开始")
        case "stop":
            print("停止")
        case _:
            print("未知命令")


if __name__ == "__main__":
    main()

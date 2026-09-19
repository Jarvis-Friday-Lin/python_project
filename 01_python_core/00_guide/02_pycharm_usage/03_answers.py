"""PyCharm 打开与运行项目：参考答案。

这份答案演示核心写法。练习任务通常还有其他正确实现；请重点比较思路。
"""


def main():
    # 先运行本答案，再逐行对照自己的实现。
    import sys
    from pathlib import Path
    print("当前解释器：", sys.executable)
    print("当前脚本：", Path(__file__).resolve())
    print("工作目录：", Path.cwd())


if __name__ == "__main__":
    main()

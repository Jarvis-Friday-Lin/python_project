"""文本文件读写：参考答案。

这份答案演示核心写法。练习任务通常还有其他正确实现；请重点比较思路。
"""


def main():
    # 先运行本答案，再逐行对照自己的实现。
    from pathlib import Path
    path = Path(__file__).with_name("demo_output.txt")
    path.write_text("第一行\n第二行\n", encoding="utf-8")
    print(path.read_text(encoding="utf-8"))


if __name__ == "__main__":
    main()

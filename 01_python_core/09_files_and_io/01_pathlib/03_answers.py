"""路径与 pathlib：参考答案。

这份答案演示核心写法。练习任务通常还有其他正确实现；请重点比较思路。
"""


def main():
    # 先运行本答案，再逐行对照自己的实现。
    from pathlib import Path
    project = Path(__file__).resolve().parent
    data_file = project / "sample.txt"
    print(project)
    print(data_file.name, data_file.suffix)


if __name__ == "__main__":
    main()

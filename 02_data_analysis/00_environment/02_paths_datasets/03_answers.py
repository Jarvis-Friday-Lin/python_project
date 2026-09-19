"""数据集与文件路径：参考答案。

这份答案演示核心写法。练习任务通常还有其他正确实现；请重点比较思路。
"""


def main():
    # 先运行本答案，再逐行对照自己的实现。
    from pathlib import Path
    data_dir = Path(__file__).resolve().parents[2] / "datasets"
    print(data_dir)
    print([path.name for path in data_dir.glob("*.csv")])


if __name__ == "__main__":
    main()

"""导出与可复现分析：参考答案。

这份答案演示核心写法。练习任务通常还有其他正确实现；请重点比较思路。
"""


def main():
    # 先运行本答案，再逐行对照自己的实现。
    from pathlib import Path
    output_dir = Path(__file__).resolve().parents[2] / "outputs"
    output_dir.mkdir(exist_ok=True)
    print("所有清洗表格、图表和摘要统一写入：", output_dir)


if __name__ == "__main__":
    main()

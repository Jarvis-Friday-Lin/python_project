"""探索性数据分析：参考答案。

这份答案演示核心写法。练习任务通常还有其他正确实现；请重点比较思路。
"""


def main():
    # 先运行本答案，再逐行对照自己的实现。
    from pathlib import Path
    import pandas as pd
    data = pd.read_csv(Path(__file__).resolve().parents[2] / "datasets" / "sales.csv")
    data["amount"] = data["price"] * data["quantity"]
    print(data["amount"].describe())
    print(data.groupby("city")["amount"].agg(["count", "sum", "mean"]))


if __name__ == "__main__":
    main()

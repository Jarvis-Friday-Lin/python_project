"""清洗与转换：参考答案。

这份答案演示核心写法。练习任务通常还有其他正确实现；请重点比较思路。
"""


def main():
    # 先运行本答案，再逐行对照自己的实现。
    from pathlib import Path
    import pandas as pd
    path = Path(__file__).resolve().parents[2] / "datasets" / "sales.csv"
    data = pd.read_csv(path)
    data["date"] = pd.to_datetime(data["date"])
    data["amount"] = data["price"] * data["quantity"]
    data = data.drop_duplicates(subset="order_id")
    print(data.info())


if __name__ == "__main__":
    main()

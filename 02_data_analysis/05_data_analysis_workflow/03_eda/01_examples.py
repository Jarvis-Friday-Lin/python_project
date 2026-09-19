"""可运行示例：先预测结果，再执行。"""

from pathlib import Path
import pandas as pd
data = pd.read_csv(Path(__file__).resolve().parents[2] / "datasets" / "sales.csv")
data["amount"] = data["price"] * data["quantity"]
print(data["amount"].describe())
print(data.groupby("city")["amount"].agg(["count", "sum", "mean"]))

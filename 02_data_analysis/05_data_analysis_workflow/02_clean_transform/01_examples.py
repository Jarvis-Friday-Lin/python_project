"""可运行示例：先预测结果，再执行。"""

from pathlib import Path
import pandas as pd
path = Path(__file__).resolve().parents[2] / "datasets" / "sales.csv"
data = pd.read_csv(path)
data["date"] = pd.to_datetime(data["date"])
data["amount"] = data["price"] * data["quantity"]
data = data.drop_duplicates(subset="order_id")
print(data.info())

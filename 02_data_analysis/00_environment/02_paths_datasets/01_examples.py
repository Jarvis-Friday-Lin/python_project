"""可运行示例：先预测结果，再执行。"""

from pathlib import Path
data_dir = Path(__file__).resolve().parents[2] / "datasets"
print(data_dir)
print([path.name for path in data_dir.glob("*.csv")])

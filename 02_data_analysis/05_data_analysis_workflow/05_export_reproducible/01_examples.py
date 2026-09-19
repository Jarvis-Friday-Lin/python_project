"""可运行示例：先预测结果，再执行。"""

from pathlib import Path
output_dir = Path(__file__).resolve().parents[2] / "outputs"
output_dir.mkdir(exist_ok=True)
print("所有清洗表格、图表和摘要统一写入：", output_dir)

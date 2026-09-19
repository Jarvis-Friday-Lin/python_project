"""可运行示例：先预测结果，再执行。"""

from pathlib import Path
project = Path(__file__).resolve().parent
data_file = project / "sample.txt"
print(project)
print(data_file.name, data_file.suffix)

"""可运行示例：先预测结果，再执行。"""

from pathlib import Path
path = Path(__file__).with_name("demo_output.txt")
path.write_text("第一行\n第二行\n", encoding="utf-8")
print(path.read_text(encoding="utf-8"))

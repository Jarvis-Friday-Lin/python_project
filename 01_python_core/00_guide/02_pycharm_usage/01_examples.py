"""可运行示例：先预测结果，再执行。"""

import sys
from pathlib import Path
print("当前解释器：", sys.executable)
print("当前脚本：", Path(__file__).resolve())
print("工作目录：", Path.cwd())

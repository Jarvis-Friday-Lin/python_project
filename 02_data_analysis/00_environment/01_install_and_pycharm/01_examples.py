"""可运行示例：先预测结果，再执行。"""

import importlib
for package in ["numpy", "pandas", "matplotlib", "seaborn"]:
    module = importlib.import_module(package)
    print(package, module.__version__)

"""可运行示例：先预测结果，再执行。"""

steps = ["阅读 README", "预测输出", "运行 examples.py", "完成 exercises.py", "对照 answers.py"]
for number, step in enumerate(steps, 1):
    print(f"{number}. {step}")

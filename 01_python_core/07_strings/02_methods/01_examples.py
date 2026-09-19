"""可运行示例：先预测结果，再执行。"""

raw = "  apple,banana,orange  "
cleaned = raw.strip()
fruits = cleaned.split(",")
print(" | ".join(fruits))
print(cleaned.replace("banana", "pear"))

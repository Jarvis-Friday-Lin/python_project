"""参考答案：保存并重新读取工具盘点文件"""
# 基础准备/综合应用：为三份 PDF 的学习提供衔接。
# 课件核心：衔接 Pandas PDF 第34—36页 CSV 输入输出。
# 扩展：pathlib、标准库csv、以__file__定位输出目录为前置补充。
# 案例数据（据此自行创建对象，不能照抄 examples 的数据）：
# | tool | quantity |
# |---|---|
# | 锤子 | 3 |
# | 扳手 | 6 |
# | 钳子 | 2 |
# 建议先做练习，再逐段对照下面的实现；assert 用于验证结果。

from pathlib import Path
import csv

# resolve() 将脚本路径绝对化，parent 指脚本所在文件夹，与终端当前位置无关。
out = Path(__file__).resolve().parent / 'outputs'
out.mkdir(exist_ok=True)
path = out / 'tool_count.csv'
rows = [{'tool': '锤子', 'quantity': 3}, {'tool': '扳手', 'quantity': 6}, {'tool': '钳子', 'quantity': 2}]
with path.open('w', encoding='utf-8', newline='') as stream:
    writer = csv.DictWriter(stream, fieldnames=['tool', 'quantity'])
    writer.writeheader()
    writer.writerows(rows)
with path.open(encoding='utf-8', newline='') as stream:
    loaded = list(csv.DictReader(stream))
# CSV 字段默认读成字符串，算术运算前显式转换。
total = sum(int(row['quantity']) for row in loaded)
low = [row['tool'] for row in loaded if int(row['quantity']) < 3]
print('\n===== (total, low) =====')
print((total, low))
assert total == 11 and low == ['钳子']
assert path.is_file() and len(loaded) == 3

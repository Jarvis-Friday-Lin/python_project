"""参考答案：从任何工作目录读取同一份CSV"""
# 基础准备/综合应用：为三份 PDF 的学习提供衔接。
# 建议先完成 02_exercises.py；下面的实现与该题数据、要求一一对应。

from pathlib import Path
import csv
path = Path(__file__).resolve().parents[2] / "datasets" / "scores.csv"
with path.open(encoding="utf-8-sig", newline="") as stream:
    rows = list(csv.DictReader(stream))
scores = [int(row["score"]) for row in rows]
print('\n===== path =====')
print(path)
print('\n===== sum(scores) / len(scores) =====')
print(sum(scores) / len(scores))
assert scores == [80, 90, 100]

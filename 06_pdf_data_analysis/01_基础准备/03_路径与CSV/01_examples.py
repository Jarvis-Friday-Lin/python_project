"""案例驱动示例：从任何工作目录读取同一份CSV"""
# 基础准备/综合应用：为三份 PDF 的学习提供衔接。
# 任务：在 PyCharm 右键运行时，也能找到课程附带的数据。
# 相对路径从当前工作目录解析；文件自身的位置是更稳定的定位起点。
# 案例数据：
# | name | score |
# |---|---:|
# | 小林 | 80 |
# | 小周 | 90 |
# | 小陈 | 100 |
# 先看整体路线：
# 第 1 步：用 __file__ 找到当前脚本，再定位课程 datasets。
# 第 2 步：用 csv.DictReader 读取带表头数据。
# 第 3 步：把文本成绩转为整数后统计。

from pathlib import Path
import csv

# resolve() 得到绝对路径；本节脚本位于“阶段/知识点”两层目录下面。
course = Path(__file__).resolve().parents[2]
path = course / "datasets" / "scores.csv"
# newline="" 交给 csv 模块处理换行，utf-8-sig 同时兼容带 BOM 的 UTF-8。
with path.open(encoding="utf-8-sig", newline="") as stream:
    rows = list(csv.DictReader(stream))
print('\n===== rows =====')
print(rows)
# CSV 字段首先是字符串，不会因为看起来像数字就自动支持求和。
scores = [int(row["score"]) for row in rows]
print('\n===== sum(scores) / len(scores) =====')
print(sum(scores) / len(scores))
assert scores == [80, 90, 100]
# 不要把 /Users/... 写死进课程代码，换电脑就失效了。

# 学完先自己回答，再看下面的参考答案：
# 1. 这个知识点解决什么类型的问题？
# 2. 为什么当前案例需要它？
# 3. 每一步代码为什么要在此时出现？
# 4. 如果换一种做法，代价和风险是什么？

# 参考答案：
# 1. 稳定定位本地文件，并读入结构化记录。
# 2. PyCharm 工作目录可变，不能把工作目录当作脚本目录。
# 3. 先解析路径，再打开文件，读出文本后再转换类型参与计算。
# 4. 直接用相对路径更短但依赖启动位置；绝对硬编码不方便迁移。

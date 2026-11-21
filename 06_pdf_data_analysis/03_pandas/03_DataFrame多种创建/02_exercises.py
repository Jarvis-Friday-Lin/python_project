"""迁移练习：从不同来源拼出展馆客流表"""
# 对应 PDF：13-pandas-full.pdf 第 13—17 页
# 课件核心：第13—17页：字典列表、列字典、二维数组、Series按索引建表。
# 扩展：DataFrame.equals用于验证等价，属检查补充。
# 案例数据（据此自行创建对象，不能照抄 examples 的数据）：
# | hall | visitors | capacity |
# |---|---|---|
# | H1 | 120 | 150 |
# | H2 | 85 | 100 |
# | H3 | 60 | 80 |
# | tickets补充 | H1=110，H3=55 | H2未提供 |
#
# 业务任务与本题要求：
# 1. 基础任务：只取H1/H2/H3三行，用字典列表、列字典各创建一张hall/visitors/capacity表并验证相等。
# 2. 应用任务：用二维数值数组创建以hall为index、含visitors/capacity两列的表。
# 3. 验证任务：用两份索引不同的Series创建visitors/tickets表，确认H2的tickets缺失，不把H3票数错放到H2。
#
# 请先独立完成；结果和解释请在自己的代码中验证，再对照 03_answers.py。

# TODO：创建数据、完成任务并检查结果。

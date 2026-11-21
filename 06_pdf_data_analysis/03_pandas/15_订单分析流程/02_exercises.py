"""迁移练习：从借阅原始记录到分类汇总"""
# 对应 PDF：13-pandas-full.pdf 第 20—46 页综合
# 课件核心：第20—26、31—36、41—46页：取列、筛选、统计、缺失、分组、CSV导出。
# 扩展：to_numeric与问题原因标记为扩展；任务不依赖原orders.csv。
# 案例数据（据此自行创建对象，不能照抄 examples 的数据）：
# | record_id | category | pages_raw | returned |
# |---|---|---|---|
# | L1 | science | "120" | yes |
# | L2 | history | "80" | yes |
# | L3 | science | "200" | yes |
# | L4 | art | "未知" | yes |
# | L5 | history | "60" | no |
# | L6 | art | "-10" | yes |
#
# 业务任务与本题要求：
# 1. 基础任务：按注释表自行创建借阅表，保留pages_raw，再转换pages。
# 2. 应用任务：只统计returned=yes且页数合法、非负的记录，按category求总页数和平均页数。
# 3. 验证任务：给未计入记录标明非法页数/未归还/负页数三种原因，验证有效与排除记录合起来仍为6行。
# 4. 输出任务：将汇总和问题明细分别保存为本节outputs/library_summary.csv和library_issues.csv，不改datasets。
#
# 请先独立完成；结果和解释请在自己的代码中验证，再对照 03_answers.py。

# TODO：创建数据、完成任务并检查结果。

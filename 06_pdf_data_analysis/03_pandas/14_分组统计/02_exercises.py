"""迁移练习：按科室汇总维修工单"""
# 对应 PDF：13-pandas-full.pdf 第 45—46 页
# 课件核心：第45—46页：groupby、遍历分组、组内mean/sum、reset_index。
# 扩展：agg/count/size的比较为扩展；0工时有效、None未登记。
# 案例数据（据此自行创建对象，不能照抄 examples 的数据）：
# | ticket | team | hours |
# |---|---|---|
# | W1 | electrical | 2 |
# | W2 | plumbing | 3 |
# | W3 | electrical | 4 |
# | W4 | plumbing | None |
# | W5 | electrical | 0 |
#
# 业务任务与本题要求：
# 1. 基础任务：按team分组，逐组展示原始工单与工时总和、平均值。
# 2. 应用任务：生成每科室一行的汇总表，将team保持为普通列。
# 3. 扩展任务：对比有效工时条数与工单条数，解释plumbing平均3小时不是用两单相除。
#
# 请先独立完成；结果和解释请在自己的代码中验证，再对照 03_answers.py。

# TODO：创建数据、完成任务并检查结果。

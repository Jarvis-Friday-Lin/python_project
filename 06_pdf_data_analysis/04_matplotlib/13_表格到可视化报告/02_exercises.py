"""迁移练习：用四张图报告社区借阅情况"""
# 对应 PDF：14-matplotlib-full.pdf 第8—21页；13-pandas-full.pdf 第45—46页综合
# 课件核心：Matplotlib第8—21页多子图、plot/bar/hist/boxplot/savefig；Pandas第45—46页分组。
# 扩展：groupby的多种聚合组合、图形读取检查与路径为跨课件应用补充。
# 案例数据（据此自行创建对象，不能照抄 examples 的数据）：
# | day | branch | books |
# |---|---|---|
# | 1 | East | 12 |
# | 1 | West | 8 |
# | 2 | East | 18 |
# | 2 | West | 12 |
# | 3 | East | 15 |
# | 3 | West | 10 |
# | 4 | East | 20 |
# | 4 | West | 15 |
#
# 业务任务与本题要求：
# 1. 基础任务：自行建DataFrame，按天汇总借阅总量、按分馆汇总总量，明确每个图回答的问题。
# 2. 应用任务：创建2×2面板：每日趋势、分馆总量、单条记录分布、按分馆的箱线图；单位均为Books或Records。
# 3. 验证任务：每日汇总[20,30,25,35]，分馆East=65/West=45，合计110；直方分箱[0,10,15,21]应覆盖全部8条记录。
# 4. 输出任务：保存outputs/library_dashboard.png，确保折线y值来自分组结果，而不是手写预期列表。
#
# 请先独立完成；结果和解释请在自己的代码中验证，再对照 03_answers.py。

# TODO：创建数据、完成任务并检查结果。

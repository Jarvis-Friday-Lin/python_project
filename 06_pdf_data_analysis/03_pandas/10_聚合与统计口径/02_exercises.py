"""迁移练习：按书架统计借阅与归还"""
# 对应 PDF：13-pandas-full.pdf 第 31—33 页
# 课件核心：第31—33页：mean/std/min/max/sum及DataFrame按列聚合。
# 扩展：agg、axis=1、count/size、min_count为统计口径扩展。
# 案例数据（据此自行创建对象，不能照抄 examples 的数据）：
# | shelf | borrowed | returned |
# |---|---|---|
# | A | 12 | 9 |
# | B | 8 | 8 |
# | C | 16 | 10 |
#
# 业务任务与本题要求：
# 1. 基础任务：对borrowed/returned分别输出均值、标准差、最小、最大与总和。
# 2. 应用任务：新增outstanding=borrowed-returned，并计算每架两种操作数量之和，区别按行求和与按列求和。
# 3. 扩展任务：将C的returned设为缺失，验证有效归还数2而两列总格子数仍6；全缺失Series用sum(min_count=1)应保持缺失。
#
# 请先独立完成；结果和解释请在自己的代码中验证，再对照 03_answers.py。

# TODO：创建数据、完成任务并检查结果。

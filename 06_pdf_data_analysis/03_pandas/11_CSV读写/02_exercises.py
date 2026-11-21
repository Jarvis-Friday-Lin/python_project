"""迁移练习：读写有说明行的维修记录"""
# 对应 PDF：13-pandas-full.pdf 第 34—36 页
# 课件核心：第34—36页：read_csv的sep/skiprows/na_values，以及to_csv(index=False)。
# 扩展：StringIO把题面文本作为可读文件，pathlib保证工作目录独立，均为输入输出补充。
# 案例数据（据此自行创建对象，不能照抄 examples 的数据）：
# | source_row | 内容（CSV以分号分隔） |
# |---|---|
# | 1 | maintenance export |
# | 2 | device;cost;hours |
# | 3 | M1;120;2 |
# | 4 | M2;Missing;3 |
# | 5 | M3;80;N/A |
# | 6 | M4;0;0 |
#
# 业务任务与本题要求：
# 1. 基础任务：把上表内容按顺序组成原始CSV文本，使用read_csv读取；跳过首行说明，分号分隔。
# 2. 应用任务：将Missing/N/A识别为缺失，计算有效维修费用总和，0费用与0工时不能被当作缺失。
# 3. 验证任务：保存outputs/maintenance.csv，不输出索引；读回核对行列、缺失位置和有效总费用，不改原datasets。
#
# 请先独立完成；结果和解释请在自己的代码中验证，再对照 03_answers.py。

# TODO：创建数据、完成任务并检查结果。

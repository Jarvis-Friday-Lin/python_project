"""迁移练习：第一次接收设备巡检表"""
# 对应 PDF：13-pandas-full.pdf 第 18—20 页；补充head/info/describe用于检查
# 课件核心：第18—20页：columns、index、values、取列。
# 扩展：head/info/describe/to_numpy和检查属性为扩展；None表示真缺失，不是字符串。
# 案例数据（据此自行创建对象，不能照抄 examples 的数据）：
# | device | room | hours |
# |---|---|---|
# | D1 | A | 10 |
# | D2 | B | 20 |
# | D3 | A | 30 |
# | D4 | A | None |
# | D5 | C | 40 |
#
# 业务任务与本题要求：
# 1. 基础任务：创建巡检表，展示列名、索引、前3行和类型信息。
# 2. 应用任务：describe(include="all")后解释room的count/unique/top/freq以及hours的count/mean，不能把行数当有效工时数。
# 3. 扩展任务：仅取hours转换成(5,1)数值数组；验证其中一个缺失，输出结果前保留表达式分隔符。
#
# 请先独立完成；结果和解释请在自己的代码中验证，再对照 03_answers.py。

# TODO：创建数据、完成任务并检查结果。

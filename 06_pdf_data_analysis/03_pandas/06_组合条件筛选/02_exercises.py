"""迁移练习：筛查图书采购候选清单"""
# 对应 PDF：13-pandas-full.pdf 第 10、23、39—40 页
# 课件核心：第10、23、39—40页：比较条件、&、|、~和指定输出列。
# 扩展：isin/between是扩展便捷方法，可用比较与逻辑运算代替。
# 案例数据（据此自行创建对象，不能照抄 examples 的数据）：
# | book | subject | price | copies |
# |---|---|---|---|
# | B1 | science | 45 | 2 |
# | B2 | history | 70 | 1 |
# | B3 | science | 80 | 0 |
# | B4 | art | 35 | 4 |
# | B5 | history | 60 | 0 |
#
# 业务任务与本题要求：
# 1. 基础任务：筛出science且price<=60的书；再筛science或history且copies==0，输出book/price。
# 2. 应用任务：筛非science书；将价格范围设为[40,70]含边界并保留完整记录。
# 3. 扩展任务：用isin、between重写对应选择；将预算改为小于10，检查结果0行但仍保留book/price两列。
#
# 请先独立完成；结果和解释请在自己的代码中验证，再对照 03_answers.py。

# TODO：创建数据、完成任务并检查结果。

"""迁移练习：交付可重复生成的能耗图片"""
# 对应 PDF：14-matplotlib-full.pdf 第 21 页；中文字体与路径为实用补充
# 课件核心：第21页savefig、第11页plot与标签、第12页tight_layout。
# 扩展：中文字体检测、pathlib、dpi与bbox_inches是实用扩展；不以关闭安全校验解决字体问题。
# 案例数据（据此自行创建对象，不能照抄 examples 的数据）：
# | month | energy_kwh |
# |---|---|
# | Jan | 320 |
# | Feb | 280 |
# | Mar | 350 |
# | Apr | 300 |
#
# 业务任务与本题要求：
# 1. 基础任务：绘制四个月能耗折线，注明kWh，保存本节outputs/energy_report.png和energy_report.pdf。
# 2. 应用任务：PNG使用dpi=180，保存前tight_layout，保存时bbox_inches="tight"。
# 3. 扩展任务：检测可用中文字体，有则用中文标题和轴标签，否则英文；换工作目录执行后仍输出到同一路径，检查两个文件非空。
#
# 请先独立完成；结果和解释请在自己的代码中验证，再对照 03_answers.py。

# TODO：创建数据、完成任务并检查结果。

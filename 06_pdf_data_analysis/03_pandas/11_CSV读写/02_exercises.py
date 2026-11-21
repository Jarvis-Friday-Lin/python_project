"""动手练习：读取有说明行和缺失标记的文件"""
# 对应 PDF：13-pandas-full.pdf 第 34—36 页
# 案例数据（请根据表格自行创建对象）：
# | name | department | salary | experience |
# |---|---|---:|---:|
# | Alice | HR | 60000 | N/A |
# | Bob | IT | 75000 | 5 |
# | Charlie | Finance | 80000 | 7 |
# | Diana | IT | 90000 | Missing |
# | Eve | HR | N/A | 3 |
# 
# 业务任务与本题要求：
# 1. 读取datasets/employees_semicolon.csv，首行是说明、分号分隔，数据与上表相同。
# 2. 将N/A和Missing识别为缺失，验证工资缺失1个、经验缺失2个。
# 3. 写到本节outputs/exercise_employees.csv，不覆盖原文件，不输出索引。
# 4. 再读取输出文件，验证列名没有额外的Unnamed列，内容与读入结果一致。
# 
# 在下方编写代码；先独立完成，再运行 03_answers.py 对照。

# TODO：根据上面的数据和本题要求，编写你的实现。


"""动手练习：接到一张表先检查什么"""
# 对应 PDF：13-pandas-full.pdf 第 18—20 页；补充head/info/describe用于检查
# 案例数据（请根据表格自行创建对象）：
# | name | city | score |
# |---|---|---:|
# | 小林 | 上海 | 95 |
# | 小周 | 北京 | 84 |
# | 小陈 | 上海 | 90 |
# | 小李 | 深圳 | 75 |
# 
# 业务任务与本题要求：
# 1. 根据上表建立DataFrame，展示前2行、shape、dtypes、info和describe(include='all')。
# 2. 说明city的count=4、unique=3、top=上海、freq=2，score均值86。
# 3. 只将score列转为(4,1)数值数组，检查不是把姓名也混进去。
# 
# 在下方编写代码；先独立完成，再运行 03_answers.py 对照。

# TODO：根据上面的数据和本题要求，编写你的实现。


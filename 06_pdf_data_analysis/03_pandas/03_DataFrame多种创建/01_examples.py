"""案例驱动示例：从记录、列与数组建立订单表"""
# 对应 PDF：13-pandas-full.pdf 第 13—17 页
# 任务：把相同订单数据从四种输入形式转成表格。
# 输入按行组织还是按列组织，决定构造字典的写法。
# 案例数据：
# | order_id | amount |
# |---|---:|
# | S001 | 100 |
# | S002 | 200 |
# 先看整体路线：
# 第 1 步：从行记录和列列表创建表。
# 第 2 步：给Series明确订单标签后组成表。
# 第 3 步：从NumPy数组创建表并观察类型限制。

import numpy as np
import pandas as pd
records=[{"order_id":"S001","amount":100},{"order_id":"S002","amount":200}]
a=pd.DataFrame(records)
b=pd.DataFrame({"order_id":["S001","S002"],"amount":[100,200]})
print('\n===== a.to_markdown(index=False) =====')
print(a.to_markdown(index=False))
assert a.equals(b)
# Series作为列时按index对齐，即使传入顺序不一致，也不会按位置硬拼。
amount=pd.Series([100,200],index=["S001","S002"])
cost=pd.Series([150,60],index=["S002","S001"])
c=pd.DataFrame({"amount":amount,"cost":cost})
print('\n===== c.to_markdown() =====')
print(c.to_markdown())
# 纯数值二维数组适合矩阵来源；columns提供列名，index提供行标签。
d=pd.DataFrame(np.array([[100,60],[200,150]]),index=["S001","S002"],columns=["amount","cost"])
print('\n===== d.to_markdown() =====')
print(d.to_markdown())
assert c.equals(d)
# Series缺少S002标签会产生缺失；字典里的普通列列表长度不等则直接报错。
partial=pd.DataFrame({"amount":amount,"cost":pd.Series([60],index=["S001"])})
print('\n===== partial.to_markdown() =====')
print(partial.to_markdown())
assert pd.isna(partial.loc["S002","cost"])

# 学完先自己回答，再看下面的参考答案：
# 1. 这个知识点解决什么类型的问题？
# 2. 为什么当前案例需要它？
# 3. 每一步代码为什么要在此时出现？
# 4. 如果换一种做法，代价和风险是什么？

# 参考答案：
# 1. 把按行、按列和矩阵形式的数据统一为表格。
# 2. 订单数据可能来自不同容器，但后续分析希望统一接口。
# 3. 先确定组织方向，再加列名和索引，最后检查标签对齐后的空值。
# 4. 普通列表按位置拼，Series按标签对齐；混淆这点会出现意外缺失或错配。

"""案例驱动示例：温度换算与销售利润率"""
# 对应 PDF：13-pandas-full.pdf 第 28 页
# 任务：将华氏温度换成摄氏温度，并计算商品利润率。
# 整列运算能表达同一业务规则；分母为0时先定义结果，而不是任由无穷大进入报表。
# 案例数据：
# | item | fahrenheit | amount | cost |
# |---|---:|---:|---:|
# | A | 32 | 100 | 60 |
# | B | 212 | 200 | 150 |
# | C | 68 | 0 | 0 |
# 先看整体路线：
# 第 1 步：用列表写出温度公式。
# 第 2 步：在Series上完成同一公式并新增列。
# 第 3 步：用where处理零销售额，再结合NumPy函数。

import numpy as np
import pandas as pd
data=pd.DataFrame({"item":["A","B","C"],"fahrenheit":[32,212,68],"amount":[100,200,0],"cost":[60,150,0]})
print('\n===== [(f-32)*5/9 for f in data["fahrenheit"]] =====')
print([(f-32)*5/9 for f in data["fahrenheit"]])
data["celsius"]=(data["fahrenheit"]-32)*5/9
# 括号决定公式顺序；Series与标量算术保留原index。
print('\n===== data[["item","celsius"]].to_markdown(index=False) =====')
print(data[["item","celsius"]].to_markdown(index=False))
data["profit"]=data["amount"]-data["cost"]
# where(cond)在条件为False处替换成缺失；零销售额的利润率不定义为0。
denominator=data["amount"].where(data["amount"]!=0)
data["margin"]=data["profit"]/denominator
print('\n===== data.to_markdown(index=False) =====')
print(data.to_markdown(index=False))
# np.sqrt等一元函数可以对数值Series逐项运算；这里示例展示非负收入平方根。
print('\n===== np.sqrt(data["amount"]) =====')
print(np.sqrt(data["amount"]))
assert data["celsius"].tolist()==[0,100,20]
assert pd.isna(data.loc[2,"margin"])

# 学完先自己回答，再看下面的参考答案：
# 1. 这个知识点解决什么类型的问题？
# 2. 为什么当前案例需要它？
# 3. 每一步代码为什么要在此时出现？
# 4. 如果换一种做法，代价和风险是什么？

# 参考答案：
# 1. 给整列应用相同计算规则。
# 2. 每条记录公式相同，但零分母需要明确业务定义。
# 3. 先验证公式，再生成列，利润算出后才能求利润率。
# 4. 循环灵活但重复；无条件除法虽短，却可能把无穷或未定义值当有效指标。

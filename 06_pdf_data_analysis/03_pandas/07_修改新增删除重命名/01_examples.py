"""案例驱动示例：修正订单并整理字段"""
# 对应 PDF：13-pandas-full.pdf 第 8、24—26、39 页
# 任务：修正B订单成本，新增利润，删除临时列，再改成中文字段。
# 每次操作都应明确是在修改原表，还是得到一个新结果。
# 案例数据：
# | order_id | amount | cost | temp |
# |---|---:|---:|---|
# | A | 100 | 60 | x |
# | B | 200 | 150 | y |
# 先看整体路线：
# 第 1 步：定位错误订单，用loc直接赋值。
# 第 2 步：基于两个数值列生成利润列。
# 第 3 步：用drop和rename返回整理后的表。

import pandas as pd
data=pd.DataFrame({"order_id":["A","B"],"amount":[100,200],"cost":[60,150],"temp":["x","y"]})
# 对字典列表要循环判断订单；loc把行条件和列名放在同一次赋值中。
data.loc[data["order_id"]=="B","cost"]=140
# 避免data[条件]["cost"]=...这样的链式赋值，无法可靠表达修改原表。
data["profit"]=data["amount"]-data["cost"]
print('\n===== data.to_markdown(index=False) =====')
print(data.to_markdown(index=False))
# Series新列按index对齐，列表新列按位置匹配，长度与行数要对应。
data["checked"]=pd.Series([True,False],index=data.index)
print('\n===== data.to_markdown(index=False) =====')
print(data.to_markdown(index=False))
# drop(columns=[...])默认返回新表，原data仍含temp。
clean=data.drop(columns=["temp"])
print('\n===== clean.to_markdown(index=False) =====')
print(clean.to_markdown(index=False))
print('\n===== data.columns.tolist() =====')
print(data.columns.tolist())
renamed=clean.rename(columns={"amount":"销售额","profit":"利润"})
print('\n===== renamed.to_markdown(index=False) =====')
print(renamed.to_markdown(index=False))
# inplace=True可就地操作，但返回None，不能写data=data.drop(...,inplace=True)。
# 版本提示：本机Pandas 3.1已对inplace参数发弃用警告；下面只为读懂PDF旧写法。
# 新代码推荐clean=data.drop(...)，显式接收返回的新表。
assert renamed["利润"].tolist()==[40,60]
assert "temp" in data and "temp" not in clean
# 多行多列更新时，一维["待核查",0]会广播到每一条选中的行。
trial=data.copy()
trial.loc[[0,1],["order_id","profit"]]=["待核查",0]
print('\n===== trial.to_markdown(index=False) =====')
print(trial.to_markdown(index=False))
assert trial["profit"].tolist()==[0,0]
# inplace=True真的修改接收操作的那份表，返回值是None；这里在副本上演示。
inplace_trial=data.copy()
returned=inplace_trial.drop(columns=["temp"],inplace=True)
print('\n===== inplace_trial.to_markdown(index=False) =====')
print(inplace_trial.to_markdown(index=False))
assert returned is None and "temp" not in inplace_trial

# 学完先自己回答，再看下面的参考答案：
# 1. 这个知识点解决什么类型的问题？
# 2. 为什么当前案例需要它？
# 3. 每一步代码为什么要在此时出现？
# 4. 如果换一种做法，代价和风险是什么？

# 参考答案：
# 1. 定位修改记录并整理表字段。
# 2. 成本错了先修正，利润才有正确依据。
# 3. 先复制保留原始表，再修正成本、计算利润、整理展示字段。
# 4. 循环字典可改但不易批量检查；链式赋值和误接inplace返回值会造成错误。

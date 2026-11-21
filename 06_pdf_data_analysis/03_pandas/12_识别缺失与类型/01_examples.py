"""案例驱动示例：缺失不是零分，非法文本也不是数字"""
# 对应 PDF：13-pandas-full.pdf 第 41—42 页；to_numeric与可空整数为实用补充
# 任务：清理成绩中的空白与文字，分别识别合法数字、缺失和非法记录。
# 文本“缺考”可能有业务含义，转换前先保留原值，不能悄悄抹掉原因。
# 案例数据：
# | name | raw_score |
# |---|---|
# | A | 80 |
# | B | 缺考 |
# | C | 空值(None) |
# | D | 0 |
# 先看整体路线：
# 第 1 步：先用原列观察类型和缺失。
# 第 2 步：用to_numeric转换，比较raise与coerce。
# 第 3 步：检测非法文本与真正零分，并转换为可空整数。

import numpy as np
import pandas as pd
data=pd.DataFrame({"name":["A","B","C","D"],"raw_score":["80","缺考",None,"0"]})
print('\n===== data.dtypes =====')
print(data.dtypes)
print('\n===== data.isna().to_markdown(index=False) =====')
print(data.isna().to_markdown(index=False))
# isna/isnull是同义方法，notna/notnull是对应的非缺失判断。
print('\n===== data["raw_score"].notna() =====')
print(data["raw_score"].notna())
# errors="coerce"将无法解析的文本变成NaN；不修改raw_score原列。
data["score"]=pd.to_numeric(data["raw_score"],errors="coerce")
print('\n===== data.to_markdown(index=False) =====')
print(data.to_markdown(index=False))
# 原值非空而转换后为空，才是本次转换失败的记录。
invalid=data["raw_score"].notna()&data["score"].isna()
print('\n===== data.loc[invalid].to_markdown(index=False) =====')
print(data.loc[invalid].to_markdown(index=False))
# errors="raise"只在存在非法数据时抛错；全是合法数字时正常运行。
print('\n===== pd.to_numeric(pd.Series(["80","0"]),errors="raise") =====')
print(pd.to_numeric(pd.Series(["80","0"]),errors="raise"))
# 不执行下面这行，以便整节正常运行：pd.to_numeric(data["raw_score"],errors="raise")
# 普通float列用NaN表示缺失，因此80可能显示80.0；不代表分数被加了小数。
data["score_nullable"]=data["score"].astype("Int64")
print('\n===== data.to_markdown(index=False) =====')
print(data.to_markdown(index=False))
assert data["score"].isna().sum()==2
assert data.loc[3,"score"]==0
# NaN不能用==识别：np.nan==np.nan是False，应该用isna。

# 学完先自己回答，再看下面的参考答案：
# 1. 这个知识点解决什么类型的问题？
# 2. 为什么当前案例需要它？
# 3. 每一步代码为什么要在此时出现？
# 4. 如果换一种做法，代价和风险是什么？

# 参考答案：
# 1. 区分合法数值、真实缺失和无法解析的文本。
# 2. 0分与未录入不能一起删除，缺考也要留痕。
# 3. 先保留原列，再转换，再用转换前后的掩码定位原因，最后选合适dtype。
# 4. 直接强转遇文字会报错；coerce虽方便，但不检查失败记录会掩盖数据质量问题。

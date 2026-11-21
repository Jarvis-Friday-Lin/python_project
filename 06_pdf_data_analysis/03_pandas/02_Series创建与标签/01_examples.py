"""案例驱动示例：从不同来源建立同一列成绩"""
# 对应 PDF：13-pandas-full.pdf 第 4—10、38 页
# 任务：从列表、字典与NumPy数组导入同一列成绩，并修正小周成绩。
# 标签用于识别人，位置用于排队顺序；这两种编号不能混为一谈。
# 案例数据：
# | 标签 | 分数 |
# |---|---:|
# | 小林 | 95 |
# | 小周 | 84 |
# | 小陈 | 90 |
# 先看整体路线：
# 第 1 步：对比列表、字典、数组构造Series。
# 第 2 步：读取index、values与name。
# 第 3 步：通过loc和iloc读写并练习切片和多选。

import numpy as np
import pandas as pd
names=["小林","小周","小陈"]
s=pd.Series([95,84,90],index=names,name="Python")
from_dict=pd.Series({"小林":95,"小周":84,"小陈":90},name="Python")
from_array=pd.Series(np.array([95,84,90]),index=names,name="Python")
print('\n===== s =====')
print(s)
print('\n===== s.index =====')
print(s.index)
print('\n===== s.values =====')
print(s.values)
# to_numpy显式表示转换；数值型普通Series在这里可得到ndarray。
print('\n===== s.to_numpy() =====')
print(s.to_numpy())
print('\n===== s.loc["小周"] =====')
print(s.loc["小周"])
print('\n===== s.iloc[1] =====')
print(s.iloc[1])
print('\n===== s.loc["小林":"小周"] =====')
print(s.loc["小林":"小周"])
print('\n===== s.iloc[0:2] =====')
print(s.iloc[0:2])
print('\n===== s.loc[["小陈","小林"]] =====')
print(s.loc[["小陈","小林"]])
# 标签切片包含结束标签，位置切片不包含结束位置。
s.loc["小周"]=85
s.iloc[0]=96
print('\n===== s =====')
print(s)
assert from_dict.equals(from_array)
assert s.loc["小周"]==85
# Series构造时index长度必须匹配；不要用s[1]含糊表达标签或位置。
# 布尔掩码也能更新Series；先复制，避免把本节的原分数改成标记值。
trial=s.copy()
trial.loc[trial<90]=0
print('\n===== trial =====')
print(trial)
# Index的union/intersection按标签做并集/交集，不是逐元素相加。
other=pd.Index(["小周","小李"])
print('\n===== s.index.union(other) =====')
print(s.index.union(other))
print('\n===== s.index.intersection(other) =====')
print(s.index.intersection(other))
assert trial.loc["小周"]==0 and s.loc["小周"]==85

# 学完先自己回答，再看下面的参考答案：
# 1. 这个知识点解决什么类型的问题？
# 2. 为什么当前案例需要它？
# 3. 每一步代码为什么要在此时出现？
# 4. 如果换一种做法，代价和风险是什么？

# 参考答案：
# 1. 从不同容器创建带身份标签的列。
# 2. 修正的是小周本人，不是永远排第二的人。
# 3. 先建立标签再读取核对，定位无误后赋值，最后比较切片边界。
# 4. 纯数组只有位置，身份信息要另存；Series自动对齐带来便利，也要求标签正确。

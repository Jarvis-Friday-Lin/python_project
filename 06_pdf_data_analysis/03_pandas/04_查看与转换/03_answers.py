"""参考答案：接到一张表先检查什么"""
# 对应 PDF：13-pandas-full.pdf 第 18—20 页；补充head/info/describe用于检查
# 建议先完成 02_exercises.py；下面的实现与该题数据、要求一一对应。

import pandas as pd
data=pd.DataFrame({"name":["小林","小周","小陈","小李"],"city":["上海","北京","上海","深圳"],"score":[95,84,90,75]})
print('\n===== data.head(2).to_markdown(index=False) =====')
print(data.head(2).to_markdown(index=False))
print('\n===== data.shape =====')
print(data.shape)
print('\n===== data.dtypes =====')
print(data.dtypes)
print('\n===== data.info() =====')
data.info()
summary=data.describe(include="all")
print('\n===== summary.to_markdown() =====')
print(summary.to_markdown())
assert summary.loc["count","city"]==4 and summary.loc["unique","city"]==3
assert summary.loc["top","city"]=="上海" and summary.loc["freq","city"]==2
assert summary.loc["mean","score"]==86
assert data[["score"]].to_numpy().shape==(4,1)

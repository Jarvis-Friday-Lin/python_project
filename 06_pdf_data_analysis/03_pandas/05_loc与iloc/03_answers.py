"""参考答案：按身份与按位置选行列"""
# 对应 PDF：13-pandas-full.pdf 第 6、9、20—22、38—40 页
# 建议先完成 02_exercises.py；下面的实现与该题数据、要求一一对应。

import pandas as pd
data=pd.DataFrame({"city":["上海","北京","上海","深圳"],"score":[95,84,90,75]},index=["小林","小周","小陈","小李"])
assert data.loc["小周","score"]==data.iloc[1,1]==data.at["小周","score"]==data.iat[1,1]==84
print('\n===== data.iloc[:2,:].to_markdown() =====')
print(data.iloc[:2,:].to_markdown())
chosen=data.loc[["小李","小林"],["score"]]
print('\n===== chosen.to_markdown() =====')
print(chosen.to_markdown())
assert chosen.shape==(2,1) and chosen["score"].tolist()==[75,95]
assert isinstance(data.loc["小周"],pd.Series)
assert isinstance(data.loc[["小周"]],pd.DataFrame)

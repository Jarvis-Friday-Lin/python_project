"""参考答案：有标签的成绩与学生表"""
# 对应 PDF：13-pandas-full.pdf 第 2—5、12 页
# 建议先完成 02_exercises.py；下面的实现与该题数据、要求一一对应。

import pandas as pd
data=pd.DataFrame({"name":["小林","小周","小陈","小李"],"city":["上海","北京","上海","深圳"],"score":[95,84,90,75]})
scores=pd.Series([95,84,90,75],index=["小林","小周","小陈","小李"],name="Python")
print('\n===== data.loc[data["score"]>=85].to_markdown(index=False) =====')
print(data.loc[data["score"]>=85].to_markdown(index=False))
assert scores.mean()==data["score"].mean()==86
assert data.loc[data["score"]>=85,"name"].tolist()==["小林","小陈"]
assert isinstance(data["score"],pd.Series) and data["score"].shape==(4,)
assert isinstance(data[["score"]],pd.DataFrame) and data[["score"]].shape==(4,1)

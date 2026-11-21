"""参考答案：从不同来源建立同一列成绩"""
# 对应 PDF：13-pandas-full.pdf 第 4—10、38 页
# 建议先完成 02_exercises.py；下面的实现与该题数据、要求一一对应。

import numpy as np
import pandas as pd
s=pd.Series([95,84,90],index=["小林","小周","小陈"],name="Python")
d=pd.Series({"小林":95,"小周":84,"小陈":90},name="Python")
a=pd.Series(np.array([95,84,90]),index=s.index,name="Python")
assert s.equals(d) and s.equals(a)
assert s.loc["小周"]==s.iloc[1]==84
s.loc["小周"]=85
print('\n===== s.loc[["小陈","小林"]] =====')
print(s.loc[["小陈","小林"]])
assert s.loc[["小陈","小林"]].tolist()==[90,95]
assert s.loc["小林":"小周"].tolist()==s.iloc[:2].tolist()==[95,85]

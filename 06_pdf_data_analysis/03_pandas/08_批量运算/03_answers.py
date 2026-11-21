"""参考答案：温度换算与销售利润率"""
# 对应 PDF：13-pandas-full.pdf 第 28 页
# 建议先完成 02_exercises.py；下面的实现与该题数据、要求一一对应。

import numpy as np
import pandas as pd
data=pd.DataFrame({"item":["A","B","C"],"fahrenheit":[32,212,68],"amount":[100,200,0],"cost":[60,150,0]})
data["celsius"]=(data["fahrenheit"]-32)*5/9
data["profit"]=data["amount"]-data["cost"]
data["margin"]=data["profit"]/data["amount"].where(data["amount"]!=0)
print('\n===== data.to_markdown(index=False) =====')
print(data.to_markdown(index=False))
assert data["celsius"].tolist()==[0,100,20]
assert data["profit"].tolist()==[40,50,0]
assert np.allclose(data["margin"].iloc[:2],[.4,.25])
assert pd.isna(data.loc[2,"margin"])

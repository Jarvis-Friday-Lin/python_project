"""参考答案：修正订单并整理字段"""
# 对应 PDF：13-pandas-full.pdf 第 8、24—26、39 页
# 建议先完成 02_exercises.py；下面的实现与该题数据、要求一一对应。

import pandas as pd
original=pd.DataFrame({"order_id":["A","B"],"amount":[100,200],"cost":[60,150],"temp":["x","y"]})
data=original.copy()
data.loc[data["order_id"]=="B","cost"]=140
data["profit"]=data["amount"]-data["cost"]
clean=data.drop(columns=["temp"]).rename(columns={"amount":"销售额"})
print('\n===== clean.to_markdown(index=False) =====')
print(clean.to_markdown(index=False))
assert original.loc[1,"cost"]==150 and clean.loc[1,"cost"]==140
assert clean["profit"].tolist()==[40,60]
assert "temp" not in clean and "销售额" in clean and "amount" not in clean

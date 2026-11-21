"""参考答案：选出符合业务要求的订单"""
# 对应 PDF：13-pandas-full.pdf 第 10、23、39—40 页
# 建议先完成 02_exercises.py；下面的实现与该题数据、要求一一对应。

import pandas as pd
data=pd.DataFrame({"order_id":["S001","S002","S003","S004"],"city":["上海","北京","上海","深圳"],"product":["键盘","鼠标","显示器","耳机"],"amount":[798,1200,1800,650]})
selected=data.loc[data["amount"]>1000,["order_id","city","amount"]]
print('\n===== selected.to_markdown(index=False) =====')
print(selected.to_markdown(index=False))
assert selected["order_id"].tolist()==["S002","S003"]
assert len(data[(data["city"]=="上海")&(data["amount"]>=1000)])==1
assert len(data[(data["city"]=="上海")|(data["city"]=="北京")])==3
assert len(data[~(data["city"]=="上海")])==2
assert len(data[data["city"].isin(["上海","北京"])])==3
assert len(data[data["amount"].between(650,1200)])==3
assert data.loc[data["amount"]>2000,["order_id","city","amount"]].shape==(0,3)

"""参考答案：按城市统计销售额与订单数"""
# 对应 PDF：13-pandas-full.pdf 第 45—46 页
# 建议先完成 02_exercises.py；下面的实现与该题数据、要求一一对应。

import pandas as pd
data=pd.DataFrame({"order_id":["A","B","C","D"],"city":["上海","北京","上海","北京"],"amount":[100,200,300,None]})
result=data.groupby("city",as_index=False).agg(total=("amount","sum"),average=("amount","mean"),valid_amounts=("amount","count"),orders=("order_id","size"))
print('\n===== result.to_markdown(index=False) =====')
print(result.to_markdown(index=False))
lookup=result.set_index("city")
assert lookup.loc["上海",["total","average","valid_amounts","orders"]].tolist()==[400,200,2,2]
assert lookup.loc["北京",["total","average","valid_amounts","orders"]].tolist()==[200,200,1,2]
assert "city" in result.columns

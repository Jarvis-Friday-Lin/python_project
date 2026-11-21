"""参考答案：从记录、列与数组建立订单表"""
# 对应 PDF：13-pandas-full.pdf 第 13—17 页
# 建议先完成 02_exercises.py；下面的实现与该题数据、要求一一对应。

import numpy as np
import pandas as pd
a=pd.DataFrame([{"order_id":"S001","amount":100},{"order_id":"S002","amount":200}])
b=pd.DataFrame({"order_id":["S001","S002"],"amount":[100,200]})
assert a.equals(b)
s=pd.DataFrame({"amount":pd.Series([100,200],index=["S001","S002"])})
n=pd.DataFrame(np.array([[100],[200]]),index=["S001","S002"],columns=["amount"])
assert s.equals(n)
s["cost"]=pd.Series([60],index=["S001"])
print('\n===== s.to_markdown() =====')
print(s.to_markdown())
assert pd.isna(s.loc["S002","cost"])

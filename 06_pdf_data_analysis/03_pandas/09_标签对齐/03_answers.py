"""参考答案：顺序不同的商品如何相加"""
# 对应 PDF：13-pandas-full.pdf 第 14、29—30 页
# 建议先完成 02_exercises.py；下面的实现与该题数据、要求一一对应。

import pandas as pd
jan=pd.Series([100,200],index=["A","B"])
feb=pd.Series([30,40],index=["B","C"])
default=jan+feb
total=jan.add(feb,fill_value=0)
print('\n===== default =====')
print(default)
print('\n===== total =====')
print(total)
assert default.loc["B"]==230 and default.isna().sum()==2
assert total.to_dict()=={"A":100.,"B":230.,"C":40.}
pd.testing.assert_series_equal(total,jan.add(feb.iloc[::-1],fill_value=0))

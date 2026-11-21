"""参考答案：用月份标签管理降雨量"""
# 对应 PDF：13-pandas-full.pdf 第 4—10、38 页
# 课件核心：第4—10、38页：三种Series来源、loc/iloc、赋值、标签与位置切片。
# 扩展：无。
# 案例数据（据此自行创建对象，不能照抄 examples 的数据）：
# | month | rain_mm |
# |---|---|
# | Jan | 15 |
# | Feb | 28 |
# | Mar | 12 |
# | Apr | 35 |
# 建议先做练习，再逐段对照下面的实现；assert 用于验证结果。

import numpy as np
import pandas as pd
labels, values = ['Jan','Feb','Mar','Apr'], [15,28,12,35]
s1 = pd.Series(values,index=labels)
s2 = pd.Series(dict(zip(labels,values)))
s3 = pd.Series(np.array(values),index=labels)
assert s1.equals(s2) and s2.equals(s3)
assert s1.loc['Feb'] == s1.iloc[1] == 28
s1.loc['Feb'] = 30
print("\n===== s1.loc[['Apr', 'Jan']] =====")
print(s1.loc[['Apr','Jan']])
print("\n===== s1.loc['Jan':'Mar'] =====")
print(s1.loc['Jan':'Mar'])
assert s1.loc[['Apr','Jan']].tolist() == [35,15]
assert s1.loc['Jan':'Mar'].equals(s1.iloc[0:3])
assert s2.loc['Feb'] == s3.loc['Feb'] == 28
# loc标签切片含终点；iloc位置切片不含终点，不能照搬同一个终止数字。

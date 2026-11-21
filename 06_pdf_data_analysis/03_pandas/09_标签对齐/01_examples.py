"""案例驱动示例：顺序不同的商品如何相加"""
# 对应 PDF：13-pandas-full.pdf 第 14、29—30 页
# 任务：汇总两个月商品销售额，但名单与顺序不同。
# Pandas先按标签对齐再计算；“缺少记录”是否等于0，需要业务决定。
# 案例数据：
# | 商品 | 一月 | 二月 |
# |---|---:|---:|
# | A | 100 | 无记录 |
# | B | 200 | 30 |
# | C | 无记录 | 40 |
# 先看整体路线：
# 第 1 步：先展示按位置硬加为什么错。
# 第 2 步：使用标签对齐识别同商品。
# 第 3 步：比较默认缺失与fill_value=0，并扩展到二维行列对齐。

import pandas as pd
jan=pd.Series([100,200],index=["A","B"],name="sales")
feb=pd.Series([30,40],index=["B","C"],name="sales")
print('\n===== jan.to_numpy()+feb.to_numpy() =====')
print(jan.to_numpy()+feb.to_numpy())
# 上一行把A+B、B+C相加，数值看起来正常，业务却错了。
print('\n===== jan+feb =====')
print(jan+feb)
# 默认只有双方都有值的B能求和，A/C是缺失。
# add(other,fill_value=0)把单方缺少的数据当0，仅适用于已确认“未出现即无销售”。
total=jan.add(feb,fill_value=0)
print('\n===== total =====')
print(total)
left=pd.DataFrame({"sales":jan,"cost":pd.Series([60,150],index=["A","B"])})
right=pd.DataFrame({"sales":feb,"units":pd.Series([3,4],index=["B","C"])})
print('\n===== (left+right).to_markdown() =====')
print((left+right).to_markdown())
# DataFrame同时对齐行和列；右表没有cost，不能自动解释成0成本。
assert total.to_dict()=={"A":100.,"B":230.,"C":40.}
assert pd.isna((jan+feb).loc["A"])

# 学完先自己回答，再看下面的参考答案：
# 1. 这个知识点解决什么类型的问题？
# 2. 为什么当前案例需要它？
# 3. 每一步代码为什么要在此时出现？
# 4. 如果换一种做法，代价和风险是什么？

# 参考答案：
# 1. 按身份匹配记录，而非按偶然的位置配对。
# 2. 两个月商品名单不完全相同。
# 3. 先演示位置相加错误，再看标签对齐，最后依据业务选择是否补0。
# 4. 转NumPy会失去标签对齐；补0更完整但可能掩盖漏报，必须有业务依据。

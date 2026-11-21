"""案例驱动示例：选出符合业务要求的订单"""
# 对应 PDF：13-pandas-full.pdf 第 10、23、39—40 页
# 任务：选销售额大于1000的订单，再比较上海且达标、上海或北京、非上海、区间和名单筛选。
# 每个条件都先产生布尔Series，组合后交给loc保留指定字段。
# 案例数据：
# | order_id | city | product | amount |
# |---|---|---|---:|
# | S001 | 上海 | 键盘 | 798 |
# | S002 | 北京 | 鼠标 | 1200 |
# | S003 | 上海 | 显示器 | 1800 |
# | S004 | 深圳 | 耳机 | 650 |
# 先看整体路线：
# 第 1 步：先用列表条件提取订单。
# 第 2 步：将比较结果与&、|、~组合。
# 第 3 步：补齐isin、between、缺失检查，并只输出需要的列。

import pandas as pd
data=pd.DataFrame({"order_id":["S001","S002","S003","S004"],"city":["上海","北京","上海","深圳"],
                   "product":["键盘","鼠标","显示器","耳机"],"amount":[798,1200,1800,650]})
rows=data.to_dict("records")
print('\n===== [r["order_id"] for r in rows if r["amount"]>1000] =====')
print([r["order_id"] for r in rows if r["amount"]>1000])
# &并且、|或者、~取反都逐行作用；每个比较表达式必须单独括号包住。
print('\n===== data.loc[(data["city"]=="上海")&(data["amount"]>=1000),["order_id","city","amount"]].to_markdown(index=False) =====')
print(data.loc[(data["city"]=="上海")&(data["amount"]>=1000),["order_id","city","amount"]].to_markdown(index=False))
print('\n===== data.loc[(data["city"]=="上海")|(data["city"]=="北京")].to_markdown(index=False) =====')
print(data.loc[(data["city"]=="上海")|(data["city"]=="北京")].to_markdown(index=False))
print('\n===== data.loc[~(data["city"]=="上海")].to_markdown(index=False) =====')
print(data.loc[~(data["city"]=="上海")].to_markdown(index=False))
# isin(values) 对名单成员筛选；between(left,right,inclusive)控制区间边界。
print('\n===== data.loc[data["city"].isin(["上海","北京"])].to_markdown(index=False) =====')
print(data.loc[data["city"].isin(["上海","北京"])].to_markdown(index=False))
print('\n===== data.loc[data["amount"].between(650,1200,inclusive="both")].to_markdown(index=False) =====')
print(data.loc[data["amount"].between(650,1200,inclusive="both")].to_markdown(index=False))
# notna保留有记录的数据，与“非零”不是同一个条件。
print('\n===== data[data["amount"].notna()].to_markdown(index=False) =====')
print(data[data["amount"].notna()].to_markdown(index=False))
# query是表达式字符串入口；外部变量用@，列名特殊时需反引号，复杂逻辑先用loc更好检查。
threshold=1000
print('\n===== data.query("amount > @threshold")[["order_id","amount"]].to_markdown(index=False) =====')
print(data.query("amount > @threshold")[["order_id","amount"]].to_markdown(index=False))
assert data.loc[data["amount"]>1000,"order_id"].tolist()==["S002","S003"]

# 学完先自己回答，再看下面的参考答案：
# 1. 这个知识点解决什么类型的问题？
# 2. 为什么当前案例需要它？
# 3. 每一步代码为什么要在此时出现？
# 4. 如果换一种做法，代价和风险是什么？

# 参考答案：
# 1. 把业务条件转成可检查的行筛选。
# 2. 城市与金额同时限制，最后还要保留订单编号。
# 3. 先写单条件确保字段正确，再组合布尔条件，最后选择展示列。
# 4. 循环能做但需维护字段输出；query简短却多了字符串语法，复杂条件先loc更直观。

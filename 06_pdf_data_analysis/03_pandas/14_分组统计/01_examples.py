"""案例驱动示例：按城市统计销售额与订单数"""
# 对应 PDF：13-pandas-full.pdf 第 45—46 页
# 任务：比较城市销售额、平均每单金额和订单数。
# 分组不是循环套一个sum那么简单：缺失金额是否计入订单数也影响结果。
# 案例数据：
# | order_id | city | amount |
# |---|---|---:|
# | A | 上海 | 100 |
# | B | 北京 | 200 |
# | C | 上海 | 300 |
# | D | 北京 | 缺失 |
# 先看整体路线：
# 第 1 步：先用字典累计各城市金额。
# 第 2 步：查看groupby对象及每组记录。
# 第 3 步：命名聚合得到报表，区分count与size。

import pandas as pd
data=pd.DataFrame({"order_id":["A","B","C","D"],"city":["上海","北京","上海","北京"],"amount":[100,200,300,None]})
manual={}
for row in data.to_dict("records"):
    if pd.notna(row["amount"]):
        manual[row["city"]]=manual.get(row["city"],0)+row["amount"]
print('\n===== manual =====')
print(manual)
# groupby(by)返回分组对象，暂时还不是汇总表。
grouped=data.groupby("city",sort=False)
for city,group in grouped:
    print('\n===== city =====')
    print(city)
    print('\n===== group.to_markdown(index=False) =====')
    print(group.to_markdown(index=False))
# 命名聚合：结果列名=(原字段,函数)，能一次展示不同统计。
summary=grouped.agg(total=("amount","sum"),average=("amount","mean"),
                    valid_amounts=("amount","count"),orders=("order_id","size")).reset_index()
print('\n===== summary.to_markdown(index=False) =====')
print(summary.to_markdown(index=False))
# count不数缺失金额，size数记录数；北京两条订单只有一条有效金额。
print('\n===== data.groupby(["city","order_id"],as_index=False)["amount"].sum(min_count=1).to_markdown(index=False) =====')
print(data.groupby(["city","order_id"],as_index=False)["amount"].sum(min_count=1).to_markdown(index=False))
# reset_index把分组键从索引变回普通列；as_index=False也能保持分组键为列。
assert summary.set_index("city").loc["上海","total"]==400

# 学完先自己回答，再看下面的参考答案：
# 1. 这个知识点解决什么类型的问题？
# 2. 为什么当前案例需要它？
# 3. 每一步代码为什么要在此时出现？
# 4. 如果换一种做法，代价和风险是什么？

# 参考答案：
# 1. 按类别把多条记录汇总成一条报告。
# 2. 要比较城市表现，而不是只知道全部总金额。
# 3. 基础累计说明分组原理，先看每组再聚合，最后把键还原为列便于输出。
# 4. 手工字典需为每种统计增加状态；默认count可能把缺失记录排除导致误读订单量。

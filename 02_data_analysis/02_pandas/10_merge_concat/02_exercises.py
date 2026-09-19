"""动手练习：merge、join 与 concat

业务任务：连接订单表和商品表，并检查未匹配的商品编号。

本题完成要求：
1. 根据下方的 Markdown 数据创建 orders 和 customers 两张表。
2. 分别尝试 inner、left 和 outer merge，比较保留的订单。
3. 使用 indicator 找出未匹配记录，并用 validate 检查连接关系。
4. 使用 concat 按行和按列拼接，比较 axis 与 ignore_index 的效果。
"""

import pandas as pd


def main():
    # 下面只提供案例数据，不直接提供 DataFrame 代码。
    # 请先阅读并理解字段，再亲自把它写成 pd.DataFrame，这是本节练习的一部分。
    # 可以先运行你写出的数据，再增加一行、修改一个边界值，观察结果如何变化。
    # 案例数据：
    # 订单表 orders：
    # 
    # | customer_id | amount |
    # |---:|---:|
    # | 1 | 100 |
    # | 2 | 200 |
    # | 3 | 150 |
    # 
    # 客户表 customers：
    # 
    # | customer_id | name |
    # |---:|---|
    # | 1 | 甲 |
    # | 2 | 乙 |
    # TODO：根据上面的数据，自己编写 pd.DataFrame(...)。
    # TODO：再使用 DataFrame 完成业务任务。
    # TODO：把每个关键步骤拆成清晰的中间变量。
    # TODO：运行后检查结果是否真的回答了业务问题。
    pass


if __name__ == "__main__":
    main()

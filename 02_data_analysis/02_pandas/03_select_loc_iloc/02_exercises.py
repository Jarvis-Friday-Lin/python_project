"""动手练习：选择数据：loc 与 iloc

业务任务：选择销售额大于 1000 的订单编号、城市和销售额。

本题完成要求：
1. 根据下方的 Markdown 表格创建订单 DataFrame。
2. 使用 loc 筛选销售额大于 1000 的订单，并只保留 order_id、city、amount。
3. 使用 iloc 取前两行，比较 loc 与 iloc 的选择依据。
4. 打印结果类型和 shape，并增加一个没有符合条件订单的边界案例。
"""

import pandas as pd


def main():
    # 下面只提供案例数据，不直接提供 DataFrame 代码。
    # 请先阅读并理解字段，再亲自把它写成 pd.DataFrame，这是本节练习的一部分。
    # 可以先运行你写出的数据，再增加一行、修改一个边界值，观察结果如何变化。
    # 案例数据：
    # | order_id | city | product | amount |
    # |---|---|---|---:|
    # | S001 | 上海 | 键盘 | 798 |
    # | S002 | 北京 | 鼠标 | 1200 |
    # | S003 | 上海 | 显示器 | 1800 |
    # | S004 | 深圳 | 耳机 | 650 |
    # TODO：根据上面的数据，自己编写 pd.DataFrame(...)。
    # TODO：再使用 DataFrame 完成业务任务。
    # TODO：把每个关键步骤拆成清晰的中间变量。
    # TODO：运行后检查结果是否真的回答了业务问题。
    pass


if __name__ == "__main__":
    main()

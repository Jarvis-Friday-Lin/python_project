"""动手练习：透视表与交叉表

业务任务：制作月份×商品类别的销售额透视表。

本题完成要求：
1. 根据下方的 Markdown 数据创建长格式销售 DataFrame。
2. 使用 pivot_table 指定 values、index、columns 和 aggfunc。
3. 使用 crosstab 统计频数，并比较 normalize 前后的结果。
4. 增加一个重复的城市与商品组合，观察 pivot 和 pivot_table 的区别。
"""

import pandas as pd


def main():
    # 下面只提供案例数据，不直接提供 DataFrame 代码。
    # 请先阅读并理解字段，再亲自把它写成 pd.DataFrame，这是本节练习的一部分。
    # 可以先运行你写出的数据，再增加一行、修改一个边界值，观察结果如何变化。
    # 案例数据：
    # | city | product | amount |
    # |---|---|---:|
    # | 上海 | A | 100 |
    # | 上海 | B | 200 |
    # | 北京 | A | 150 |
    # TODO：根据上面的数据，自己编写 pd.DataFrame(...)。
    # TODO：再使用 DataFrame 完成业务任务。
    # TODO：把每个关键步骤拆成清晰的中间变量。
    # TODO：运行后检查结果是否真的回答了业务问题。
    pass


if __name__ == "__main__":
    main()

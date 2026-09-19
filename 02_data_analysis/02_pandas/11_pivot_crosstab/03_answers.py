"""参考答案：透视表与交叉表

这份文件用于自我核对，不要求你写出完全相同的代码。
核对时请思考：如果输入为空、含缺失值或列名改变，代码需要怎样调整？
"""

import pandas as pd


def main():
    # 以下是本节核心操作的参考实现。
    import pandas as pd
    data = pd.DataFrame({"city": ["上海", "上海", "北京"], "product": ["A", "B", "A"], "amount": [100, 200, 150]})
    # pivot_table 按 index/columns 重塑表格，values 是要汇总的列，aggfunc="sum" 指定求和。
    print(pd.pivot_table(data, values="amount", index="city", columns="product", aggfunc="sum", fill_value=0).to_markdown())
    # crosstab 统计两个分类字段的频数，这里回答“每个城市有多少种商品记录”。
    print(pd.crosstab(data["city"], data["product"]).to_markdown())


if __name__ == "__main__":
    main()

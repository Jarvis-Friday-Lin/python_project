"""参考答案：merge、join 与 concat

这份文件用于自我核对，不要求你写出完全相同的代码。
核对时请思考：如果输入为空、含缺失值或列名改变，代码需要怎样调整？
"""

import pandas as pd


def main():
    # 以下是本节核心操作的参考实现。
    import pandas as pd
    orders = pd.DataFrame({"customer_id": [1, 2], "amount": [100, 200]})
    customers = pd.DataFrame({"customer_id": [1, 2], "name": ["甲", "乙"]})
    # merge 按 customer_id 连接两张表；how="left" 保留全部订单，validate 检查连接关系。
    print(orders.merge(customers, on="customer_id", how="left", validate="many_to_one").to_markdown(index=False))
    # concat 沿行方向拼接表；ignore_index=True 重新生成连续索引。
    print(pd.concat([orders, orders], ignore_index=True).to_markdown(index=False))


if __name__ == "__main__":
    main()

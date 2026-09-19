"""参考答案：新增、修改与删除列

这份文件用于自我核对，不要求你写出完全相同的代码。
核对时请思考：如果输入为空、含缺失值或列名改变，代码需要怎样调整？
"""

import pandas as pd


def main():
    # 以下是本节核心操作的参考实现。
    import pandas as pd
    data = pd.DataFrame({"price": [10, 20], "quantity": [3, 2]})
    # 用列名赋值会新增 amount；右侧是逐行相乘得到的 Series，长度与 data 行数一致。
    data["amount"] = data["price"] * data["quantity"]
    # loc[行条件, 列名] 只给满足条件的行写入 level，其余行暂时保持缺失。
    data.loc[data["amount"] >= 40, "level"] = "高"
    # fillna(value) 用 value 填补缺失等级，返回新 Series，需要重新赋回原列。
    data["level"] = data["level"].fillna("普通")
    print(data.to_markdown(index=False))


if __name__ == "__main__":
    main()

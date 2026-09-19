"""参考答案：选择数据：loc 与 iloc

这份文件用于自我核对，不要求你写出完全相同的代码。
核对时请思考：如果输入为空、含缺失值或列名改变，代码需要怎样调整？
"""

import pandas as pd


def main():
    # 以下是本节核心操作的参考实现。
    import pandas as pd
    data = pd.DataFrame({"name": ["甲", "乙", "丙"], "score": [88, 95, 76]})
    # loc[行条件, 列标签] 按标签选择；这里的行条件会保留 score >= 80 的行，列列表只保留 name 和 score。
    # 返回值是 DataFrame，因为我们选择了多列；如果只写 data.loc[条件, "name"]，结果会是 Series。
    print(data.loc[data["score"] >= 80, ["name", "score"]].to_markdown(index=False))
    # iloc[行位置, 列位置] 按整数位置选择；:2 表示第 0、1 行，: 表示保留所有列。
    # iloc 的切片终点不包含 2，返回仍是 DataFrame，因为这里保留了二维表结构。
    print(data.iloc[:2, :].to_markdown(index=False))


if __name__ == "__main__":
    main()

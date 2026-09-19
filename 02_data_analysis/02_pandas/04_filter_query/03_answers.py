"""参考答案：条件筛选与 query

这份文件用于自我核对，不要求你写出完全相同的代码。
核对时请思考：如果输入为空、含缺失值或列名改变，代码需要怎样调整？
"""

import pandas as pd


def main():
    # 以下是本节核心操作的参考实现。
    import pandas as pd
    data = pd.DataFrame({"city": ["上海", "北京", "上海"], "amount": [500, 1200, 1800]})
    # 先把条件拆开：每个比较表达式都会生成一列 True/False，便于单独检查。
    is_shanghai = data["city"] == "上海"
    is_expensive = data["amount"] >= 1000
    # & 表示逐行“并且”；两侧条件必须分别加括号，不能写 Python 的 and。
    selected_and = data[is_shanghai & is_expensive]
    print(selected_and.to_markdown(index=False))
    # | 表示逐行“或者”；~ 表示逐行取反，可以组合出“上海或金额达标”“不是上海”等条件。
    selected_or = data[(data["city"] == "上海") | (data["amount"] >= 1000)]
    selected_not = data[~(data["city"] == "上海")]
    print(selected_or.to_markdown(index=False))
    print(selected_not.to_markdown(index=False))
    # isin(values) 判断每行是否属于 values 列表，适合“城市在多个候选值中”的场景。
    selected_cities = data[data["city"].isin(["上海", "北京"])]
    print(selected_cities.to_markdown(index=False))
    # between(left, right, inclusive=...) 判断区间；inclusive="both" 表示包含两端。
    selected_range = data[data["amount"].between(500, 1500, inclusive="both")]
    print(selected_range.to_markdown(index=False))
    # query 接收字符串条件，列名可以直接写在字符串中；适合条件较长时提高可读性。
    selected_query = data.query("city == '上海' and amount >= 1000")
    print(selected_query.to_markdown(index=False))


if __name__ == "__main__":
    main()

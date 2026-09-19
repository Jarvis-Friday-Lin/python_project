"""参考答案：类型转换与缺失值

这份文件用于自我核对，不要求你写出完全相同的代码。
核对时请思考：如果输入为空、含缺失值或列名改变，代码需要怎样调整？
"""

import pandas as pd


def main():
    # 以下是本节核心操作的参考实现。
    import pandas as pd
    data = pd.DataFrame({"age": ["18", "错误", None], "score": [90, None, 80]})
    # to_numeric 的 errors="coerce" 会把无法转换的文本变成 NaN，而不是让程序直接报错。
    data["age"] = pd.to_numeric(data["age"], errors="coerce")
    # median() 求中位数；fillna(中位数) 用统计值补齐 score 的缺失项。
    data["score"] = data["score"].fillna(data["score"].median())
    print(data.to_markdown(index=False))
    print(data.isna().sum())


if __name__ == "__main__":
    main()

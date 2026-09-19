"""参考答案：map、apply 与 transform

这份文件用于自我核对，不要求你写出完全相同的代码。
核对时请思考：如果输入为空、含缺失值或列名改变，代码需要怎样调整？
"""

import pandas as pd


def main():
    # 以下是本节核心操作的参考实现。
    import pandas as pd
    data = pd.DataFrame({"group": ["A", "A", "B"], "score": [80, 100, 70]})
    # transform("mean") 计算组均值，但返回长度与原表相同，所以可以安全赋回新列。
    data["group_mean"] = data.groupby("group")["score"].transform("mean")
    # 逐行相减得到每条记录相对本组均值的差异。
    data["difference"] = data["score"] - data["group_mean"]
    print(data.to_markdown(index=False))


if __name__ == "__main__":
    main()

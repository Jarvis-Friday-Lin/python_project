"""参考答案：异常值处理与导出

这份文件用于自我核对，不要求你写出完全相同的代码。
核对时请思考：如果输入为空、含缺失值或列名改变，代码需要怎样调整？
"""

import pandas as pd


def main():
    # 以下是本节核心操作的参考实现。
    import pandas as pd
    values = pd.Series([10, 11, 12, 13, 100])
    # quantile([0.25, 0.75]) 一次取得 Q1、Q3；IQR 是两者之差。
    q1, q3 = values.quantile([0.25, 0.75])
    iqr = q3 - q1
    # 布尔条件标记异常值；这里先标记，不直接删除，方便后续业务复核。
    mask = (values < q1 - 1.5 * iqr) | (values > q3 + 1.5 * iqr)
    result = pd.DataFrame({"value": values, "is_outlier": mask})
    print(result.to_markdown(index=False))


if __name__ == "__main__":
    main()

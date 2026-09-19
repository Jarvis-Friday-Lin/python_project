"""参考答案：读取与观察数据

这份文件用于自我核对，不要求你写出完全相同的代码。
核对时请思考：如果输入为空、含缺失值或列名改变，代码需要怎样调整？
"""

import pandas as pd


def main():
    # 以下是本节核心操作的参考实现。
    from pathlib import Path
    import pandas as pd
    path = Path(__file__).resolve().parents[2] / "datasets" / "sales.csv"
    data = pd.read_csv(path)
    print(data.head().to_markdown(index=False))
    # info() 会直接把列名、非空数量和 dtype 打印出来；它主要用于检查结构，返回值本身是 None。
    data.info()
    # describe() 默认偏重数值列；include="all" 才会同时概览 price、quantity 等数值列和 city、product 等文本列。
    # count：非缺失值数量；unique：不同值数量；top：出现次数最多的值；freq：top 出现的次数。
    # mean/std/min/25%/50%/75%/max：数值列的平均值、标准差、最小值、四分位数、中位数、四分之三位数和最大值。
    # 文本列在这些数值统计位置会显示 NaN，这是“该统计不适用于文本”的意思，不是原数据凭空多了缺失。
    print(data.describe(include="all"))


if __name__ == "__main__":
    main()

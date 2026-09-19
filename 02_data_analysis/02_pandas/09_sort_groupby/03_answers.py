"""参考答案：排序、分组与聚合

这份文件用于自我核对，不要求你写出完全相同的代码。
核对时请思考：如果输入为空、含缺失值或列名改变，代码需要怎样调整？
"""

import pandas as pd


def main():
    # 以下是本节核心操作的参考实现。
    import pandas as pd
    data = pd.DataFrame({"city": ["上海", "北京", "上海"], "amount": [100, 200, 300]})
    # groupby("city") 按城市分组；as_index=False 让 city 继续作为普通列保留。
    summary = data.groupby("city", as_index=False).agg(
        # agg 中每个命名参数定义一个输出列：原列 amount 使用 size/sum/mean 计算不同指标。
        orders=("amount", "size"),
        total=("amount", "sum"),
        average=("amount", "mean"),
    )
    print(summary.sort_values("total", ascending=False).to_markdown(index=False))


if __name__ == "__main__":
    main()

"""动手练习：重复值与字符串清洗

业务任务：清理商品类别的空格和大小写后再统计唯一类别。

本题完成要求：
1. 根据下方的 Markdown 表格创建客户 DataFrame。
2. 使用 str.strip、lower 或 replace 统一文本格式。
3. 使用 duplicated 的不同 keep 参数观察重复标记，再用 drop_duplicates 去重。
4. 比较清洗前后的客户数量，并保留重复记录供复核。
"""

import pandas as pd


def main():
    # 下面只提供案例数据，不直接提供 DataFrame 代码。
    # 请先阅读并理解字段，再亲自把它写成 pd.DataFrame，这是本节练习的一部分。
    # 可以先运行你写出的数据，再增加一行、修改一个边界值，观察结果如何变化。
    # 案例数据：
    # | name | email |
    # |---|---|
    # |  Alice  | A@X.COM |
    # | alice | a@x.com |
    # | Bob | b@x.com |
    # TODO：根据上面的数据，自己编写 pd.DataFrame(...)。
    # TODO：再使用 DataFrame 完成业务任务。
    # TODO：把每个关键步骤拆成清晰的中间变量。
    # TODO：运行后检查结果是否真的回答了业务问题。
    pass


if __name__ == "__main__":
    main()

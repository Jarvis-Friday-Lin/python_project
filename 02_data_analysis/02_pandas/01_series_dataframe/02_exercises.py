"""动手练习：Series 与 DataFrame

业务任务：创建 students DataFrame，包含 name、class、math、python 四列；
再取出 python 成绩这一列，计算平均分，并筛选平均分不低于 85 的学生。

本题完成要求：
1. 根据 Markdown 表格创建 students DataFrame。
2. 分别取出 python 单列和多列结果，观察 Series 与 DataFrame 的区别。
3. 计算 Python 平均分，并筛选成绩不低于 85 分的完整记录。
4. 打印 type、shape、columns，并增加一名边界成绩为 85 分的学生。
"""

import pandas as pd


def main():
    # 案例数据（请自己把下面内容写成 pd.DataFrame）：
    # | name | class | math | python |
    # |---|---|---:|---:|
    # | 小林 | 一班 | 92 | 95 |
    # | 小周 | 一班 | 76 | 84 |
    # | 小陈 | 二班 | 85 | 90 |
    # | 小李 | 二班 | 68 | 75 |
    # TODO：根据上面的 Markdown 表格编写 students = pd.DataFrame(...)
    # TODO：取出 python 这一列，观察它是 Series 还是 DataFrame。
    # TODO：计算 python 平均分，并用条件筛选成绩不低于 85 的学生。
    # TODO：打印 type、shape 和筛选结果，验证自己的判断。
    pass


if __name__ == "__main__":
    main()

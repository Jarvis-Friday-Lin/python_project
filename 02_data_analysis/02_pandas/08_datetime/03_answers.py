"""参考答案：日期时间处理

这份文件用于自我核对，不要求你写出完全相同的代码。
核对时请思考：如果输入为空、含缺失值或列名改变，代码需要怎样调整？
"""

import pandas as pd


def main():
    # 以下是本节核心操作的参考实现。
    import pandas as pd
    data = pd.DataFrame({"date": ["2026-01-01", "2026-02-15"]})
    # to_datetime 把字符串解析为日期时间，返回可使用 dt 访问器的 Series。
    data["date"] = pd.to_datetime(data["date"])
    # dt.to_period("M") 把日期转换为月份周期，便于按月统计。
    data["month"] = data["date"].dt.to_period("M")
    # 两个日期相减得到 Timedelta，再用 dt.days 取出天数整数。
    data["days_from_start"] = (data["date"] - data["date"].min()).dt.days
    print(data.to_markdown(index=False))


if __name__ == "__main__":
    main()

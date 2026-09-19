"""排序、any 与 all：参考答案。

这份答案演示核心写法。练习任务通常还有其他正确实现；请重点比较思路。
"""


def main():
    # 先运行本答案，再逐行对照自己的实现。
    records = [{"name": "甲", "score": 80}, {"name": "乙", "score": 95}]
    print(sorted(records, key=lambda row: row["score"], reverse=True))
    print(any(row["score"] >= 90 for row in records))
    print(all(row["score"] >= 60 for row in records))


if __name__ == "__main__":
    main()

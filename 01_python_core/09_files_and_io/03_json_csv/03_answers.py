"""JSON 与 CSV：参考答案。

这份答案演示核心写法。练习任务通常还有其他正确实现；请重点比较思路。
"""


def main():
    # 先运行本答案，再逐行对照自己的实现。
    import json
    data = {"name": "小林", "skills": ["Python", "Pandas"]}
    text = json.dumps(data, ensure_ascii=False, indent=2)
    restored = json.loads(text)
    print(text)
    print(restored["skills"])


if __name__ == "__main__":
    main()

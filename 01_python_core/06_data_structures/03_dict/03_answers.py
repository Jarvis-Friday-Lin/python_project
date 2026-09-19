"""字典：参考答案。

这份答案演示核心写法。练习任务通常还有其他正确实现；请重点比较思路。
"""


def main():
    # 先运行本答案，再逐行对照自己的实现。
    student = {"name": "小林", "score": 90}
    student["age"] = 18
    print(student.get("city", "未知"))
    for key, value in student.items():
        print(key, value)


if __name__ == "__main__":
    main()

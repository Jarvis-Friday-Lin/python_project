"""类型别名、Literal 与 TypedDict：参考答案。

这份答案演示核心写法。练习任务通常还有其他正确实现；请重点比较思路。
"""


def main():
    # 先运行本答案，再逐行对照自己的实现。
    from typing import Literal, TypedDict
    class User(TypedDict):
        name: str
        role: Literal["admin", "member"]
    user: User = {"name": "小林", "role": "member"}
    print(user)


if __name__ == "__main__":
    main()

"""Protocol 与泛型：参考答案。

这份答案演示核心写法。练习任务通常还有其他正确实现；请重点比较思路。
"""


def main():
    # 先运行本答案，再逐行对照自己的实现。
    from typing import Protocol, TypeVar
    class SupportsClose(Protocol):
        def close(self) -> None: ...
    T = TypeVar("T")
    def first(items: list[T]) -> T:
        return items[0]
    print(first([1, 2, 3]))


if __name__ == "__main__":
    main()

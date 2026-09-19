"""可运行示例：先预测结果，再执行。"""

from typing import Protocol, TypeVar
class SupportsClose(Protocol):
    def close(self) -> None: ...
T = TypeVar("T")
def first(items: list[T]) -> T:
    return items[0]
print(first([1, 2, 3]))

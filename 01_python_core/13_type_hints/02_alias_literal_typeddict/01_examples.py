"""可运行示例：先预测结果，再执行。"""

from typing import Literal, TypedDict
class User(TypedDict):
    name: str
    role: Literal["admin", "member"]
user: User = {"name": "小林", "role": "member"}
print(user)

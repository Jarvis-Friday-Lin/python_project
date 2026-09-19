"""可运行示例：先预测结果，再执行。"""

from contextlib import contextmanager
@contextmanager
def managed_resource():
    print("打开")
    try: yield "资源"
    finally: print("关闭")
with managed_resource() as value: print(value)

"""可运行示例：先预测结果，再执行。"""

class Managed:
    def __enter__(self):
        print("获取资源")
        return self
    def __exit__(self, exc_type, exc, traceback):
        print("释放资源")

with Managed():
    print("使用资源")

"""可运行示例：先预测结果，再执行。"""

def parse_count(text):
    try:
        return int(text)
    except ValueError as error:
        raise ValueError(f"数量必须是整数，收到：{text!r}") from error

try:
    parse_count("abc")
except ValueError as error:
    print(error)

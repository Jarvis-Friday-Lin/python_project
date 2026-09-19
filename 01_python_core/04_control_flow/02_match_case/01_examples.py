"""可运行示例：先预测结果，再执行。"""

command = "start"
match command:
    case "start":
        print("开始")
    case "stop":
        print("停止")
    case _:
        print("未知命令")

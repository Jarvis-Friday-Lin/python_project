"""可运行示例：先预测结果，再执行。"""

values = [3, 1, 2]
values.append(4)
values[0] = 30
print(values[1:3])
print(sorted(values))  # 返回新列表
values.sort()          # 原地排序

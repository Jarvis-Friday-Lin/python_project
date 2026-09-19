"""可运行示例：先预测结果，再执行。"""

from copy import copy, deepcopy
original = [[1], [2]]
shallow = copy(original)
deep = deepcopy(original)
shallow[0].append(9)
print(original, shallow, deep)

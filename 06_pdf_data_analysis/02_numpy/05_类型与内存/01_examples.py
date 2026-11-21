"""案例驱动示例：为什么整数数组写入小数会丢精度"""
# 对应 PDF：11-numpy-full.pdf 第 13—14、54、63 页
# 任务：把 80 分修正为 80.5，并比较数据占用。
# 数组像一排统一规格的盒子，dtype 决定每格能装什么；改变某格不会自动换掉所有盒子。
# 案例数据：
# | 原分数 | 修正分数 |
# |---:|---:|
# | 80 | 80.5 |
# | 90 | 90 |
# 先看整体路线：
# 第 1 步：观察默认整数类型及赋值截断。
# 第 2 步：先转浮点，再保存小数。
# 第 3 步：用 itemsize 与 nbytes 比较存储。

import numpy as np
scores = np.array([80, 90], dtype=np.int32)
scores[0] = 80.5
print('\n===== scores =====')
print(scores)
# 整数格只能存整数，这次赋值截断小数；不是四舍五入。
fixed = scores.astype(np.float64)
# astype(dtype) 返回转换后的数组；默认创建副本，不改原来的 dtype。
fixed[0] = 80.5
print('\n===== fixed =====')
print(fixed)
print('\n===== scores.dtype =====')
print(scores.dtype)
print('\n===== (scores.itemsize, scores.nbytes) =====')
print((scores.itemsize, scores.nbytes))
print('\n===== (fixed.itemsize, fixed.nbytes) =====')
print((fixed.itemsize, fixed.nbytes))
# 常见类型还有无符号uint8、bool_、complex128、datetime64、object_。
# 按数值范围选类型；高精度浮点类型在不同平台不保证都存在。
flags = np.array([True, False], dtype=np.bool_)
dates = np.array(["2026-01-01", "2026-01-02"], dtype="datetime64[D]")
print('\n===== flags =====')
print(flags)
print('\n===== dates =====')
print(dates)
assert scores[0] == 80 and fixed[0] == 80.5
assert scores.nbytes == scores.size * scores.itemsize

# 学完先自己回答，再看下面的参考答案：
# 1. 这个知识点解决什么类型的问题？
# 2. 为什么当前案例需要它？
# 3. 每一步代码为什么要在此时出现？
# 4. 如果换一种做法，代价和风险是什么？

# 参考答案：
# 1. 选择数值表示方式、识别精度丢失与内存占用。
# 2. 80.5 无法完整保存到整数数组里。
# 3. 先观察类型，再转换整个数组，最后赋值并检查。
# 4. 直接用浮点避免这次截断，但精度、范围、内存仍需根据业务选择。

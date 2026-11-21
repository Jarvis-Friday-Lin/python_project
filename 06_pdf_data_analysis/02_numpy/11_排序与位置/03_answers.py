"""参考答案：配送时长从快到慢排序"""
# 对应 PDF：11-numpy-full.pdf 第 63—66 页
# 课件核心：第63—66页：sort、argsort、argmin、argmax与布尔选值。
# 扩展：kind="stable"保证并列时保留输入顺序，是排序参数扩展。
# 案例数据（据此自行创建对象，不能照抄 examples 的数据）：
# | courier | minutes |
# |---|---|
# | Q1 | 18 |
# | Q2 | 12 |
# | Q3 | 25 |
# | Q4 | 12 |
# | Q5 | 20 |
# 建议先做练习，再逐段对照下面的实现；assert 用于验证结果。

import numpy as np
names = np.array(['Q1','Q2','Q3','Q4','Q5'])
minutes = np.array([18,12,25,12,20])
order = np.argsort(minutes, kind='stable')
print('\n===== names[order] =====')
print(names[order])
print('\n===== minutes[order] =====')
print(minutes[order])
print('\n===== names[minutes == minutes.min()] =====')
print(names[minutes == minutes.min()])
print('\n===== np.nonzero(minutes > 18)[0] =====')
print(np.nonzero(minutes > 18)[0])
assert names[order].tolist() == ['Q2','Q4','Q1','Q5','Q3']
assert minutes.argmin() == 1 and names[minutes == minutes.min()].tolist() == ['Q2','Q4']
assert np.nonzero(minutes > 18)[0].tolist() == [2,4]
assert minutes.tolist() == [18,12,25,12,20]
# argsort返回位置；用同一位置数组同时重排姓名和时长，才不会错配。

"""参考答案：快递超重收费与关键字参数"""
# 基础准备/综合应用：为三份 PDF 的学习提供衔接。
# 课件核心：为阅读库函数的位置参数、关键字参数与返回值做准备。
# 扩展：函数定义、默认参数、关键字专用参数都是前置补充。
# 案例数据（据此自行创建对象，不能照抄 examples 的数据）：
# | parcel | weight_kg |
# |---|---|
# | P1 | 1.0 |
# | P2 | 2.5 |
# | P3 | 4.0 |
# 建议先做练习，再逐段对照下面的实现；assert 用于验证结果。

# * 后的参数必须写成 limit=...、per_kg=...，防止混淆多个收费数值。
def fee(weight, base=8, *, limit=2, per_kg=4):
    return base + max(weight - limit, 0) * per_kg

weights = [1.0, 2.5, 4.0]
costs = [fee(w) for w in weights]
special = fee(weight=2.5, base=10, limit=1, per_kg=6)
print('\n===== costs =====')
print(costs)
print('\n===== special =====')
print(special)
assert costs == [8, 10, 16]
assert special - fee(2.5) == 9
assert fee(2) == 8
# base 是固定费用；weight 是必填参数；关键字调用使收费规则更直观。

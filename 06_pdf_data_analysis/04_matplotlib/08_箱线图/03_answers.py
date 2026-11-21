"""参考答案：比较两条产线的加工时间分布"""
# 对应 PDF：14-matplotlib-full.pdf 第 18、20 页
# 课件核心：第18、20页：boxplot、中位数、四分位数、可能的离群值。
# 扩展：percentile手工核对IQR与fliers对象检查为扩展；对照C用于边界观察。
# 案例数据（据此自行创建对象，不能照抄 examples 的数据）：
# | line | minutes |
# |---|---|
# | A | 8,9,10,11,12 |
# | B | 7,9,10,11,25 |
# | 对照C | 10,10,10,10,10 |
# 建议先做练习，再逐段对照下面的实现；assert 用于验证结果。

import numpy as np
import matplotlib.pyplot as plt
a,b,c = [8,9,10,11,12], [7,9,10,11,25], [10,10,10,10,10]
fig, ax = plt.subplots()
boxes = ax.boxplot([a,b],patch_artist=True,boxprops={'facecolor':'lightblue'},medianprops={'color':'red'})
ax.set_xticks([1,2],labels=['Line A','Line B'])
ax.set_ylabel('Minutes')
q1,q3 = np.percentile(b,[25,75])
upper = q3 + 1.5*(q3-q1)
print('\n===== (q1, q3, upper) =====')
print((q1,q3,upper))
assert (q1,q3,upper) == (9,11,14)
assert list(boxes['fliers'][1].get_ydata()) == [25]
assert all(np.allclose(m.get_ydata(),10) for m in boxes['medians'])
fig2, ax2 = plt.subplots()
control = ax2.boxplot([c])
assert np.allclose(control['medians'][0].get_ydata(),10)
assert np.percentile(c,75)-np.percentile(c,25) == 0
# 离群标记是统计规则，不自动说明设备故障或数据录错；需要结合工况核查。
plt.show()
plt.close(fig)
plt.close(fig2)

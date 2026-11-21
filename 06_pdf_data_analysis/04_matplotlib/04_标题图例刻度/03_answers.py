"""参考答案：让噪声监测图具有明确含义"""
# 对应 PDF：14-matplotlib-full.pdf 第 11—12、15—16 页
# 课件核心：第11—12、15—16页：标题、坐标轴标签、图例及自定义刻度文字。
# 扩展：grid/set_ylim/annotate与读取标签属扩展。
# 案例数据（据此自行创建对象，不能照抄 examples 的数据）：
# | slot | period | noise_db |
# |---|---|---|
# | 0 | Dawn | 35 |
# | 1 | Morning | 55 |
# | 2 | Noon | 62 |
# | 3 | Night | 40 |
# 建议先做练习，再逐段对照下面的实现；assert 用于验证结果。

import matplotlib.pyplot as plt
x, labels, noise = [0,1,2,3], ['Dawn','Morning','Noon','Night'], [35,55,62,40]
fig, ax = plt.subplots()
ax.plot(x,noise,label='Room A',marker='o')
ax.set_title('Noise monitoring')
ax.set_xlabel('Period')
ax.set_ylabel('Noise (dB)')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()
# 扩展：axis='y'只画横向网格线；xy为标注指向点，xytext为文字位置。
ax.grid(axis='y',linestyle='--')
ax.set_ylim(0,80)
ax.annotate('Peak',xy=(2,62),xytext=(2.2,70),arrowprops={'arrowstyle':'->'})
assert [t.get_text() for t in ax.get_xticklabels()] == labels
assert list(ax.lines[0].get_ydata()) == noise and ax.get_ylabel() == 'Noise (dB)'
assert ax.get_ylim() == (0,80)
plt.show()
plt.close(fig)

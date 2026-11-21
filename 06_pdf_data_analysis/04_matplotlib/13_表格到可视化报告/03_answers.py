"""参考答案：用四张图报告社区借阅情况"""
# 对应 PDF：14-matplotlib-full.pdf 第8—21页；13-pandas-full.pdf 第45—46页综合
# 课件核心：Matplotlib第8—21页多子图、plot/bar/hist/boxplot/savefig；Pandas第45—46页分组。
# 扩展：groupby的多种聚合组合、图形读取检查与路径为跨课件应用补充。
# 案例数据（据此自行创建对象，不能照抄 examples 的数据）：
# | day | branch | books |
# |---|---|---|
# | 1 | East | 12 |
# | 1 | West | 8 |
# | 2 | East | 18 |
# | 2 | West | 12 |
# | 3 | East | 15 |
# | 3 | West | 10 |
# | 4 | East | 20 |
# | 4 | West | 15 |
# 建议先做练习，再逐段对照下面的实现；assert 用于验证结果。

from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
df = pd.DataFrame({'day':[1,1,2,2,3,3,4,4],'branch':['East','West']*4,
                   'books':[12,8,18,12,15,10,20,15]})
daily = df.groupby('day')['books'].sum()
branches = df.groupby('branch')['books'].sum()
fig, axes = plt.subplots(2,2,figsize=(10,7))
axes[0,0].plot(daily.index,daily,marker='o')
axes[0,0].set_title('Daily borrowing')
axes[0,0].set_xlabel('Day')
axes[0,0].set_ylabel('Books')
axes[0,1].bar(branches.index,branches)
axes[0,1].set_title('Branch total')
axes[0,1].set_ylabel('Books')
counts,_,_ = axes[1,0].hist(df['books'],bins=[0,10,15,21])
axes[1,0].set_xlabel('Books per record')
axes[1,0].set_ylabel('Records')
axes[1,1].boxplot([df.loc[df['branch'] == name,'books'] for name in branches.index])
axes[1,1].set_xticks([1,2],labels=branches.index)
axes[1,1].set_ylabel('Books per record')
assert daily.tolist() == [20,30,25,35] and branches.to_dict() == {'East':65,'West':45}
assert daily.sum() == branches.sum() == 110
assert counts.tolist() == [1,3,4] and counts.sum() == len(df)
assert list(axes[0,0].lines[0].get_ydata()) == daily.tolist()
fig.tight_layout()
out = Path(__file__).resolve().parent / 'outputs'
out.mkdir(exist_ok=True)
fig.savefig(out/'library_dashboard.png',dpi=160,bbox_inches='tight')
assert (out/'library_dashboard.png').stat().st_size > 0
plt.show()
plt.close(fig)

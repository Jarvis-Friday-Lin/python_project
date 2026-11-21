"""参考答案：交付可重复生成的能耗图片"""
# 对应 PDF：14-matplotlib-full.pdf 第 21 页；中文字体与路径为实用补充
# 课件核心：第21页savefig、第11页plot与标签、第12页tight_layout。
# 扩展：中文字体检测、pathlib、dpi与bbox_inches是实用扩展；不以关闭安全校验解决字体问题。
# 案例数据（据此自行创建对象，不能照抄 examples 的数据）：
# | month | energy_kwh |
# |---|---|
# | Jan | 320 |
# | Feb | 280 |
# | Mar | 350 |
# | Apr | 300 |
# 建议先做练习，再逐段对照下面的实现；assert 用于验证结果。

from pathlib import Path
import matplotlib.pyplot as plt
from matplotlib import font_manager
available = {font.name for font in font_manager.fontManager.ttflist}
font = next((name for name in ['PingFang SC','Heiti TC','Microsoft YaHei','SimHei','Noto Sans CJK SC','Arial Unicode MS'] if name in available),None)
fig, ax = plt.subplots(figsize=(6,3))
ax.plot(['Jan','Feb','Mar','Apr'],[320,280,350,300],marker='o')
# 字体属性只传给本图文字，不修改其他例题的全局rcParams。
if font:
    ax.set_title('月度能耗',fontname=font)
    ax.set_xlabel('月份',fontname=font)
    ax.set_ylabel('用电量 (kWh)',fontname=font)
else:
    ax.set_title('Monthly energy')
    ax.set_xlabel('Month')
    ax.set_ylabel('Energy (kWh)')
fig.tight_layout()
out = Path(__file__).resolve().parent / 'outputs'
out.mkdir(exist_ok=True)
fig.savefig(out/'energy_report.png',dpi=180,bbox_inches='tight')
fig.savefig(out/'energy_report.pdf',bbox_inches='tight')
assert all((out/name).stat().st_size > 0 for name in ['energy_report.png','energy_report.pdf'])
assert list(ax.lines[0].get_ydata()) == [320,280,350,300]
plt.show()
plt.close(fig)

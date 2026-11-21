"""参考答案：把图保存成可交付文件"""
# 对应 PDF：14-matplotlib-full.pdf 第 21 页；中文字体与路径为实用补充
# 建议先完成 02_exercises.py；下面的实现与该题数据、要求一一对应。

from pathlib import Path
import matplotlib.pyplot as plt
from matplotlib import font_manager
available={f.name for f in font_manager.fontManager.ttflist}
font=next((n for n in ["PingFang SC","Heiti TC","Microsoft YaHei","SimHei","Noto Sans CJK SC","Arial Unicode MS"] if n in available),None)
if font:
    plt.rcParams["font.sans-serif"]=[font]
    plt.rcParams["axes.unicode_minus"]=False
fig,ax=plt.subplots()
ax.plot([1,2,3],[10,20,15],marker="o")
ax.set(title="每日销量" if font else "Daily sales",xlabel="日期" if font else "Day",ylabel="件数" if font else "Units")
fig.tight_layout()
out=Path(__file__).resolve().parent/"outputs"
out.mkdir(exist_ok=True)
fig.savefig(out/"exercise_sales.png",dpi=160,bbox_inches="tight")
fig.savefig(out/"exercise_sales.pdf",bbox_inches="tight")
assert all((out/name).stat().st_size>0 for name in ["exercise_sales.png","exercise_sales.pdf"])
plt.show()
plt.close(fig)

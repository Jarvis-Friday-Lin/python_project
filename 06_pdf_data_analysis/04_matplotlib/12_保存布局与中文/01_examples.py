"""案例驱动示例：把图保存成可交付文件"""
# 对应 PDF：14-matplotlib-full.pdf 第 21 页；中文字体与路径为实用补充
# 任务：保存带标题、坐标、图例的销售图，换一个启动目录也能找到输出。
# 中文正常显示需要真实存在的字体；不存在时用英文标签，不能靠配置一个假字体名解决。
# 案例数据：
# | day | sales |
# |---:|---:|
# | 1 | 10 |
# | 2 | 20 |
# | 3 | 15 |
# 先看整体路线：
# 第 1 步：检查系统可用字体，选择中英标签。
# 第 2 步：创建图并调整边距。
# 第 3 步：在show之前保存PNG/PDF，确认文件存在。

from pathlib import Path
import matplotlib.pyplot as plt
from matplotlib import font_manager
# fontManager列出当前可用字体；首个命中即可，不下载或修改系统字体。
available={font.name for font in font_manager.fontManager.ttflist}
font=next((n for n in ["PingFang SC","Heiti TC","Microsoft YaHei","SimHei","Noto Sans CJK SC","Arial Unicode MS"] if n in available),None)
if font:
    plt.rcParams["font.sans-serif"]=[font]
    plt.rcParams["axes.unicode_minus"]=False
print('\n===== {"使用字体":font or "默认字体；图内使用英文"} =====')
print({"使用字体":font or "默认字体；图内使用英文"})
fig,ax=plt.subplots(figsize=(6,4))
ax.plot([1,2,3],[10,20,15],marker="o",label="销量" if font else "Sales")
ax.set(title="每日销量" if font else "Daily sales",xlabel="日期" if font else "Day",ylabel="件数" if font else "Units")
ax.legend()
fig.tight_layout()
output=Path(__file__).resolve().parent/"outputs"
output.mkdir(exist_ok=True)
# dpi影响位图像素；bbox_inches="tight"减少边缘裁切；PDF中的线和文字通常是矢量。
fig.savefig(output/"sales.png",dpi=160,bbox_inches="tight")
fig.savefig(output/"sales.pdf",bbox_inches="tight")
print('\n===== output/"sales.png" =====')
print(output/"sales.png")
assert (output/"sales.png").stat().st_size>0
assert (output/"sales.pdf").stat().st_size>0
# 先保存再show，避免某些后端在窗口关闭后保存成空白。
plt.show()
plt.close(fig)

# 学完先自己回答，再看下面的参考答案：
# 1. 这个知识点解决什么类型的问题？
# 2. 为什么当前案例需要它？
# 3. 每一步代码为什么要在此时出现？
# 4. 如果换一种做法，代价和风险是什么？

# 参考答案：
# 1. 将图形可靠保存为可交付文件。
# 2. 在PyCharm看见图不等于已经得到可分享的文件。
# 3. 先检查字体和标签，再完成布局，在show之前保存并检查路径。
# 4. 截图方便但清晰度和边界难控制；只设不存在的字体仍会显示方框。

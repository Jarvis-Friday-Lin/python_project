# Matplotlib（中文翻译）

原文：`14-matplotlib-full.pdf`，共 29 页。课程：COMP 1023《Python 编程入门》，2026 年秋季。作者：SC Cheung 教授、Alex Lam 博士、Desmond Tsoi 博士，中国香港特别行政区香港科技大学计算机科学与工程学系。联系邮箱：`{sccheung, lamngok, desmond}@ust.hk`。

翻译说明：按原文页序保留正文、代码、扩展方法列表、复习题与答案，省略重复页脚。API、变量名、图表内的示例字符串保留英文，说明和注释译为中文；图内字符串的含义在相邻正文中说明，这也避免默认字体不支持中文时出现方框。原图的结构和结果使用中文描述，图形可运行对应代码重现。“译注”是对原文笔误或适用条件的补充。各代码示例独立运行；随机图形每次可能不同。

## 原文第 1 页：封面

COMP 1023《Python 编程入门》：Matplotlib。作者与机构见文首。

## 原文第 2 页：简介

Matplotlib 是一个功能全面的 Python 可视化库，可以创建静态、动画和交互式可视化，广泛用于数据科学、工程和科研等领域。

主要特点：

- 静态可视化：生成高质量折线图、柱状图、散点图等。
- 动画可视化：通过动态画面表示数据随时间或其他变量的变化。
- 交互式可视化：允许用户缩放、平移图形，或查看实时更新。

本课程使用 Matplotlib **3.10.8**，重点学习静态可视化。

## 原文第 3 页：为什么选择 Matplotlib

- 应用广泛：它是 Python 生态中使用最广泛的数据可视化库之一。
- 可定制：可调整颜色、标签、样式等大量视觉元素。
- 易于整合：可以与 NumPy、Pandas、Seaborn 等库结合，增强数据分析与可视化能力；Seaborn 是统计数据可视化库。

## 原文第 4 页：一幅 Matplotlib 图的主要组成

- `Figure`（整张图 / 画布）：所有视觉元素的顶层容器。
- `Axes`（绘图区）：实际绘制数据的区域，一张 Figure 可以有多个 Axes。
- `Axis`（坐标轴）：定义水平 x 轴或垂直 y 轴，包括取值范围、刻度、刻度标签等。
- 线条和标记：线条连接数据点以展示趋势；标记突出各个数据点，散点图中尤为常见。
- 标题和标签：标题提供整张图的背景信息，坐标轴标签说明各轴数据的含义。

原图“一幅图的结构”还标注了这些元素及相关访问方式：

| 原图标签 | 中文含义 | 原图对应写法 |
|---|---|---|
| Figure | 整张图 | `plt.figure` |
| Axes | 绘图区 | `fig.subplots` |
| Title | 标题 | `ax.set_title` |
| X Axis / Y Axis | x 坐标轴 / y 坐标轴 | `ax.xaxis` / `ax.yaxis` |
| X label / Y label | x 轴标签 / y 轴标签 | `ax.set_xlabel` / `ax.set_ylabel` |
| Major tick / Minor tick | 主刻度 / 次刻度 | 对应轴的 `set_major_locator` / `set_minor_locator` |
| Major tick label / Minor tick label | 主刻度标签 / 次刻度标签 | 对应轴的 `set_major_formatter` / `set_minor_formatter` |
| Legend | 图例 | `ax.legend` |
| Grid | 网格 | `ax.grid` |
| Line | 线条 | `ax.plot` |
| Markers | 数据点标记 | `ax.scatter` |
| Spine | 绘图区边框 | `ax.spines` |

> 译注：`Axes` 是一个绘图区对象的类名，并不等同于“多根 Axis”。初学时尤其要分清 `Figure → Axes → Axis` 的包含关系。

## 原文第 5 页：Matplotlib pyplot 入门

`pyplot` 是 Matplotlib 的一个模块，用于创建静态、交互式和动画可视化。

基本步骤：

1. 导入模块：`import matplotlib.pyplot as plt`。
2. 准备数据：整理为列表或数组。
3. 创建图形：使用数据调用 `plt.plot()`。
4. 完善图形：使用 `plt.title()`、`plt.xlabel()`、`plt.ylabel()` 添加标题、坐标轴标签等。
5. 显示图形：调用 `plt.show()`。

## 原文第 6 页：Figure 与 Axes

Figure 对象包含整张图的全部内容，其中可以有多个绘图区，也可以保存为 JPEG、PNG 等图像文件。

Figure 内的每一个 Axes 对象对应一个绘图区。普通二维 Axes 中有 x 轴与 y 轴，表示要绘制的数据维度。

## 原文第 7 页：创建一张包含单个绘图区的图

`plt.subplots()` 创建并返回一个新的 Figure 及其 Axes。

```python
# 文件名：single_plot_create.py
import matplotlib.pyplot as plt

# 宽 5 英寸，高 3 英寸
fig, ax = plt.subplots(figsize=(5, 3))
plt.show()
```

结果是一个尚未添加数据的空绘图区。`figsize` 的单位为英寸。

## 原文第 8 页：创建多个绘图区

`plt.subplots()` 前两个参数指定行数与列数。在本例中，它返回 Figure 和一个 NumPy 数组形式的 Axes 集合，可以用 NumPy 索引方式访问各绘图区。

```python
# 文件名：multiple_plots_create.py
import matplotlib.pyplot as plt

# 2 行 3 列，共 6 个绘图区
fig, ax = plt.subplots(2, 3, figsize=(5, 3))
plt.show()
```

> 译注：默认 `squeeze=True`，只有一个绘图区时返回单个 Axes，一行或一列时常返回一维数组，本例 2×3 时才是二维数组。

## 原文第 9 页：第一部分——成对数据可视化

下面介绍以 `(x, y)` 等成对数据为基础的绘图方法。

## 原文第 10 页：成对数据的绘图方法

这类可视化用于 `(x, y)` 坐标数据、表格中的多个变量以及 `f(x) = y` 形式的函数关系。

| 方法 | 用途 |
|---|---|
| `plot(x, y)` | 用线连接数据点，创建折线图 |
| `scatter(x, y)` | 用独立点创建散点图 |
| `bar(x, height)` | 用柱形表示分类数据 |
| `stem(x, y)` † | 用茎叶式线段与标记表示离散数据，即茎状图 |
| `fill_between(x, y1, y2)` † | 填充两条曲线之间的区域 |
| `stackplot(x, y)` † | 创建堆叠面积图，展示累计数据 |
| `stairs(values)` † | 创建阶梯图，展示分段变化 |

†：原文标记为自行探索。

## 原文第 11 页：绘制折线

使用 Axes 的 `.plot()` 方法：传入两组列表或 NumPy 数组，第一组是 x 坐标，第二组是对应的 y 坐标。

`marker` 指定点标记样式，`label` 指定该组数据的图例名称。使用 `.set_xlabel()`、`.set_ylabel()` 设置轴标签，使用 `.set_title()` 设置标题。

```python
# 文件名：line_curve_draw.py
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(5, 3))
# 依次连接 (0,0)、(2,4)、(4,16)、(6,36)、(8,64)
ax.plot([0, 2, 4, 6, 8], [0, 4, 16, 36, 64],
        marker='o', label='Data Points 1')
# 另一条线经过 (0,3)、(4,7)、(8,50)
ax.plot([0, 4, 8], [3, 7, 50], marker='x', label='Data Points 2')
ax.set_xlabel('X Values')
ax.set_ylabel('Y Values')
ax.set_title('Sample Plot of X vs Y')
plt.show()
```

图中两条线分别使用圆形标记与叉形标记。字符串含义：`Data Points 1/2` 为“数据点 1/2”，`X Values` / `Y Values` 为“X 值 / Y 值”，标题为“X 与 Y 的示例图”。

> 译注：原文虽然设置了 `label`，但没有调用 `ax.legend()`，因此该示例默认不会显示图例。若需要显示，在 `plt.show()` 前添加 `ax.legend()`。

## 原文第 12 页：在多行、多列中绘制折线

每个子图可以展示不同数据集，并分别设置轴标签和标题。

```python
# 文件名：line_plot_draw_multiples.py
import matplotlib.pyplot as plt

fig, ax = plt.subplots(2, 2, figsize=(10, 6))
ax[0, 0].plot([0, 1, 2], [2, 4, 6])  # 第一幅子图
ax[0, 0].set_xlabel('X Values')
ax[0, 0].set_ylabel('Y Values')
ax[0, 0].set_title('Plot 1: Line through (0,2), (1,4), (2,6)')

ax[0, 1].plot([0, 1, 2], [3, 6, 9])  # 第二幅子图
ax[0, 1].set_xlabel('X Values')
ax[0, 1].set_ylabel('Y Values')
ax[0, 1].set_title('Plot 2: Line through (0,3), (1,6), (2,9)')

ax[1, 0].plot([0, 1, 2], [1, 2, 3])  # 第三幅子图
ax[1, 0].set_xlabel('X Values')
ax[1, 0].set_ylabel('Y Values')
ax[1, 0].set_title('Plot 3: Line through (0,1), (1,2), (2,3)')

ax[1, 1].plot([0, 1, 2], [4, 8, 12])  # 第四幅子图
ax[1, 1].set_xlabel('X Values')
ax[1, 1].set_ylabel('Y Values')
ax[1, 1].set_title('Plot 4: Line through (0,4), (1,8), (2,12)')
plt.tight_layout()
plt.show()
```

`Plot n: Line through ...` 表示“第 n 幅图：经过所列坐标点的折线”。结果为 2×2 子图布局。

## 原文第 13 页：绘制一组点或线段

`plot()` 也可以绘制一组具有相同大小、颜色、线宽等属性的点或线段。

```python
# 文件名：sequence_points_segments_draw.py
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 5, 20)
y = np.exp(x)
fig, ax = plt.subplots(figsize=(3, 2))
ax.plot(x, y, c='blue', linestyle='', marker='*', label='Curve 1')
ax.plot(x, 2*y, c='green', linestyle='--', label='Curve 2')
# 用相对于绘图区的位置设置图例
ax.legend(loc=(1.1, 0.5))
plt.show()
```

第一组是蓝色星形点，不连线；第二组是绿色虚线，纵坐标为第一组的两倍。`Curve 1/2` 表示“曲线 1/2”。图例放在绘图区右侧。

## 原文第 14 页：散点图——使用颜色映射展示一组点

`.scatter()` 可以分别指定各点的颜色、大小等属性。传入所有点的 x、y 坐标数组；`cmap` 指定颜色映射，`s` 指定点的面积。

```python
# 文件名：scatterplot.py
import numpy as np
import matplotlib.pyplot as plt

x = np.random.rand(20)
y = np.random.rand(20)
colors = x + y  # 颜色数值随位置变化
area = 100 * (x + y)  # 面积也随位置变化
fig, ax = plt.subplots(figsize=(3, 2))
ax.scatter(x, y, c=colors, cmap='spring', s=area)
plt.show()
```

图中 20 个点的颜色和面积都与 `x + y` 有关。

> 译注：原文把面积单位写作“square points (dpi)”，其中 dpi 不准确。`s` 的单位是平方点（points²）；1 point 为 1/72 英寸，dpi 则是每英寸像素数。

## 原文第 15 页：柱状图——用柱形展示一组数值

`.bar()` 接收每根柱子的 x 轴位置，以及对应高度，两组数据长度应相同。`tick_label` 指定横轴刻度文字。

```python
# 文件名：barchart_single.py
import numpy as np
import matplotlib.pyplot as plt

x = [1, 2, 3]  # 柱子在 x 轴的位置
height = [10, 2, 8]  # 柱子高度
labels = ['Sensor 1', 'Sensor 2', 'Sensor 3']
fig, ax = plt.subplots(figsize=(3, 2))
ax.bar(x, height, tick_label=labels)
plt.show()
```

三个传感器（Sensor 1/2/3）对应的柱高分别为 10、2、8。

> 译注：原文提到水平和垂直柱形，但 `bar()` 默认画垂直柱；水平柱状图通常使用 `barh()`。

## 原文第 16 页：并列柱状图

可以把多组柱子并排放置。两组柱子的中心分别位于 `x + width/2` 与 `x - width/2`。

```python
# 文件名：barchart_multiples.py
import numpy as np
import matplotlib.pyplot as plt

heightMin = [10, 2, 8]
heightMax = [8, 6, 5]
x = np.arange(3)
width = 0.4
labels = ['Sensor 1', 'Sensor 2', 'Sensor 3']
fig, ax = plt.subplots(figsize=(3, 2))
# 默认颜色循环下，第一组为蓝色，第二组为橙色
ax.bar(x + width / 2, heightMin, width=width, label='Min')
ax.bar(x - width / 2, heightMax, width=width, label='Max')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend(loc=(1.1, 0.5))
plt.show()
```

每个传感器位置都有两根柱。`Min` / `Max` 表示“最小值 / 最大值”。

> 译注：原文数据中部分 `heightMin` 大于对应 `heightMax`，不符合“最小值不得大于最大值”的业务含义。此处保留原数据以对照原文；它演示的是并列绘图方法，不应把这些数据当作有效的极值统计。

## 原文第 17 页：第二部分——统计分布

下面介绍用于呈现数据分布的图形。

## 原文第 18 页：统计分布的绘图方法

这些可视化技术描述数据集中一个或多个变量的分布；其中许多方法也会计算绘图所需的统计量。

| 方法 | 用途 |
|---|---|
| `hist(x)` | 直方图，展示单变量的频数分布 |
| `boxplot(X)` | 箱线图，通过四分位数概括分布 |
| `errorbar(x, y, yerr, xerr)` † | 带误差棒的数据点，表示变异或误差 |
| `violinplot(D)` † | 小提琴图，结合分布密度与统计概要 |
| `eventplot(D)` † | 沿轴展示事件，适用于时间序列等数据 |
| `hist2d(x, y)` † | 二维直方图，显示双变量联合分布 |
| `hexbin(x, y, C)` † | 六边形分箱图，用于双变量可视化 |
| `pie(x)` † | 饼图，展示类别占比 |
| `ecdf(x)` † | 计算并绘制经验累积分布函数 |

†：原文标记为自行探索。表中写法用于说明主要参数，不是所有方法的完整函数签名。

## 原文第 19 页：创建直方图

`hist(x)` 用来展示数据分布，`x` 为包含数值的一维数组或列表。`bins` 控制分箱数量，从而改变观察分布的粒度；`color`、`alpha`、`edgecolor` 可以调整颜色、透明度和边框颜色。

```python
# 文件名：histogram.py
import matplotlib.pyplot as plt
import numpy as np

data = np.random.randn(1000)  # 生成随机数据
plt.hist(data, bins=30, color='blue', alpha=0.7, edgecolor='black')
plt.title('Histogram of Random Data')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.show()
```

标题意为“随机数据的直方图”，横轴为“数值”，纵轴为“频数”。结果是 1000 个标准正态随机数的 30 分箱直方图。

## 原文第 20 页：创建箱线图

`boxplot(X)` 通过四分位数描述数据分布。`X` 可以是一维数据，也可以是用于多个箱线图的二维数据。

箱线图概括中心位置、离散程度和潜在离群值。原文提到可以调整颜色、`notch` 缺口和 `vert` 方向等外观设置。

```python
# 文件名：boxplot.py
import matplotlib.pyplot as plt
import numpy as np

data = [np.random.normal(0, std, 100) for std in range(1, 4)]
plt.boxplot(data, notch=True, patch_artist=True,
            boxprops=dict(facecolor='lightblue', color='blue'),
            medianprops=dict(color='red'))
plt.title('Box Plot of Random Data')
plt.xlabel('Dataset')
plt.ylabel('Value')
plt.xticks([1, 2, 3], ['Data 1', 'Data 2', 'Data 3'])
plt.show()
```

标题为“随机数据的箱线图”，横轴为“数据集”，纵轴为“数值”，三组数据分别标为“数据 1/2/3”。它们都来自均值 0 的正态分布，标准差分别为 1、2、3，每组 100 个样本。

> 译注：`boxplot` 没有统一的顶层 `color=` 参数，应如示例通过 `boxprops`、`medianprops` 等设置颜色。`vert` 是原文版本中的方向参数，新版可能要求改用 `orientation`，例如 `orientation='horizontal'`。

## 原文第 21 页：把图保存到文件

可以将图保存为 JPEG、PNG、PDF、EPS 等格式，使用 Figure 的 `.savefig()` 方法。

```python
# 文件名：save_plot.py
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(3, 2))
ax.plot([0, 1, 2], [2, 4, 6])
ax.plot([0, 1, 2], [3, 6, 9])
fig.savefig('test.png')  # 也可使用 .jpg、.eps、.pdf 等扩展名
```

结果文件是一张包含两条折线的图。

## 原文第 22 页：更多可探索的绘图方法

以下保留原文的方法列表。† 表示自行探索；这不是完整 API 签名，也不意味着这些方法都属于普通二维 Axes。

### 网格数据

| 原文方法 | 中文用途 |
|---|---|
| `imshow(Z)` † | 以图像形式显示二维数据 |
| `pcolormesh(X, Y, Z)` † | 用伪彩色网格显示数据 |
| `contour(X, Y, Z)` | 绘制等高线 |
| `contourf(X, Y, Z)` † | 绘制填色等高线 |
| `barbs(X, Y, U, V)` † | 绘制风羽等方向与强度标记 |
| `quiver(X, Y, U, V)` † | 绘制箭头向量场 |
| `streamplot(X, Y, U, V)` † | 绘制流线 |

### 不规则网格数据

| 原文方法 | 中文用途 |
|---|---|
| `tricontour(x, y, z)` | 基于三角网格的等高线 |
| `tricontourf(x, y, z)` † | 基于三角网格的填色等高线 |
| `tripcolor(x, y, z)` † | 三角网格伪彩色图 |
| `triplot(x, y)` † | 绘制三角网格结构 |

### 三维与体数据

| 原文方法 | 中文用途 |
|---|---|
| `bar3d(x, y, z, dx, dy, dz)` † | 三维柱形 |
| `fill_between(x1, y1, z1, x2, y2, z2)` | 两条三维曲线之间的填充，取决于具体版本支持 |
| `plot(xs, ys, zs)` † | 三维曲线 |
| `quiver(X, Y, Z, U, V, W)` † | 三维箭头向量场 |
| `scatter(xs, ys, zs)` † | 三维散点 |
| `streamplot(x, y, u, v)` † | 原文列在本组的流线方法，见译注 |
| `plot_surface(X, Y, Z)` † | 三维曲面 |
| `plot_trisurf(x, y, z)` † | 三角网格曲面 |
| `voxels([x, y, z], filled)` † | 体素图 |
| `plot_wireframe(X, Y, Z)` † | 三维线框图 |

> 译注：原文把二维 `streamplot(x, y, u, v)` 列入三维方法组，不应据此推断其支持三维流线。三维方法通常需要三维 Axes。`voxels([x, y, z], filled)` 的方括号表示坐标参数可选，不是要求把三个坐标装进一个列表传入。原文因排版显示为 `fill between`、`plot surface` 等的方法名，此处恢复下划线。

## 原文第 23 页：使用 contour() 创建等高线图

`contour()` 使用二维平面上的等值线表示三维数值关系：二维网格 `X`、`Y` 定义位置，`Z` 定义对应值。

`levels` 可以控制等高线层级数量或直接指定等值线数值；`cmap` 指定颜色映射。

```python
# 文件名：contour.py
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)
Z = np.sin(np.sqrt(X**2 + Y**2))
plt.contour(X, Y, Z, levels=20, cmap='viridis')
plt.colorbar(label='Z Value')
plt.title(r'Contour Plot of $Z = \sin(\sqrt{X^2 + Y^2})$')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.show()
```

图形展示 `Z = sin(sqrt(X² + Y²))` 的等高线，形成围绕原点的环状结构。标题意为“该函数的等高线图”，色条标签 `Z Value` 为“Z 值”，横纵轴分别为“X 轴”“Y 轴”。

> 译注：使用整数 `levels` 时，绘图库会选择合适层级，并不保证恰好生成指定数量的线；需要准确控制时传入具体层级数组。此处为数学字符串加 `r` 前缀，避免反斜杠引发转义警告，不改变显示含义。

## 原文第 24 页：使用 tricontour() 创建三角网格等高线图

`tricontour()` 用于不规则分布的数据：三组一维数组分别表示点的 x、y 坐标和对应 z 值。通过三角剖分组织这些点，再绘制等高线。

`levels` 控制等高线层级。原文还提到可以自行定义三角剖分，以改善可视化。

```python
# 文件名：tricontour.py
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.tri import Triangulation

x = np.random.rand(30)
y = np.random.rand(30)
z = np.sin(x) + np.cos(y)
triang = Triangulation(x, y)  # 创建三角剖分
plt.tricontour(triang, z, levels=14, cmap='plasma')
plt.colorbar(label='Z Value')
plt.title('Triangular Contour Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.show()
```

标题为“三角网格等高线图”，色条表示 Z 值。图形由 30 个随机位置上的函数值 `sin(x) + cos(y)` 构成。

> 译注：原文把自定义剖分描述为 `triangulate` 参数，但这里应像代码一样创建 `Triangulation` 对象，并作为参数传入；不要直接照文字写不存在的 `triangulate=`。

## 原文第 25 页：使用 fill_between() 填充区域

`fill_between()` 填充两条曲线之间的区域。x 坐标与两组 y 坐标共同确定填充边界，适合突出图中某一区域。

通过 `color` 设置颜色，`alpha` 设置透明度，`label` 设置图例名称。

```python
# 文件名：area_filling.py
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.sin(x) + 0.5
plt.fill_between(x, y1, y2, color='skyblue',
                 alpha=0.5, label='Area between curves')
plt.plot(x, y1, label='y1 = sin(x)', color='blue')
plt.plot(x, y2, label='y2 = sin(x) + 0.5', color='orange')
plt.title('Area Filling with fill_between()')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.legend()
plt.show()
```

图形用半透明天蓝色填充 `sin(x)` 与 `sin(x) + 0.5` 之间的带状区域。`Area between curves` 表示“两条曲线之间的区域”，标题表示“使用 fill_between() 填充区域”。

## 原文第 26 页：关键术语

| 英文 | 中文 |
|---|---|
| Animated Visualizations | 动画可视化 |
| Area Filling | 区域填充 |
| Axes | 绘图区 |
| Axis | 坐标轴 |
| Bar Chart | 柱状图 |
| Box Plot | 箱线图 |
| Color Map | 颜色映射 |
| Contour Plot | 等高线图 |
| Data Visualization | 数据可视化 |
| Error Bars | 误差棒 |
| Figure | 整张图 / 画布 |
| fill_between | 曲线之间的区域填充方法 |
| Gridded Data | 网格数据 |
| Histogram | 直方图 |
| Interactive Visualizations | 交互式可视化 |
| Irregularly Gridded Data | 不规则网格数据 |
| Matplotlib | Python 绘图库 |
| Plot | 图 / 绘图 |
| Pyplot | Matplotlib 的绘图模块 |
| Scatter Plot | 散点图 |
| Static Visualizations | 静态可视化 |
| Triangular Contour Plot | 三角网格等高线图 |

## 原文第 27 页：复习题 1—6

请填空。

1. Matplotlib 是用于在 Python 中创建____、动画和交互式可视化的综合库。
2. ____模块用于创建静态、交互式和动画可视化。
3. ____是图中全部视觉元素的顶层容器。
4. ____定义图的水平方向（x 轴）与垂直方向（y 轴）。
5. ____函数用于创建直方图，展示数据集分布。
6. 可以使用 `boxplot()` 创建____图。

原文答案：1. 静态图（static plots）；2. Pyplot；3. Figure；4. Axis；5. `hist()`；6. 箱线（box）。

## 原文第 28 页：复习题 7—12

7. `scatter()` 方法用于在图上展示一组____。
8. 可以使用____函数填充两条曲线之间的区域。
9. `contour()` 用于创建____图，在二维中表示三维数据。
10. 要在一个 Figure 中创建多个绘图区，可调用 `subplots()` 并指定____和____。
11. `plot()` 方法中的____参数可以定制点标记的外观。
12. 使用 `fig.savefig()` 保存图时，可以选择不同文件____。

原文答案：7. 点；8. `fill_between()`；9. 等高线；10. 行数；列数。11. `marker`。12. 格式。

## 原文第 29 页：结束

本讲到此结束！有什么问题吗？

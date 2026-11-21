# 数值计算 Python：NumPy（中文翻译）

原文：`11-numpy-full.pdf`，共 67 页。课程：COMP 1023《Python 编程入门》，2026 年秋季。作者：SC Cheung 教授、Alex Lam 博士、Desmond Tsoi 博士，中国香港特别行政区香港科技大学计算机科学与工程学系。联系邮箱：`{sccheung, lamngok, desmond}@ust.hk`。

翻译说明：按原文页序保留正文、示例、题目与答案，省略重复页脚。代码中的 API、变量名与案例数据保持原样，说明和注释译为中文；原图中的运算关系改用公式、表格或文字表达。标为“译注”的内容是对原文笔误或适用条件的补充，不属于原文。示例通常各自独立，标明“续”的代码沿用前文变量。随机数、耗时、内存大小以及部分类型显示可能随运行环境变化。

## 原文第 1 页：封面

COMP 1023《Python 编程入门》：数值计算 Python（Numerical Python，NumPy）。作者与机构见文首。

## 原文第 2 页：NumPy 概述

NumPy 是 Numerical Python 的缩写，是 Python 中用于数值计算与科学计算的基础库。它提供高效的多维数组结构，以及操作这些数组的多种工具。

本课程使用 NumPy **2.4.0**。

## 原文第 3 页：认识数组

NumPy 数组是一组按网格组织的值，元素具有相同的数据类型，可以通过非负整数构成的索引元组定位。数组的维数称为“秩”（rank）；形状（shape）是一个整数元组，说明各个维度的大小。

可以使用 Python 嵌套列表创建数组，再用方括号访问元素。

```python
# 文件名：array_example.py
import numpy as np

a: np.ndarray = np.array([10, 20, 30])  # 创建一维数组
print(type(a))  # <class 'numpy.ndarray'>
print(a.shape)  # (3,)
print(a[0], a[1], a[2])  # 10 20 30
a[0] = 50  # 修改一个元素
print(a)  # [50 20 30]

b: np.ndarray = np.array([[7, 8, 9], [10, 11, 12]])  # 创建二维数组
print(b.shape)  # (2, 3)
print(b[0, 0], b[0, 1], b[1, 0])  # 7 8 10
```

> 译注：NumPy 也支持负数索引。这里的 rank 指 `ndim`，不是线性代数中的矩阵秩；普通数组元素具有相同的 `dtype`，而 `object` 类型数组可存放不同的 Python 对象。

## 原文第 4 页：创建数组

NumPy 提供多种数组创建函数。

```python
# 文件名：array_generation.py
import numpy as np

a: np.ndarray = np.zeros((3, 3))  # 全 0 数组，默认浮点型
print(a)
# [[0. 0. 0.]
#  [0. 0. 0.]
#  [0. 0. 0.]]
b: np.ndarray = np.ones((2, 3))  # 全 1 数组
print(b)
# [[1. 1. 1.]
#  [1. 1. 1.]]
c: np.ndarray = np.full((3, 2), 5)  # 用常量 5 填充
print(c)
# [[5 5]
#  [5 5]
#  [5 5]]
d: np.ndarray = np.eye(3)  # 3×3 单位矩阵
print(d)
# [[1. 0. 0.]
#  [0. 1. 0.]
#  [0. 0. 1.]]
e: np.ndarray = np.random.rand(3, 2)  # 随机值数组
print(e)
# 原文给出的示意输出，实际数值随机变化：
# [[0.12345678 0.87654321]
#  [0.23456789 0.76543210]
#  [0.34567890 0.65432109]]
```

## 原文第 5 页：数组索引与切片

| 表达式 | 含义 |
|---|---|
| `a[i]` | 获取索引为整数 `i` 的元素，索引从 0 开始。 |
| `a[-i]` | 获取倒数第 `i` 个元素：最后一个是 `-1`，倒数第二个是 `-2`。这里 `i` 为正整数。 |
| `a[i:j]` | 从索引 `i` 开始，到索引 `j` 之前结束，不含 `j`。 |
| `a[:]` 或 `a[0:]` | 获取指定轴上的全部元素。 |
| `a[:i]` | 从索引 0 到 `i` 之前，不含 `i`。 |
| `a[i:]` | 从索引 `i` 到最后一个元素。 |
| `a[i:j:n]` | 从 `i` 到 `j` 之前，步长为 `n`。 |
| `a[::-1]` | 按相反顺序获取全部元素。 |

## 原文第 6 页：多维数组切片

与 Python 列表一样，NumPy 数组支持切片。由于数组可以有多个维度，需要为相应维度指定切片。

```python
# 文件名：array_indexing_slicing_example.py
import numpy as np

# 二维数组，形状为 (3, 4)
a: np.ndarray = np.array([
    [10, 20, 30, 40],
    [50, 60, 70, 80],
    [90, 100, 110, 120],
])
# 提取前两行、索引为 2 和 3 的列，得到形状 (2, 2) 的子数组
b: np.ndarray = a[:2, 2:4]
# b 为 [[30, 40], [70, 80]]

# 基本切片得到原数据的视图，修改视图也会修改原数组
print(a[0, 2])  # 30
b[0, 0] = 99  # 与 a[0, 2] 指向同一份数据
print(a[0, 2])  # 99
```

## 原文第 7 页：混合整数索引与切片

整数索引与切片可以混用，但整数索引会消去相应的轴，使结果维数降低；仅使用切片则保留对应维度。

```python
# 文件名：array_indexing_slicing_example2.py
import numpy as np

a: np.ndarray = np.array([
    [11, 12, 13, 14], [15, 16, 17, 18], [19, 20, 21, 22]
])
row_r1: np.ndarray = a[2, :]  # 第三行的一维视图
row_r2: np.ndarray = a[2:3, :]  # 第三行的二维视图
print(row_r1, row_r1.shape)  # [19 20 21 22] (4,)
print(row_r2, row_r2.shape)  # [[19 20 21 22]] (1, 4)

col_r1: np.ndarray = a[:, 2]
col_r2: np.ndarray = a[:, 2:3]
print(col_r1, col_r1.shape)  # [13 17 21] (3,)
print(col_r2, col_r2.shape)
# [[13]
#  [17]
#  [21]] (3, 1)
```

## 原文第 8 页：索引、切片与形状图解

原图使用一个 3×3 网格，着色表示选中区域，其对应关系如下。

| 表达式 | 选中的区域 | 结果形状 |
|---|---|---|
| `arr[:2, 1:]` | 前两行、后两列 | `(2, 2)` |
| `arr[2]` | 第三行 | `(3,)` |
| `arr[2, :]` | 第三行 | `(3,)` |
| `arr[2:, :]` | 第三行，保留行维度 | `(1, 3)` |
| `arr[:, :2]` | 所有行、前两列 | `(3, 2)` |
| `arr[1, :2]` | 第二行的前两个元素 | `(2,)` |
| `arr[1:2, :2]` | 第二行的前两列，保留二维结构 | `(1, 2)` |

## 原文第 9 页：整数数组索引

整数数组索引允许从另一个数组中自由选取元素，构造新的数组，也称花式索引（Fancy Indexing）或高级索引（Advanced Indexing）。

```python
# 文件名：integer_array_indexing_example.py
import numpy as np

a: np.ndarray = np.array([[7, 8], [9, 10], [11, 12]])
# 两个索引列表逐对配合，结果形状为 (3,)
print(a[[0, 1, 2], [1, 0, 1]])  # [8 9 12]
print(np.array([a[0, 1], a[1, 0], a[2, 1]]))  # 等价写法
# 同一个源元素可以重复选取
print(a[[1, 1], [0, 0]])  # [9 9]
print(np.array([a[1, 0], a[1, 0]]))  # 等价写法
```

## 原文第 10 页：每行选择或修改一个元素

整数数组索引的一种实用技巧，是从矩阵的每一行选择或修改一个元素。

```python
# 文件名：integer_array_indexing_example2.py
import numpy as np

a: np.ndarray = np.array([
    [13, 14, 15], [16, 17, 18], [19, 20, 21], [22, 23, 24]
])
print(a)
b: np.ndarray = np.array([1, 0, 2, 1])  # 每一行要选择的列索引
print(a[np.arange(4), b])  # [14 16 21 23]
a[np.arange(4), b] += 5  # 把每行被选中的元素增加 5
print(a)
# [[13 19 15]
#  [21 17 18]
#  [19 20 26]
#  [22 28 24]]
```

## 原文第 11 页：布尔数组索引

布尔数组索引可以选取满足指定条件的元素，也属于花式索引或高级索引。

```python
# 文件名：boolean_array_indexing_example.py
import numpy as np

a: np.ndarray = np.array([[7, 8], [9, 10], [11, 12]])
bool_idx: np.ndarray = a < 10  # 生成同形状的布尔数组
print(bool_idx)
# [[ True  True]
#  [ True False]
#  [False False]]
# 取出 True 对应的元素，得到一维数组
print(a[bool_idx])  # [7 8 9]
print(a[a < 10])  # 用一条语句完成相同操作
```

## 原文第 12 页：组合布尔条件

可以对布尔数组应用逻辑运算来筛选元素：`&` 表示“与”，`|` 表示“或”，`~` 表示“非”。组合时，每个条件必须分别加括号。

```python
# 文件名：logical_operators_example.py
import numpy as np

a: np.ndarray = np.array([[7, 8], [9, 10], [11, 12]])
result: np.ndarray = a[(0 < a) & (a < 10)]
print(result)  # [7 8 9]
```

## 原文第 13 页：NumPy 数据类型

数组中的元素具有相同的数据类型。NumPy 提供多种类型；创建数组时会尝试推断合适的类型，通常也可以通过可选参数明确指定。

```python
# 文件名：dtype_example.py
import numpy as np

x: np.ndarray = np.array([3, 4])  # 自动推断类型
print(x.dtype)  # 原文环境：int64
x = np.array([3.5, 4.5])
print(x.dtype)  # float64
x = np.array([3, 4], dtype=np.float32)  # 显式指定类型
print(x.dtype)  # float32
```

## 原文第 14 页：数据类型一览

| 类别 | 数据类型 | 说明 |
|---|---|---|
| 有符号整数 | `np.int8`、`np.int16`、`np.int32`、`np.int64` | 分别为 8、16、32、64 位有符号整数 |
| 无符号整数 | `np.uint8`、`np.uint16`、`np.uint32`、`np.uint64` | 分别为 8、16、32、64 位无符号整数 |
| 浮点数 | `np.float16`、`np.float32`、`np.float64`、`np.float128` | 原文分别称为 16、32、64、128 位浮点数 |
| 复数 | `np.complex64`、`np.complex128`、`np.complex256` | 原文分别称为 64、128、256 位复数 |
| 布尔值 | `np.bool_` | `True` / `False` |
| 字符串 | `np.str_` | 原文写作“可变长度字符串”，见译注 |
| 字节串 | `np.bytes_` | 字节字符串 |
| 对象 | `np.object_` | 保存任意对象的通用类型 |
| 日期时间 | `np.datetime64` | 日期与时间 |
| 时间差 | `np.timedelta64` | 时间间隔 |
| 原始数据 | `np.void` | 灵活的数据类型，例如原始字节或结构化记录 |

> 译注：传统 `np.str_` 数组使用固定宽度 Unicode 字符串；它不是专门的可变长度字符串类型。`float128`、`complex256` 是否存在及其精度取决于平台，不能假定所有电脑均支持。

## 原文第 15 页：数组数学运算

基本数学运算逐元素进行，既能使用运算符，也能调用 NumPy 函数。

```python
# 文件名：array_math_example.py
import numpy as np

x: np.ndarray = np.array([[2, 3], [4, 5]], dtype=np.float64)
y: np.ndarray = np.array([[6, 7], [8, 9]], dtype=np.float64)
print(x + y)
print(np.add(x, y))  # 都是 [[8., 10.], [12., 14.]]
print(x - y)
print(np.subtract(x, y))  # 都是 [[-4., -4.], [-4., -4.]]
print(x * y)
print(np.multiply(x, y))  # 都是 [[12., 21.], [32., 45.]]
print(x / y)
print(np.divide(x, y))
# [[0.33333333 0.42857143]
#  [0.5        0.55555556]]
print(np.sqrt(x))  # 逐元素求平方根
# [[1.41421356 1.73205081]
#  [2.         2.23606798]]
```

## 原文第 16 页：向量、矩阵和张量

向量是一维数值数组，矩阵是二维数值数组，张量在本讲义中指三维或更高维的数值数组。这些结构用于表示数值数据并执行各种操作，在统计、机器学习和计算机科学中十分重要。

> 译注：这是本课程的入门分类；广义数学定义中的张量也包括标量、向量与矩阵。

## 原文第 17 页：点积

两个长度相同的向量，其对应元素相乘后求和，称为点积。结果是一个标量。

原图中的计算：`[1, 2, 3]` 与 `[10, 20, 30]` 的点积为：

```text
1×10 + 2×20 + 3×30 = 140
```

## 原文第 18 页：矩阵乘法

矩阵乘法是人工智能中的重要运算，可以理解为把向量点积扩展到矩阵。结果中每个元素来自第一个矩阵某一行与第二个矩阵某一列的点积。

原图：一个 2×3 矩阵乘以一个 3×2 矩阵，结果是 2×2 矩阵。

```text
[[1, 2, 3],     [[10, 11],
 [4, 5, 6]]  ×  [20, 21],
                [30, 31]]

= [[1×10 + 2×20 + 3×30, 1×11 + 2×21 + 3×31],
   [4×10 + 5×20 + 6×30, 4×11 + 5×21 + 6×31]]

= [[140, 146],
   [320, 335]]
```

## 原文第 19 页：点积与矩阵乘法的写法

点积可以通过 `dot` 函数或数组的 `dot` 方法计算。矩阵乘法可以使用：

- `dot` 函数或方法。
- `matmul` 函数。
- `@` 运算符：Python 3.5 起支持，等价于矩阵乘法的 `matmul`。

对于维数大于 2 的数组，`dot` 和 `matmul` 的结果可能不同。原文建议矩阵乘法使用 `matmul` 或 `@`。

> 译注：高维情况下不是数值精度上的“小差异”，而是轴组合规则可能不同。

## 原文第 20 页：dot 示例

`dot` 既是 NumPy 函数，也是数组实例方法。

```python
# 文件名：dot_product_example.py
import numpy as np

x: np.ndarray = np.array([[2, 4], [6, 8]])
y: np.ndarray = np.array([[1, 3], [5, 7]])
v: np.ndarray = np.array([8, 9])
w: np.ndarray = np.array([10, 11])
print(v.dot(w))  # 向量点积：179
print(np.dot(v, w))  # 179
print(x.dot(v))  # 矩阵乘向量：[52 120]
print(np.dot(x, v))  # [52 120]
print(x.dot(y))  # 矩阵乘矩阵：[[22, 34], [46, 74]]
print(np.dot(x, y))
```

## 原文第 21 页：matmul 与 @ 示例

`matmul` 通过 NumPy 函数调用，而不是数组的同名实例方法。

```python
# 文件名：matrix_operations.py
import numpy as np

a: np.ndarray = np.array([[2, 3], [5, 7]])
b: np.ndarray = np.array([[4, 1], [6, 3]])
u: np.ndarray = np.array([8, 9])
v: np.ndarray = np.array([10, 11])
print(np.matmul(u, v))  # 向量内积：179
print(u @ v)  # 179
print(np.matmul(a, u))  # 矩阵乘向量：[43 103]
print(a @ u)
print(np.matmul(a, b))  # 矩阵乘矩阵：[[26, 11], [62, 26]]
print(a @ b)
```

## 原文第 22 页：mean 函数

NumPy 提供许多数组计算函数，平均值函数 `mean` 是其中之一。

```python
# 文件名：mean_func.py
import numpy as np

y: np.ndarray = np.array([[5, 10], [15, 20]])
print(np.mean(y))  # 所有元素的平均值：12.5
print(np.mean(y, axis=0))  # 每列平均值：[10. 15.]
print(np.mean(y, axis=1))  # 每行平均值：[7.5 17.5]
```

## 原文第 23 页：矩阵转置

除了数学计算，还经常需要调整数组形状或结构。矩阵（二维数组）转置交换行与列，可以使用 `.T` 属性、`np.transpose()` 函数或数组的 `.transpose()` 方法。

```python
# 文件名：transpose_example.py
import numpy as np

a: np.ndarray = np.array([[5, 6], [7, 8]])
print(a)  # [[5, 6], [7, 8]]
print(a.T)  # [[5, 7], [6, 8]]
print(np.transpose(a))  # 相同结果
print(a.transpose())  # 相同结果
```

## 原文第 24 页：多维数组转置参数

多维数组也可以转置。`axes` 参数允许指定轴的新顺序。

```python
np.transpose(array, axes=None)
```

- `array`：要转置的数组。
- `axes`：默认 `None`，省略时反转所有轴的顺序；指定时应为 `[0, 1, ..., N-1]` 的一个排列，使用元组或列表表示，其中 `N` 是数组维数。

## 原文第 25 页：三维数组转置

```python
# 文件名：transpose_example2.py
import numpy as np

# 2 层、每层 4 行、每行 3 列，数值从 0 到 23
array: np.ndarray = np.array([
    [[0, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11]],
    [[12, 13, 14], [15, 16, 17], [18, 19, 20], [21, 22, 23]],
])
# 原轴 2 移到最前，原轴 0 移到中间，原轴 1 移到最后
print(np.transpose(array, [2, 0, 1]))
print(array.transpose([2, 0, 1]))  # 等价
# [[[ 0  3  6  9]
#   [12 15 18 21]]
#  [[ 1  4  7 10]
#   [13 16 19 22]]
#  [[ 2  5  8 11]
#   [14 17 20 23]]]
```

## 原文第 26 页：一维数组转置没有效果

```python
# 文件名：transpose_example3.py
import numpy as np

vector: np.ndarray = np.array([1, 2, 3])
print(vector)  # [1 2 3]
print(vector.T)  # [1 2 3]
print(np.transpose(vector))  # [1 2 3]
```

## 原文第 27 页：数组变形 reshape

变形就是改变数组的形状。形状表示每个维度中的元素数量。变形可以增加或减少维数，也可以改变各维大小，但总元素数必须兼容。

```python
np.reshape(array, newshape)
```

- `array`：要变形的数组。
- `newshape`：整数或整数元组。单个整数表示生成该长度的一维数组。允许将一个维度设为 `-1`，由元素总数和其他维度自动推算。

> 译注：这里按原文保留参数名；使用位置参数可避免新版中参数名调整带来的差异。

## 原文第 28 页：变形示例与挑战

```python
# 文件名：reshape_example.py
import numpy as np

array1: np.ndarray = np.array([
    10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120
])
array2: np.ndarray = array1.reshape(4, 3)  # 4 行 3 列
# array2 = array1.reshape(4, -1) 也能得到相同结果
print(array2)
# [[ 10  20  30]
#  [ 40  50  60]
#  [ 70  80  90]
#  [100 110 120]]
print("array2 的形状：", array2.shape)  # (4, 3)
```

挑战：如何用一行代码创建以下数组？

```text
[[[ 0,  1,  2,  3], [ 4,  5,  6,  7], [ 8,  9, 10, 11]],
 [[12, 13, 14, 15], [16, 17, 18, 19], [20, 21, 22, 23]]]
```

原文答案：

```python
array: np.ndarray = np.arange(24).reshape(2, 3, 4)
```

## 原文第 29 页：扩展数组维度

`np.newaxis` 与 `np.expand_dims()` 可以在数组中引入新轴。`np.newaxis` 就是 `None` 的别名，在索引方括号内指定位置，会插入大小为 1 的新维度。

```python
np.expand_dims(arr, axis)
```

- `arr`：需要扩展的数组。
- `axis`：整数或整数元组，表示在扩展后的轴序列中，新轴应插入的位置。

## 原文第 30 页：使用 newaxis 扩展维度

```python
# 文件名：newaxis_example.py
import numpy as np

array1: np.ndarray = np.array([10, 20, 30, 40, 50])
print(array1)  # [10 20 30 40 50]
array2: np.ndarray = array1[np.newaxis]  # 一维数组转成二维行向量
print(array2)  # [[10 20 30 40 50]]
array3: np.ndarray = array1[None]  # 等价写法
print(array3)
array4: np.ndarray = np.array([[7, 8, 9], [10, 11, 12]])
print(array4)
array5: np.ndarray = array4[np.newaxis]
print(array5)  # [[[7, 8, 9], [10, 11, 12]]]，形状 (1, 2, 3)
```

## 原文第 31 页：在末尾新增轴

```python
# 文件名：newaxis_example2.py
import numpy as np

array1: np.ndarray = np.array([[7, 8, 9], [10, 11, 12]])
print(array1)
array2: np.ndarray = array1[:, :, np.newaxis]
# 等价于 array1[..., np.newaxis]
print(array2)
# [[[ 7]
#   [ 8]
#   [ 9]]
#  [[10]
#   [11]
#   [12]]]
print(array2.shape)  # (2, 3, 1)：2 层、3 行、1 列
```

## 原文第 32 页：在开头新增轴

```python
# 文件名：newaxis_example3.py
import numpy as np

array1: np.ndarray = np.array([[5, 6, 7], [8, 9, 10]])
print(array1)
array2: np.ndarray = array1[np.newaxis, :, :]
print(array2)  # [[[5, 6, 7], [8, 9, 10]]]
print(array2.shape)  # (1, 2, 3)：1 层、2 行、3 列
```

> 译注：原文将新轴称为“1 行”，但此例新增的是最外层大小为 1 的轴；以 `(1, 2, 3)` 为准。

## 原文第 33 页：expand_dims 在中间新增轴

```python
# 文件名：expand_dims_example.py
import numpy as np

array1: np.ndarray = np.array([[7, 8, 9], [10, 11, 12]])
print(array1)
array2: np.ndarray = np.expand_dims(array1, axis=1)
print(array2)  # [[[7, 8, 9]], [[10, 11, 12]]]
print(array2.shape)  # (2, 1, 3)：2 层、1 行、3 列
```

## 原文第 34 页：expand_dims 在末尾新增轴

```python
# 文件名：expand_dims_example2.py
import numpy as np

array1: np.ndarray = np.array([[13, 14, 15], [16, 17, 18]])
print(array1)
array2: np.ndarray = np.expand_dims(array1, axis=2)
print(array2)
# [[[13], [14], [15]], [[16], [17], [18]]]
print(array2.shape)  # (2, 3, 1)：2 层、3 行、1 列
```

## 原文第 35 页：视图与副本

视图（view）引用原始数据，经由视图进行的修改会影响原数据。副本（copy）则创建保存相同数据的新对象；修改副本不会影响原对象，因此适合保留原始数据。

```python
# 文件名：view_example.py
import numpy as np

arr: np.ndarray = np.array([1, 2, 3])
view_arr: np.ndarray = arr[1:3]  # 创建视图
view_arr[0] = 10
print(arr)  # [1 10 3]
```

```python
# 文件名：copy_example.py
import numpy as np
import copy

original: np.ndarray = np.array([1, 2, 3])
copy_list: np.ndarray = copy.copy(original)  # 原文称为浅拷贝
copy_list[0] = 10
print(original)  # [1 2 3]
```

## 原文第 36 页：哪些操作产生视图，哪些产生副本

原文列出的视图操作：

| 操作 | 含义 |
|---|---|
| `arr[1:3]` | 数组基本切片 |
| `arr.reshape(new_shape)` | 不改变数据内容的变形；某些非连续布局需要复制 |
| `arr.transpose()` | 转置 |
| `arr[:, :]` | 用基本切片获取子集 |
| `arr.view()` | 创建视图 |
| `arr[np.newaxis]` | 添加新轴 |
| `np.expand_dims(arr, axis)` | 扩展形状 |

原文列出的副本操作：

| 操作 | 含义 |
|---|---|
| `np.copy(arr)` | 复制数组，原文称为深拷贝，见译注 |
| `arr.copy()` | 数组复制方法 |
| 整数数组或布尔数组索引 | 高级索引选取会创建副本 |
| `arr.astype(new_dtype)` | 转换类型，默认复制 |
| `np.array(arr)` | 从已有数组创建新数组，默认复制 |
| `arr.tolist()` | 转成 Python 列表 |
| `arr[np.arange(n)]` | 数组形式的索引产生副本 |
| `arr.flatten()` | 展平为一维副本 |

> 译注：`expand_dims` 返回视图，原文关于“非连续数据例外返回副本”的说明不宜套用于它。`np.copy` / `arr.copy` 复制数组缓冲区，但对 `object` 数组并不递归复制元素对象，不等于通用的 `copy.deepcopy`。`astype(copy=False)` 等参数也会影响是否复制。

## 原文第 37 页：广播

广播（broadcasting）使 NumPy 能够在算术运算中处理形状不同但兼容的数组。常见需求是把一个较小数组反复用于较大数组。

原文将其解释为沿需要扩展的维度重复较小数组。原图展示三种情况：

- `np.arange(3) + 5`：`[0, 1, 2] + 5 → [5, 6, 7]`。
- `np.ones((3, 3)) + np.arange(3)`：每一行都是 `[1, 2, 3]`。
- `np.arange(3).reshape((3, 1)) + np.arange(3)`：得到 `[[0, 1, 2], [1, 2, 3], [2, 3, 4]]`。

> 译注：这里的“重复”是概念上的扩展，并不意味着必须在内存中真的复制多份。具体是否兼容，要按第 41 页规则从末尾维度对齐判断。

## 原文第 38 页：广播的动机——逐行循环

```python
# 文件名：broadcasting_example.py
import numpy as np

# 把向量 v 加到矩阵 x 的每一行，结果放入 y
x: np.ndarray = np.array([[2, 3, 4], [5, 6, 7], [8, 9, 10], [11, 12, 13]])
v: np.ndarray = np.array([2, 1, 2])
y: np.ndarray = np.empty_like(x)  # 与 x 同形状，元素尚未初始化
for i in range(4):
    y[i, :] = x[i, :] + v
print(y)
# [[ 4  4  6]
#  [ 7  7  9]
#  [10 10 12]
#  [13 13 15]]
```

这种方法可以工作，但当矩阵非常大时，显式 Python 循环可能效率较低。

## 原文第 39 页：广播的动机——先复制再相加

把 `v` 加到 `x` 的每一行，相当于先把 `v` 竖向复制多份形成 `vv`，再逐元素相加。

```python
# 文件名：broadcasting_example2.py
import numpy as np

x: np.ndarray = np.array([[2, 3, 4], [5, 6, 7], [8, 9, 10], [11, 12, 13]])
v: np.ndarray = np.array([2, 1, 2])
vv: np.ndarray = np.tile(v, (4, 1))  # 竖向堆叠 4 份 v
print(vv)  # [[2, 1, 2], [2, 1, 2], [2, 1, 2], [2, 1, 2]]
y: np.ndarray = x + vv
print(y)  # 与上一页循环得到的结果相同
```

## 原文第 40 页：直接广播

广播不需要显式生成 `v` 的多份副本。

```python
# 文件名：broadcasting_demo.py
import numpy as np

x: np.ndarray = np.array([[2, 3, 4], [5, 6, 7], [8, 9, 10], [11, 12, 13]])
v: np.ndarray = np.array([2, 1, 2])
y: np.ndarray = x + v
print(y)
# [[ 4  4  6]
#  [ 7  7  9]
#  [10 10 12]
#  [13 13 15]]
```

`x` 的形状为 `(4, 3)`，`v` 为 `(3,)`。广播使 `v` 在运算中表现得像一个每行均为 `v` 的 `(4, 3)` 数组。

## 原文第 41 页：广播规则

1. 两个数组维数不同时，在维数较少的形状左侧补 1，直到形状长度相同。
2. 对于每个对应维度，大小相同，或者其中一个大小为 1，才算兼容。
3. 所有维度都兼容，两个数组才能广播。

广播后，各数组在概念上具有匹配的形状。对于大小为 1、而另一数组大小大于 1 的维度，前者表现得像沿该轴被重复了多次。原文将结果形状描述为各维大小逐项取最大值。

> 译注：最后一句适用于原文中的正长度形状示例；包含长度为 0 的轴时，不能简单用“逐项最大值”概括。

## 原文第 42 页：广播规则示例一

`a = [1, 2, 3]`，`b = [2]`，能否执行 `a * b`？

两者都是一维数组，形状分别为 `(3,)` 和 `(1,)`。因为其中一个轴大小为 1，所以兼容，结果形状为 `(3,)`。

```python
# 文件名：broadcasting_rule1.py
import numpy as np

a: np.ndarray = np.array([1, 2, 3])
print(a.ndim)  # 1
print(a.shape)  # (3,)
b: np.ndarray = np.array([2])
print(b.ndim)  # 1
print(b.shape)  # (1,)
print(a * b)  # [2 4 6]
```

## 原文第 43 页：广播规则示例二

`a` 为 `[1, 2, 3]`，`b` 为 `[[4, 4, 4], [3, 3, 3]]`。两者维数不同，先把 `a` 的形状 `(3,)` 看成 `(1, 3)`，再与 `(2, 3)` 对齐。第一维中 1 可扩展为 2，第二维同为 3，因此结果是 `(2, 3)`。

```python
# 文件名：broadcasting_rule2.py
import numpy as np

a: np.ndarray = np.array([1, 2, 3])
print(a.ndim)  # 1
print(a.shape)  # (3,)
b: np.ndarray = np.array([[4, 4, 4], [3, 3, 3]])
print(b.ndim)  # 2
print(b.shape)  # (2, 3)
print(a * b)  # [[4, 8, 12], [3, 6, 9]]
```

## 原文第 44 页：广播兼容性练习与答案

判断下列两数组能否执行 `a * b`，若能，写出结果形状。

| 题号 | a 的形状 | b 的形状 | 原文答案 |
|---|---|---|---|
| 1 | `(5, 4)` | `(1,)` | 能，`(5, 4)` |
| 2 | `(5, 4)` | `(4,)` | 能，`(5, 4)` |
| 3 | `(15, 3, 5)` | `(15, 1, 5)` | 能，`(15, 3, 5)` |
| 4 | `(15, 3, 5)` | `(3, 5)` | 能，`(15, 3, 5)` |
| 5 | `(15, 3, 5)` | `(3, 1)` | 能，`(15, 3, 5)` |
| 6 | `(16, 6, 7)` | `(16, 6)` | 不能，末尾维度 7 与 6 不兼容 |

## 原文第 45 页：广播的实际应用

广播可以简化计算。下面通过两个例子展示：

1. 数据集中心化：成绩册案例。
2. 计算成对距离：两个数组中各行之间的欧几里得距离。

## 原文第 46 页：例一——数据集中心化

假设有 5 名学生，每人参加 3 次考试，成绩存储在 5×3 数组中。

```python
# 文件名：centering_a_dataset.py
import numpy as np

scores: np.ndarray = np.array([
    [1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15]
])
# 沿第一个轴求平均，得到每次考试的平均分
score_mean: np.ndarray = scores.mean(0)
print(score_mean)  # [7. 8. 9.]
# 使用广播减去各列平均值，完成中心化
scores_centered: np.ndarray = scores - score_mean
print(scores_centered)
# [[-6. -6. -6.]
#  [-3. -3. -3.]
#  [ 0.  0.  0.]
#  [ 3.  3.  3.]
#  [ 6.  6.  6.]]
# 检查中心化后的每列平均值是否为 0
print(scores_centered.mean(axis=0))  # [0. 0. 0.]
```

## 原文第 47 页：例二——成对距离

两个二维数组 `x`、`y` 的形状分别为 `(M, D)` 和 `(N, D)`：行数可以不同，但列数相同。目标是计算 `x` 的每一行与 `y` 的每一行之间的欧几里得距离。

若两行分别为 `(x₀, x₁, …, xＤ₋₁)` 和 `(y₀, y₁, …, yＤ₋₁)`，距离为：

```text
sqrt((x₀-y₀)² + (x₁-y₁)² + … + (xＤ₋₁-yＤ₋₁)²)
```

## 原文第 48 页：成对距离的数据与问题

```python
# 文件名：pairwise_distance.py
import numpy as np

x: np.ndarray = np.array([
    [8.54, 1.54, 8.12], [3.13, 8.76, 5.29], [7.73, 6.71, 1.31]
])  # 形状 (3, 3)
y: np.ndarray = np.array([
    [8.65, 0.27, 4.67], [7.73, 7.26, 1.95]
])  # 形状 (2, 3)
```

问题：需要计算多少个距离？答案：6 个，即 `x` 与 `y` 各行的所有组合。

问题：若 `x` 形状为 `(M, 3)`，`y` 为 `(N, 3)`，需要多少个距离？答案：`M×N`。

## 原文第 49 页：成对距离——变形与广播（续）

```python
reshaped_x: np.ndarray = x.reshape(3, 1, 3)
reshaped_y: np.ndarray = y.reshape(1, 2, 3)
diffs: np.ndarray = reshaped_x - reshaped_y
print("diffs 的形状：", diffs.shape)  # (3, 2, 3)
```

广播后，`diffs[i, j]` 就是 `x[i] - y[j]`，保存这一对行在各列上的差。

## 原文第 50 页：成对距离——平方、求和、开方（续）

```python
print(diffs)
# [[[-0.11  1.27  3.45]
#   [ 0.81 -5.72  6.17]]
#  [[-5.52  8.49  0.62]
#   [-4.60  1.50  3.34]]
#  [[-0.92  6.44 -3.36]
#   [ 0.00 -0.55 -0.64]]]
dists: np.ndarray = np.sqrt(np.sum(diffs**2, axis=2))
# axis=2：沿保存各列差值的轴求和
print(dists)
# [[ 3.67797499  8.45241977]
#  [10.14568381  5.87925165]
#  [ 7.32185769  0.84386018]]
print(dists.shape)  # (3, 2)，即 3 行 2 列
```

## 原文第 51 页：成对距离思考题

能否不用 `reshape`，改用 `np.newaxis` 编写计算两数组成对距离的程序？

同样，能否改用 `np.expand_dims`，代替 `reshape` 完成计算？

原文此页没有提供答案。

## 原文第 52 页：为什么 NumPy 数组更有优势

与 Python 列表相比，NumPy 数组通常具有以下优势：占用内存更少、运行更快、使用更方便。

> 译注：“通常”指适合 NumPy 的同质数值数据与批量运算，不是对所有数据规模、所有操作的绝对保证。

## 原文第 53 页：NumPy 数组与 Python 列表的存储结构

原文说明：NumPy 数组通过一个引用指向一整块连续数据；Python 列表指向一块“引用组成的区域”，其中每个引用再指向完整的 Python 对象。

原图关系可写成：

```text
NumPy 数组对象
  ├─ data ──→ 连续数值区域：[1][2][3][4][5][6][7][8]
  ├─ dimensions：形状信息
  └─ strides：各轴的字节步长

Python 列表对象
  ├─ length：长度
  └─ items ──→ [引用][引用][引用]……
                 ↓     ↓     ↓
              Python 对象（分别保存数值及对象元数据）
```

> 译注：连续缓冲区是典型数值数组的情况；切片、转置等可能形成非连续视图，`object` 数组也需要保存对象引用。

## 原文第 54 页：数组与列表的内存占用

```python
# 文件名：memory_consumption.py
import numpy as np
import sys
import gc

def actualsize(input_object: object) -> int:
    memory_size: int = 0  # 累计对象占用的内存
    ids: set[int] = set()  # 已访问对象的 id，避免重复统计
    objects: list[object] = [input_object]  # 从输入对象开始遍历
    while objects:
        new: list[object] = []  # 记录本轮新访问的对象
        for obj in objects:
            if id(obj) not in ids:
                ids.add(id(obj))
                memory_size += sys.getsizeof(obj)
                new.append(obj)
        # 获取这些对象直接引用的对象，继续下一轮
        objects = gc.get_referents(*new)
    return memory_size

l: list[int] = list(range(0, 1000))
a: np.ndarray = np.arange(1000)
print("整个列表的字节数：", actualsize(l))  # 原文环境：36056
print("整个 NumPy 数组的字节数：", actualsize(a))  # 原文环境：8112
```

> 译注：这是原文的示范性统计方法，不是对所有 Python 扩展对象均适用的通用内存测量器。结果受 Python、NumPy 版本和平台影响。

## 原文第 55 页：数组与列表的耗时比较

```python
# 文件名：time_comparison.py
import numpy as np
import time as t

size: int = 1000000
list1: range = range(size)
list2: range = range(size)
array1: np.ndarray = np.arange(size)
array2: np.ndarray = np.arange(size)
initialTime: float = t.time()
resultList: list[int] = [(a * b) for a, b in zip(list1, list2)]
print("列表计算耗时：", t.time() - initialTime, "秒")
# 原文示例约 0.130242586 秒
initialTime = t.time()
resultArray: np.ndarray = array1 * array2
print("NumPy 数组计算耗时：", t.time() - initialTime, "秒")
# 原文示例约 0.006006956 秒
```

> 译注：原文变量 `list1`、`list2` 实际是 `range` 对象，不是已经构造的列表；结果 `resultList` 才是列表。实际速度取决于运行环境，不能把示例耗时当作固定倍数。

## 原文第 56 页：相同运算对数组与列表的影响

```python
# 文件名：effect_of_operations.py
import numpy as np

ls: list[int] = [1, 2, 3]
arr: np.ndarray = np.array(ls)
try:
    ls = ls + 4
except TypeError:
    print("列表不支持 list + int")
try:
    arr = arr + 4  # 数组每个元素加 4
    print("修改后的 NumPy 数组：", arr)
except TypeError:
    print("NumPy 数组不支持 array + int")
```

输出：

```text
列表不支持 list + int
修改后的 NumPy 数组： [5 6 7]
```

原文说明：本课程不讲解 `try-except`。

## 原文第 57 页：关键术语与致谢

| 英文 | 中文 |
|---|---|
| Array indexing and slicing | 数组索引与切片 |
| Advanced indexing / Fancy indexing | 高级索引 / 花式索引 |
| Boolean array indexing | 布尔数组索引 |
| Broadcasting | 广播 |
| Dot product | 点积 |
| expand_dims | 扩展维度 |
| Integer array indexing | 整数数组索引 |
| Matrix / Matrix multiplication | 矩阵 / 矩阵乘法 |
| newaxis | 新轴 |
| NumPy array | NumPy 数组 |
| Rank / Shape | 维数（本讲义中的秩）/ 形状 |
| Reshaping | 变形 |
| Sum function | 求和函数 |
| Tensor / Transpose / Vector | 张量 / 转置 / 向量 |

致谢：本讲义资料基于 [Python NumPy 教程](https://cs231n.github.io/python-numpy-tutorial/)，该教程以 [MIT 许可证](https://opensource.org/license/MIT) 发布。

## 原文第 58 页：复习题 1—5

请填空。

1. NumPy 是用于数值计算 Python 的一个____，是 Python 数值与科学计算的核心库。
2. NumPy 数组是具有相同类型的值组成的____，可用非负整数元组索引。
3. 数组的____是整数元组，表示各维度大小。
4. 可以从 Python 的____列表初始化 NumPy 数组，再通过方括号访问元素。
5. ____函数创建全 0 数组。

原文答案：1. 库（library）；2. 网格（grid）；3. 形状（shape）；4. 嵌套（nested）；5. `np.zeros`。

> 译注：第 1 题原文英语句式不顺，此处按原文答案“library”译写。

## 原文第 59 页：复习题 6—11

6. ____函数创建全 1 数组。
7. ____函数创建由指定值填充的常量数组。
8. 数组的____表示维度数量。
9. NumPy 数组可以进行____，从而支持不同形状数组之间的运算。
10. 广播通过沿需要扩展的维度____较小数组，解决不同形状数组的运算问题。
11. 点积是两个等长向量对应值乘积的____。

原文答案：6. `np.ones`；7. `np.full`；8. 秩（rank）；9. 广播（broadcasted）；10. 重复（replicating，概念上的扩展）；11. 和（sum）。

## 原文第 60 页：复习题 12—16

12. 点积的输出是一个____。
13. ____方法用于改变数组形状。
14. ____允许使用另一个数组的数据构造任意选取结果。
15. ____允许给数组添加新轴。
16. 数组对象的____属性用于反转轴顺序。

原文答案：12. 标量（scalar）；13. `reshape`；14. 整数数组索引；15. `np.newaxis`；16. `T`。

> 译注：原文第 14、15 题使用“函数”一词，但整数数组索引是一种索引方式，`np.newaxis` 是索引标记，不是可调用函数。

## 原文第 61 页：复习题 17—20

17. ____是人工智能的重要运算，是点积的矩阵版本。
18. NumPy 提供许多数组计算函数，其中十分有用的一个是____函数。
19. ____函数计算数组全部元素的和。
20. 整数数组索引允许重复使用源数组的同一元素，也可以对矩阵多行中的元素进行____。

原文答案：17. 矩阵乘法；18. `sum`；19. `np.sum`；20. 选择或修改。

## 原文第 62 页：复习题 21—23

21. ____引用原数据，因此经由它的修改会影响原数据。
22. 要创建保存相同数据的新对象、又不影响原对象，应使用____。
23. 对____的修改不会影响原对象。

原文答案：21. 视图；22. 副本；23. 副本。

## 原文第 63 页：练习题 1—14（打印结果）

1. 创建长度为 15 的全 0 数组 `A`。
2. 求数组 `A` 的内存大小。
3. 创建取值从 20 到 60 的数组 `B`。
4. 创建顺序与 `B` 相反的数组 `C`。
5. 创建 4×4 数组 `D`，从上到下、从左到右依次填入 0 到 15。
6. 求 `E = [[3, 4, 5], [6, 7, 8]]` 的维度大小。
7. 求 `F = [0, 3, 0, 0, 4, 0]` 中非零元素的索引。
8. 创建 3×3×3 随机数组 `G`。
9. 求 `H = [1, 13, 0, 56, 71, 22]` 的最大值。
10. 求 `H` 的最小值。
11. 求 `H` 的平均值。
12. 求 `H` 的标准差。
13. 求 `H` 的中位数。
14. 转置数组 `D`。

## 原文第 64 页：练习题 15—27（打印结果）

15. 把 `[4, 5, 6]` 追加到 `I = [1, 2, 3]`。
16. 对 `J = [1, 2, 3]` 和 `K = [4, 5, 6]` 分别逐元素加、减、乘、除。
17. 求数组 `I` 全部元素之和。
18. 求数组 `I` 的自然对数。
19. 使用 `full` / `repeat` 创建 `L = [8, 8, 8, 8, 8]`。
20. 对 `M = [2, 5, 7, 3, 6]` 排序。
21. 求 `M` 最大值所在索引。
22. 求 `M` 最小值所在索引。
23. 求使 `M` 有序排列的元素索引序列。
24. 求 `N = [[6, 1, 1], [4, -2, 5], [2, 8, 7]]` 的逆矩阵。
25. 求 `N` 各元素的绝对值。
26. 提取 `O = [[11, 22, 33], [44, 55, 66], [77, 88, 99]]` 的第三列。
27. 从 `P = [[3, 6, 9, 12], [15, 18, 21, 24], [27, 30, 33, 36], [39, 42, 45, 48], [51, 54, 57, 60]]` 提取奇数行、偶数列组成的子数组。

## 原文第 65 页：练习答案 1—15

```python
import numpy as np  # 译注补充：运行答案前先导入

# 1
A = np.zeros(15)
print(A)
# 2：元素缓冲区占用字节数，不含数组对象的其他开销
print(A.size * A.itemsize)
# 3
B = np.arange(20, 61)
print(B)
# 4
C = B[::-1]
print(C)
# 5
D = np.arange(16).reshape(4, 4)
print(D)
# 6
E = np.array([[3, 4, 5], [6, 7, 8]])
print(E.shape)
# 7
F = np.array([0, 3, 0, 0, 4, 0])
print(F.nonzero())
# 8
G = np.random.random((3, 3, 3))
print(G)
# 9—13
H = np.array([1, 13, 0, 56, 71, 22])
print(H.max())
print(H.min())
print(H.mean())
print(H.std())
print(np.median(H))
# 14
print(np.transpose(D))
# 15
I = np.array([1, 2, 3])
I = np.append(I, [4, 5, 6])
print(I)
```

## 原文第 66 页：练习答案 16—27（续）

```python
# 16
J = np.array([1, 2, 3])
K = np.array([4, 5, 6])
print(J + K)
print(J - K)
print(J * K)
print(J / K)
# 17—18
print(np.sum(I))
print(np.log(I))
# 19：原文 no.full 为笔误，此处更正为 np.full
L = np.full(5, 8)
print(L)
# 另一种写法：L = np.repeat(8, 5)
# 20—23
M = np.array([2, 5, 7, 3, 6])
print(np.sort(M))
print(M.argmax())
print(M.argmin())
print(M.argsort())
# 24—25
N = np.array([[6, 1, 1], [4, -2, 5], [2, 8, 7]])
print(np.linalg.inv(N))
print(np.abs(N))
# 26
O = np.array([[11, 22, 33], [44, 55, 66], [77, 88, 99]])
print(O[:, 2])
# 27
P = np.array([
    [3, 6, 9, 12], [15, 18, 21, 24], [27, 30, 33, 36],
    [39, 42, 45, 48], [51, 54, 57, 60]
])
print(P[::2, 1::2])
```

> 译注：第 27 题“奇数行、偶数列”按日常从 1 开始计数，因此对应索引为 0、2、4 的行和 1、3 的列。第 17、18 题若接着第 15 题执行，`I` 已为 `[1, 2, 3, 4, 5, 6]`；若独立做题则需明确是否重新创建原始 `I`，原文未消除此歧义。

## 原文第 67 页：结束

本讲到此结束！有什么问题吗？

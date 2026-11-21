# Pandas（中文翻译）

原文：`13-pandas-full.pdf`，共 51 页。课程：COMP 1023《Python 编程入门》，2026 年秋季。作者：SC Cheung 教授、Alex Lam 博士、Desmond Tsoi 博士，中国香港特别行政区香港科技大学计算机科学与工程学系。联系邮箱：`{sccheung, lamngok, desmond}@ust.hk`。

翻译说明：按原文页序保留正文、代码、数据、结果和复习题答案，省略重复页脚。API、变量名和案例字段保留英文，说明与注释译为中文。“译注”是对原文条件、笔误或版本差异的补充。原文案例数据仅用于教学，不代表最新城市统计数据。除标明“续”的内容外，示例各自独立；部分输出排版和类型显示会因 Pandas 版本不同而变化。

## 原文第 1 页：封面

COMP 1023《Python 编程入门》：Pandas。作者与机构见文首。

## 原文第 2 页：简介

Pandas 是用于数据处理与分析的强大 Python 库，尤其适合结构化数据。

它提供两种主要结构：一维 `Series` 和二维 `DataFrame`，简化数据管理与运算。主要功能包括数据筛选、聚合、使用透视表重塑数据、处理缺失值和探索性数据分析。

Pandas 建立在 NumPy 之上，增加了数据对齐与直观的索引功能，是数据科学工作流程中的重要工具。

本课程使用 Pandas **2.3.3**。

## 原文第 3 页：第一部分——Series

下面介绍 Pandas 的一维数据结构 `Series`。

## 原文第 4 页：Pandas Series

Series 是带标签的一维数组，可以存放整数、字符串、浮点数等不同种类的数据。每个元素都关联一个索引；索引可以自定义为数值或字符串标签。

可以从列表、字典或 NumPy 数组创建 Series。常见操作包括通过索引访问元素、数学运算和对整个 Series 应用函数。

> 译注：“可以存放不同种类的数据”描述 Series 支持的类型范围，并不意味着每个元素都有独立的 `dtype`；一个 Series 仍有自己的统一 `dtype`。

## 原文第 5 页：创建 Series

```python
# 文件名：series_create.py
import pandas as pd

# 不指定索引，自动生成从 0 开始的整数索引
s1 = pd.Series([10, 20, 30, 40])
print(s1)
# 指定自定义索引
s2 = pd.Series([10, 20, 30, 40],
               index=['first', 'second', 'third', 'fourth'])
print(s2)
# 从字典创建：键成为索引，值成为数据
data = {'first': 10, 'second': 20, 'third': 30, 'fourth': 40}
s3 = pd.Series(data)
print(s3)
```

原文输出：

```text
0    10
1    20
2    30
3    40
dtype: int64

first     10
second    20
third     30
fourth    40
dtype: int64

first     10
second    20
third     30
fourth    40
dtype: int64
```

## 原文第 6 页：访问 Series 元素

两种索引方式：

- 按标签索引：通过创建 Series 时设置的显式标签访问，使用 `.loc[]`。
- 按位置索引：类似 NumPy，使用从 0 开始的整数位置访问，使用 `.iloc[]`。

```python
# 文件名：series_access_elements.py
import pandas as pd

s = pd.Series([10, 20, 30, 40], index=['first', 'second', 'third', 'fourth'])
e1 = s.loc['second']  # 标签为 second 的元素
print(e1)  # 20
e2 = s.iloc[2]  # 位置为 2，即第三个元素
print(e2)  # 30
```

## 原文第 7 页：获取 Series 的值与索引

`.values` 获取值，`.index` 获取索引。原文示例中的值返回为 NumPy 数组，索引返回 Pandas `Index` 对象。Index 支持并集、交集等操作。

```python
# 文件名：series_access_values_index.py
import pandas as pd

s = pd.Series([10, 20, 30, 40], index=['first', 'second', 'third', 'fourth'])
print(s.values)  # [10 20 30 40]
print(s.index)
# Index(['first', 'second', 'third', 'fourth'], dtype='object')
```

> 译注：对于扩展数据类型，`.values` 不一定是普通 NumPy 数组；需要明确转换为 NumPy 时，可以了解 `.to_numpy()`。此处保留原文写法。

## 原文第 8 页：给 Series 元素赋值

可以通过 `.loc[]` 或 `.iloc[]` 赋新值，直接修改这个 Series。

```python
# 文件名：series_assign_values.py
import pandas as pd

s = pd.Series([10, 20, 30], index=['first', 'second', 'third'])
print(s.loc['first'])  # 显式标签：10
print(s.iloc[0])  # 位置：10
s.loc['second'] = 50
print(s)
# first     10
# second    50
# third     30
# dtype: int64
```

## 原文第 9 页：Series 切片

`.loc[]` 与 `.iloc[]` 都可以进行切片：

- `.loc[]` 的标签切片包含起始与结束标签。
- `.iloc[]` 的位置切片与列表、NumPy 类似，包含起点，不包含终点。

原文提醒：不存在的标签可能引发 `KeyError`，并把切片结果描述为包含所选元素的新 Series 视图。

```python
# 文件名：series_slicing.py
import pandas as pd

s = pd.Series([10, 20, 30, 40, 50, 60],
              index=['first', 'second', 'third', 'fourth', 'fifth', 'sixth'])
print(s.loc['third':'fifth'])  # 起止标签都包含
print(s.iloc[2:5])  # 包含位置 2，不包含位置 5
# 两次输出均为：
# third    30
# fourth   40
# fifth    50
# dtype: int64
```

> 译注：单标签访问不存在的标签会报错，但标签切片的边界行为还取决于索引是否排序等条件，不能一概而论。切片修改是否影响来源也受版本和写时复制（Copy-on-Write）机制影响，不能把“视图”理解为一定联动修改。需要更新来源时直接在来源上使用 `.loc[...] = ...`。

## 原文第 10 页：Series 掩码

掩码是一个布尔 Series：`True` 表示满足条件，`False` 表示不满足。与 NumPy 相似，可以通过掩码直接访问或修改满足条件的元素，不一定需要使用 `.loc[]`。

```python
# 文件名：series_masking.py
import pandas as pd

s = pd.Series([10, 15, 25, 5, 30], index=['a', 'b', 'c', 'd', 'e'])
mask = (s > 10) & (s < 30)  # 大于 10 且小于 30
print(mask)
# a    False
# b     True
# c     True
# d    False
# e    False
# dtype: bool
s[mask] = 0
print(s)
# a    10
# b     0
# c     0
# d     5
# e    30
# dtype: int64
```

## 原文第 11 页：第二部分——DataFrame

下面介绍 Pandas 的二维数据结构 `DataFrame`。

## 原文第 12 页：DataFrame 简介

DataFrame 类似电子表格或 SQL 表，由行、列构成。每一列可视为一个 Series；各列可以有不同类型，但共享同一套行索引。

列通过名称访问和操作。DataFrame 适合处理结构化数据，以及执行复杂的数据分析与处理任务。

> 译注：原文写“每列具有唯一名称”，这是清晰建模时的建议，并非 Pandas 强制要求；Pandas 允许重复列名，重复时部分取列操作的返回类型也可能改变。

## 原文第 13 页：从 Series 创建 DataFrame

把列名作为字典键，对应 Series 作为值，传入 `pd.DataFrame()`。此例各 Series 具有相同索引。

```python
# 文件名：dataframe_create1.py
import pandas as pd

sales = pd.Series([100, 150, 200], index=['Product A', 'Product B', 'Product C'])
cost = pd.Series([80, 90, 120], index=['Product A', 'Product B', 'Product C'])
units_sold = pd.Series([20, 30, 15], index=['Product A', 'Product B', 'Product C'])
df = pd.DataFrame({'Sales': sales, 'Cost': cost, 'Units Sold': units_sold})
print(df)
```

| 索引 | Sales | Cost | Units Sold |
|---|---:|---:|---:|
| Product A | 100 | 80 | 20 |
| Product B | 150 | 90 | 30 |
| Product C | 200 | 120 | 15 |

## 原文第 14 页：索引不同时创建 DataFrame

多个 Series 的索引会自动对齐。有匹配标签的位置填入数值，没有对应值的位置填入 `NaN`，表示缺失。

```python
# 文件名：dataframe_create2.py
import pandas as pd

sales = pd.Series([100, 150, 200, 250],
                  index=['Product A', 'Product B', 'Product C', 'Product D'])
cost = pd.Series([80, 90, 120], index=['Product A', 'Product B', 'Product C'])
units_sold = pd.Series([20, 30], index=['Product A', 'Product B'])
df = pd.DataFrame({'Sales': sales, 'Cost': cost, 'Units Sold': units_sold})
print(df)
```

| 索引 | Sales | Cost | Units Sold |
|---|---:|---:|---:|
| Product A | 100 | 80.0 | 20.0 |
| Product B | 150 | 90.0 | 30.0 |
| Product C | 200 | 120.0 | NaN |
| Product D | 250 | NaN | NaN |

> 译注：原文 Cost 列的非缺失值没有显示小数；对于此代码默认生成的浮点列，通常显示为 `80.0` 等，此处按类型统一展示。

## 原文第 15 页：从字典列表创建 DataFrame

列表中的每个字典表示一行。不指定索引时，自动生成整数索引；可通过 `index=['row1', 'row2', 'row3']` 自定义。

```python
# 文件名：dataframe_create3.py
import pandas as pd

data1 = [
    {'name': 'Emma', 'age': 28, 'city': 'Beijing'},
    {'name': 'Liam', 'age': 32, 'city': 'Shanghai'},
    {'name': 'Noah', 'age': 27, 'city': 'Guangzhou'},
]
df1 = pd.DataFrame(data1)
print(df1)
data2 = [
    {'name': 'Sophie', 'age': 29, 'city': 'Shenzhen'},
    {'name': 'Oliver', 'age': 31, 'city': 'Chengdu'},
    {'name': 'Ava', 'age': 26, 'city': 'Hangzhou'},
]
df2 = pd.DataFrame(data2, index=['row1', 'row2', 'row3'])
print(df2)
```

| df1 索引 | name | age | city |
|---|---|---:|---|
| 0 | Emma | 28 | Beijing |
| 1 | Liam | 32 | Shanghai |
| 2 | Noah | 27 | Guangzhou |

| df2 索引 | name | age | city |
|---|---|---:|---|
| row1 | Sophie | 29 | Shenzhen |
| row2 | Oliver | 31 | Chengdu |
| row3 | Ava | 26 | Hangzhou |

## 原文第 16 页：从“键—列表”字典创建 DataFrame

每个键表示列名，对应列表包含该列数据。除非指定 `index`，否则使用递增整数索引。

```python
# 文件名：dataframe_create4.py
import pandas as pd

data_dict = {
    'Name': ['Emma', 'Liam', 'Noah'],
    'Age': [28, 32, 27],
    'City': ['Beijing', 'Shanghai', 'Guangzhou'],
}
df = pd.DataFrame(data_dict)
print(df)
```

| 索引 | Name | Age | City |
|---|---|---:|---|
| 0 | Emma | 28 | Beijing |
| 1 | Liam | 32 | Shanghai |
| 2 | Noah | 27 | Guangzhou |

## 原文第 17 页：从二维 NumPy 数组创建 DataFrame

传入二维 NumPy 数组，可同时指定列名和可选的行索引。

```python
# 文件名：dataframe_create5.py
import numpy as np
import pandas as pd

arr = np.array([
    [28, 32, 27],  # 年龄
    [1, 2, 3],  # ID 或类似标识
    [1, 0, 1],  # 二元信息，例如某项服务是否可用
])
df = pd.DataFrame(arr, columns=['Beijing', 'Shanghai', 'Guangzhou'],
                  index=['Age', 'ID', 'Service Available'])
print(df)
```

| 索引 | Beijing | Shanghai | Guangzhou |
|---|---:|---:|---:|
| Age | 28 | 32 | 27 |
| ID | 1 | 2 | 3 |
| Service Available | 1 | 0 | 1 |

## 原文第 18 页：获取列名与行索引

`.columns` 返回包含列名的 Index，`.index` 返回行索引 Index。两者均可用于后续索引操作。

```python
# 文件名：dataframe_access1.py
import pandas as pd

data = {
    'Name': ['Emma', 'Liam', 'Noah'],
    'Age': [28, 32, 27],
    'City': ['Beijing', 'Shanghai', 'Guangzhou'],
}
df = pd.DataFrame(data)
print(df.columns)  # Index(['Name', 'Age', 'City'], dtype='object')
print(df.index)  # RangeIndex(start=0, stop=3, step=1)
```

## 原文第 19 页：以 NumPy 数组形式访问 DataFrame 数据

`.values` 可以把 DataFrame 数据转换为 NumPy 数组。

```python
# 文件名：dataframe_access2.py
import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [30, 25, 35],
    'Salary': [70000, 80000, 120000],
}
df = pd.DataFrame(data)
arr = df.values
print(arr)
# [['Alice' 30 70000]
#  ['Bob' 25 80000]
#  ['Charlie' 35 120000]]
```

## 原文第 20 页：访问 DataFrame 的一列

把列名写在方括号 `[]` 中，结果为该列对应的 Series。

```python
# 文件名：dataframe_access3.py
import pandas as pd

temperature = pd.Series([22.5, 23.0, 19.5],
                        index=['Monday', 'Tuesday', 'Wednesday'])
humidity = pd.Series([55, 60, 50], index=['Monday', 'Tuesday', 'Wednesday'])
wind_speed = pd.Series([5.5, 3.0, 7.2], index=['Monday', 'Tuesday', 'Wednesday'])
df = pd.DataFrame({'Temperature': temperature, 'Humidity': humidity,
                   'Wind Speed': wind_speed})
print(df['Humidity'])
# Monday       55
# Tuesday      60
# Wednesday    50
# Name: Humidity, dtype: int64
```

## 原文第 21 页：按索引访问 DataFrame 的一行

与 Series 一样，`.loc` 按标签访问，`.iloc` 按位置访问。访问单行返回一个 Series，每列成为其中一个元素，而 Series 的索引是原表列名。

```python
# 文件名：dataframe_access4.py
import pandas as pd

city = pd.Series(['Beijing', 'Shanghai', 'Guangzhou'], index=['A', 'B', 'C'])
population = pd.Series([21542000, 24183300, 14904000], index=['A', 'B', 'C'])
area = pd.Series([16410.54, 6340.5, 7434.4], index=['A', 'B', 'C'])
df = pd.DataFrame({'City': city, 'Population': population, 'Area (sq km)': area})
print(df.loc['A'])
print(df.iloc[0])
# 两次输出相同：
# City               Beijing
# Population        21542000
# Area (sq km)      16410.54
# Name: A, dtype: object
```

## 原文第 22 页：DataFrame 切片

切片可以选择行、列或同时选择两者。原文提醒不要混用位置索引与标签索引。

```python
# 文件名：dataframe_access5.py
import pandas as pd

city = pd.Series(['Beijing', 'Shanghai', 'Guangzhou'], index=['A', 'B', 'C'])
population = pd.Series([21542000, 24183300, 14904000], index=['A', 'B', 'C'])
area = pd.Series([16410.54, 6340.5, 7434.4], index=['A', 'B', 'C'])
df = pd.DataFrame({'City': city, 'Population': population, 'Area (sq km)': area})
# 行从 B 到 C，列从 Population 到 Area (sq km)，两端都包含
print(df.loc['B':'C', 'Population':'Area (sq km)'])
```

| 索引 | Population | Area (sq km) |
|---|---:|---:|
| B | 24183300 | 6340.5 |
| C | 14904000 | 7434.4 |

> 译注：这里指同一次 `.loc` 或 `.iloc` 调用应遵守各自语义：`.loc` 的整数若作为标签，不代表位置。不是说不能通过分步操作转换或结合两种选取方式。

## 原文第 23 页：DataFrame 掩码与切片

可以先用条件掩码选择行，再用切片选择列。

```python
# 文件名：dataframe_access6.py
import pandas as pd

city = pd.Series(['Beijing', 'Shanghai', 'Guangzhou'], index=['A', 'B', 'C'])
population = pd.Series([21542000, 24183300, 14904000], index=['A', 'B', 'C'])
area = pd.Series([16410.54, 6340.5, 7434.4], index=['A', 'B', 'C'])
df = pd.DataFrame({'City': city, 'Population': population, 'Area (sq km)': area})
# 人口超过 1000 万，并且面积小于 7000 平方千米
mask = (df['Population'] > 10000000) & (df['Area (sq km)'] < 7000)
print(df.loc[mask, 'Population':])
```

| 索引 | Population | Area (sq km) |
|---|---:|---:|
| B | 24183300 | 6340.5 |

## 原文第 24 页：新增一列

可以把 Series 赋给 DataFrame 的新列，原表会直接改变；如果同名列已经存在，则替换该列。原文示例使用相同行索引。

```python
# 文件名：dataframe_add_column.py
import pandas as pd

city = pd.Series(['Beijing', 'Shanghai', 'Guangzhou'], index=['A', 'B', 'C'])
population = pd.Series([21542000, 24183300, 14904000], index=['A', 'B', 'C'])
area = pd.Series([16410.54, 6340.5, 7434.4], index=['A', 'B', 'C'])
df = pd.DataFrame({'City': city, 'Population': population, 'Area (sq km)': area})
df['Is Coastal'] = pd.Series([False, True, False], index=['A', 'B', 'C'])
# 此例也等价于 df['Is Coastal'] = [False, True, False]
print(df)
```

| 索引 | City | Population | Area (sq km) | Is Coastal |
|---|---|---:|---:|---|
| A | Beijing | 21542000 | 16410.54 | False |
| B | Shanghai | 24183300 | 6340.50 | True |
| C | Guangzhou | 14904000 | 7434.40 | False |

> 译注：Series 赋列会按标签对齐；索引不同并非必然报错，而可能出现缺失值。列表赋列则按位置，长度需要匹配。

## 原文第 25 页：删除列

通过 `drop(columns=['column1', 'column2'])` 删除指定列。默认返回一个新的 DataFrame，不直接修改原表；要更新变量，可重新赋值。原文还提供 `inplace=True` 的就地修改写法。

```python
# 文件名：dataframe_drop_column.py
import pandas as pd

city = pd.Series(['Beijing', 'Shanghai', 'Guangzhou'], index=['A', 'B', 'C'])
population = pd.Series([21542000, 24183300, 14904000], index=['A', 'B', 'C'])
area = pd.Series([16410.54, 6340.5, 7434.4], index=['A', 'B', 'C'])
df = pd.DataFrame({'City': city, 'Population': population, 'Area (sq km)': area})
print(df)  # 原表同上一页去掉 Is Coastal 列
df = df.drop(columns=['Population', 'Area (sq km)'])
print(df)
#         City
# A    Beijing
# B   Shanghai
# C  Guangzhou
```

> 译注：`df = df.drop(...)` 是接收返回结果，不是对原对象进行就地修改。新版可能调整或弃用部分 `inplace` 用法；本例的重新赋值形式更明确。

## 原文第 26 页：重命名列

向 `.rename()` 的 `columns` 参数传入“旧列名 → 新列名”的字典。

```python
# 文件名：dataframe_rename_column.py
import pandas as pd

city = pd.Series(['Beijing', 'Shanghai', 'Guangzhou'], index=['A', 'B', 'C'])
population = pd.Series([21542000, 24183300, 14904000], index=['A', 'B', 'C'])
area = pd.Series([16410.54, 6340.5, 7434.4], index=['A', 'B', 'C'])
df = pd.DataFrame({'City': city, 'Population': population, 'Area (sq km)': area})
df = df.rename(columns={'Population': 'Pop', 'Area (sq km)': 'Area'})
print(df)
```

| 索引 | City | Pop | Area |
|---|---|---:|---:|
| A | Beijing | 21542000 | 16410.54 |
| B | Shanghai | 24183300 | 6340.50 |
| C | Guangzhou | 14904000 | 7434.40 |

## 原文第 27 页：第三部分——计算

下面介绍 Series 与 DataFrame 的运算、聚合，以及 CSV 读写。

## 原文第 28 页：Series 和 DataFrame 的逐元素运算

原文标题为“一元运算”。NumPy 一元函数可以作用于 Series 或 DataFrame 的各元素，广播机制也可以使用。使用 `+`、`-`、`*`、`/`，可对各元素与一个标量进行运算。

```python
# 文件名：series_dataframe_unary_op.py
import pandas as pd

temperature = pd.Series([32.0, 75.0, 68.5],
                        index=['Monday', 'Tuesday', 'Wednesday'])
df = pd.DataFrame({'Temperature (F)': temperature})
# 华氏温度转摄氏温度
df['Temperature (C)'] = (df['Temperature (F)'] - 32) * 5 / 9
print(df)
```

| 索引 | Temperature (F) | Temperature (C) |
|---|---:|---:|
| Monday | 32.0 | 0.000000 |
| Tuesday | 75.0 | 23.888889 |
| Wednesday | 68.5 | 20.277778 |

> 译注：严格来说，示例是与标量进行的逐元素二元算术运算，不是只有一个操作数的一元运算。这里保留原文讨论范围。

## 原文第 29 页：两个 Series 之间的运算

运算先对齐索引，再逐元素进行。不能匹配的标签位置产生 `NaN`（Not a Number）。本例索引不一致，结果使用对齐后的有序标签。

```python
# 文件名：series_op.py
import pandas as pd

city_a = pd.Series([21540000, 10000000, 8000000],
                   index=['Shanghai', 'Beijing', 'Chongqing'])
city_b = pd.Series([1000000, 2000000, 3000000],
                   index=['Beijing', 'Chongqing', 'Guangzhou'])
result = city_a + city_b
print(result)
# Beijing      11000000.0
# Chongqing    10000000.0
# Guangzhou           NaN
# Shanghai            NaN
# dtype: float64
```

## 原文第 30 页：两个 DataFrame 之间的运算

DataFrame 运算同时对齐行索引和列名，再逐元素运算。如果某一列不能匹配，该列相应运算结果为 `NaN`；行不匹配也会产生缺失。

```python
# 文件名：dataframes_op.py
import pandas as pd

df1 = pd.DataFrame(
    [[21540000, 2400.0], [10000000, 1687.0], [8000000, 315.0]],
    columns=['Population', 'Area (sq mi)'],
    index=['Shanghai', 'Beijing', 'Chongqing'],
)
print(df1)
df2 = pd.DataFrame(
    [[1000000, 743.0], [2000000, 400.0]],
    columns=['Population', 'Area (sq mi)'],
    index=['Beijing', 'Guangzhou'],
)
print(df2)
print(df1 + df2)
```

`df1`：

| 索引 | Population | Area (sq mi) |
|---|---:|---:|
| Shanghai | 21540000 | 2400.0 |
| Beijing | 10000000 | 1687.0 |
| Chongqing | 8000000 | 315.0 |

`df2`：

| 索引 | Population | Area (sq mi) |
|---|---:|---:|
| Beijing | 1000000 | 743.0 |
| Guangzhou | 2000000 | 400.0 |

相加结果：

| 索引 | Population | Area (sq mi) |
|---|---:|---:|
| Beijing | 11000000.0 | 2430.0 |
| Chongqing | NaN | NaN |
| Guangzhou | NaN | NaN |
| Shanghai | NaN | NaN |

## 原文第 31 页：聚合

Series 与 DataFrame 都支持聚合计算。

| 方法 | 计算内容 |
|---|---|
| `.mean()` | 平均值 |
| `.std()` | 标准差 |
| `.min()` | 最小值 |
| `.max()` | 最大值 |
| `.sum()` | 总和 |

## 原文第 32 页：Series 聚合

Series 聚合通常返回单个值，表示这些元素的平均值、总和等。

```python
# 文件名：series_aggregations.py
import pandas as pd

populations = pd.Series([21540000, 10000000, 8000000],
                        index=['Shanghai', 'Beijing', 'Chongqing'])
mean_population = populations.mean()
print(f'平均人口：{mean_population}')  # 13180000.0
```

## 原文第 33 页：DataFrame 聚合

默认按列应用聚合函数，返回一个 Series，其中各元素分别表示各列的统计结果。

```python
# 文件名：dataframes_aggregations.py
import pandas as pd

data = {
    'City': ['Shanghai', 'Beijing', 'Chongqing'],
    'Population': [21540000, 10000000, 8000000],
    'Area (sq mi)': [2400.0, 1687.0, 315.0],
}
df = pd.DataFrame(data)
mean_values = df[['Population', 'Area (sq mi)']].mean()
print(mean_values)
# Population      1.318000e+07
# Area (sq mi)    1.467333e+03
# dtype: float64
```

## 原文第 34 页：从 CSV 文件读取数据

Pandas 可以从 CSV 文件创建 DataFrame：

- `sep` 指定分隔符，例如 `sep=';'` 表示分号分隔。
- 默认从首行读取列名，可以用 `skiprows` 跳过行，例如 `skiprows=1`。
- 自动推断各列类型，方便后续处理。
- 可以指定哪些文本表示缺失；默认情况下空字段会成为缺失值，字符串 `NaN` 也会被识别为缺失。

## 原文第 35 页：CSV 读取示例

```python
# 文件名：csv_loading_data.py
import pandas as pd

df = pd.read_csv('./data/employees.csv',
                 sep=',', skiprows=0, na_values=['N/A', 'Missing'])
print(df)
```

文件 `employees.csv` 内容：

```csv
Name,Department,Salary,Experience
Alice,HR,60000,N/A
Bob,IT,75000,5
Charlie,Finance,80000,7
Diana,IT,90000,Missing
Eve,HR,N/A,3
```

输出数据：

| 索引 | Name | Department | Salary | Experience |
|---|---|---|---:|---:|
| 0 | Alice | HR | 60000.0 | NaN |
| 1 | Bob | IT | 75000.0 | 5.0 |
| 2 | Charlie | Finance | 80000.0 | 7.0 |
| 3 | Diana | IT | 90000.0 | NaN |
| 4 | Eve | HR | NaN | 3.0 |

> 译注：原文 Salary 列省略了非缺失值的小数位；按此代码的默认浮点类型，通常如上显示。`./data` 相对当前工作目录，运行前需要准备该文件。

## 原文第 36 页：保存到 CSV 文件

使用 `.to_csv()` 保存已有 DataFrame。`index=False` 表示不把行索引额外写入文件。

```python
# 文件名：csv_saving_data.py
import pandas as pd
import os

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve'],
    'Department': ['HR', 'IT', 'Finance', 'IT', 'HR'],
    'Salary': [60000, 75000, 80000, 90000, None],
    'Experience': [None, 5, 7, None, 3],
}
df = pd.DataFrame(data)
path = os.path.join('./data', 'employees2.csv')
df.to_csv(path, sep=',', index=False)
```

保存的 `employees2.csv` 内容：

```csv
Name,Department,Salary,Experience
Alice,HR,60000.0,
Bob,IT,75000.0,5.0
Charlie,Finance,80000.0,7.0
Diana,IT,90000.0,
Eve,HR,,3.0
```

> 译注：输出目录必须事先存在；`to_csv` 不会自动创建父文件夹。

## 原文第 37 页：第四部分——自学内容

以下介绍高级索引、缺失值处理与分组。

## 原文第 38 页：Series 的花式索引 / 高级索引

通过一个标签或位置列表，可以选出 Series 的子集。

```python
# 文件名：series_fancy_indexing.py
import pandas as pd

s = pd.Series([10, 20, 30, 40, 50],
              index=['first', 'second', 'third', 'fourth', 'fifth'])
print(s.loc[['first', 'third']])
print(s.iloc[[0, 2]])
# 两次输出均为：
# first    10
# third    30
# dtype: int64
```

## 原文第 39 页：DataFrame 的花式索引 / 高级索引

可以用两个列表选择部分行和部分列：第一个列表指定行标签，第二个指定列名。选中区域也可以被赋值。

```python
# 文件名：dataframe_access7.py
import pandas as pd

city = pd.Series(['Beijing', 'Shanghai', 'Guangzhou'], index=['A', 'B', 'C'])
population = pd.Series([21542000, 24183300, 14904000], index=['A', 'B', 'C'])
area = pd.Series([16410.54, 6340.5, 7434.4], index=['A', 'B', 'C'])
df = pd.DataFrame({'City': city, 'Population': population, 'Area (sq km)': area})
print(df.loc[['A', 'C'], ['City', 'Population']])
df.loc[['A', 'C'], ['City', 'Population']] = ['Updated City', 0]
print(df.loc[['A', 'C'], ['City', 'Population']])
```

更新前：

| 索引 | City | Population |
|---|---|---:|
| A | Beijing | 21542000 |
| C | Guangzhou | 14904000 |

更新后：

| 索引 | City | Population |
|---|---|---:|
| A | Updated City | 0 |
| C | Updated City | 0 |

## 原文第 40 页：组合掩码与花式索引

```python
# 文件名：dataframe_access8.py
import pandas as pd

city = pd.Series(['Beijing', 'Shanghai', 'Guangzhou'], index=['A', 'B', 'C'])
population = pd.Series([21542000, 24183300, 14904000], index=['A', 'B', 'C'])
area = pd.Series([16410.54, 6340.5, 7434.4], index=['A', 'B', 'C'])
df = pd.DataFrame({'City': city, 'Population': population, 'Area (sq km)': area})
# 人口大于 1000 万，并且面积小于 7000 平方千米
mask = (df['Population'] > 10000000) & (df['Area (sq km)'] < 7000)
print(df.loc[mask, ['City', 'Area (sq km)']])
```

| 索引 | City | Area (sq km) |
|---|---|---:|
| B | Shanghai | 6340.5 |

## 原文第 41 页：处理缺失值

Pandas 通过特殊标记值表示缺失。原文介绍两种：Python 的空值 `None`，以及 NumPy 的非数值 `np.nan`。

两者区别是：`None` 是 Python 对象，而 `np.nan` 是浮点值。在数值计算中使用 `np.nan` 通常能保留更高效的数值存储和运算方式。Pandas 支持这两种标记，并会在适当情况下自动转换。

> 译注：这是原文的简化说明，不是全部缺失值体系。Pandas 还使用 `pd.NA`、日期时间类型中的 `NaT` 等；缺失值表示和性能还取决于列的数据类型。

## 原文第 42 页：检查缺失元素

`.isnull()` 返回布尔掩码：缺失位置为 `True`，其他为 `False`。`.notnull()` 相反，非缺失位置为 `True`。

```python
# 文件名：checking_missing.py
import numpy as np
import pandas as pd

s = pd.Series([21540000, None, 8000000, np.nan],
              index=['Shanghai', 'Beijing', 'Chongqing', 'Guangzhou'])
null_mask = s.isnull()
print(null_mask)
# Shanghai     False
# Beijing       True
# Chongqing    False
# Guangzhou     True
# dtype: bool
```

## 原文第 43 页：删除缺失元素

`.dropna()` 可以删除缺失元素。原文 DataFrame 示例使用默认设置：删除包含任一缺失值的行。

```python
# 文件名：remove_missing.py
import numpy as np
import pandas as pd

s = pd.Series([21540000, None, 8000000, np.nan],
              index=['Shanghai', 'Beijing', 'Chongqing', 'Guangzhou'])
print('原始 Series：')
print(s)
print('\n删除缺失值后的 Series：')
print(s.dropna())
print()
df = pd.DataFrame({
    'Population': [21540000, 10000000, None],
    'Area (sq mi)': [2400.0, np.nan, 315.0],
}, index=['Shanghai', 'Beijing', 'Chongqing'])
print('原始 DataFrame：')
print(df)
print('\n删除缺失值后的 DataFrame：')
print(df.dropna())
```

原始 Series：

```text
Shanghai     21540000.0
Beijing             NaN
Chongqing     8000000.0
Guangzhou           NaN
dtype: float64
```

删除缺失值后的 Series：

```text
Shanghai     21540000.0
Chongqing     8000000.0
dtype: float64
```

原始 DataFrame：

| 索引 | Population | Area (sq mi) |
|---|---:|---:|
| Shanghai | 21540000.0 | 2400.0 |
| Beijing | 10000000.0 | NaN |
| Chongqing | NaN | 315.0 |

删除后仅剩：

| 索引 | Population | Area (sq mi) |
|---|---:|---:|
| Shanghai | 21540000.0 | 2400.0 |

## 原文第 44 页：填充缺失值

使用 `.fillna()`，可以用列平均值填充缺失。

```python
# 文件名：fill_missing_values.py
import numpy as np
import pandas as pd

s = pd.Series([10, 20, None, 30, np.nan])
mean_value = s.mean()
print(s.fillna(mean_value))
# 0    10.0
# 1    20.0
# 2    20.0
# 3    30.0
# 4    20.0
# dtype: float64
print()
df = pd.DataFrame({'Sales': [100, 200, 300], 'Profit': [20, np.nan, 50]},
                  index=['Q1', 'Q2', 'Q3'])
mean_profit = df['Profit'].mean()
print(df.fillna(mean_profit))
```

| 索引 | Sales | Profit |
|---|---:|---:|
| Q1 | 100 | 20.0 |
| Q2 | 200 | 35.0 |
| Q3 | 300 | 50.0 |

> 译注：`df.fillna(mean_profit)` 将同一个标量用于整张表的所有缺失位置，而不是自动按各列均值填充。此例只有 Profit 缺失，所以符合目标；若只想填 Profit，可使用 `df.fillna({'Profit': mean_profit})`。

## 原文第 45 页：DataFrame 内部分组

Pandas 可以分组分析数据，再进行均值、求和、计数等聚合，或根据条件筛选。`.groupby()` 返回 `DataFrameGroupBy` 对象，需要指定分组依据的一列或多列，即分组键。

```python
# 文件名：dataframe_grouping_data1.py
import pandas as pd

df = pd.DataFrame({
    'Region': ['North', 'South', 'North', 'South'],
    'Sales': [250, 150, 300, 200],
    'Profit': [50, 30, 70, 40],
})
groupedDf = df.groupby('Region')  # North 和 South 两组
for key, groupDf in groupedDf:
    print(key)
    print(groupDf)
```

North 组：

| 原行索引 | Region | Sales | Profit |
|---|---|---:|---:|
| 0 | North | 250 | 50 |
| 2 | North | 300 | 70 |

South 组：

| 原行索引 | Region | Sales | Profit |
|---|---|---:|---:|
| 1 | South | 150 | 30 |
| 3 | South | 200 | 40 |

## 原文第 46 页：分组后聚合

```python
# 文件名：dataframe_grouping_data2.py
import pandas as pd

df = pd.DataFrame({
    'Department': ['HR', 'IT', 'HR', 'IT'],
    'Salary': [50000, 60000, 55000, 70000],
    'Experience': [2, 5, 3, 7],
})
groupedDf = df.groupby('Department')
# 分别计算各部门工资与经验的平均值，再把分组索引恢复成普通列
result = groupedDf.mean().reset_index()
print(result)
```

| 索引 | Department | Salary | Experience |
|---|---|---:|---:|
| 0 | HR | 52500.0 | 2.5 |
| 1 | IT | 65000.0 | 6.0 |

## 原文第 47 页：关键术语

| 英文 | 中文 |
|---|---|
| Aggregation | 聚合 |
| Advanced indexing / Fancy indexing | 高级索引 / 花式索引 |
| DataFrame | 二维数据表 |
| Label-based indexing | 按标签索引 |
| Pandas | Python 数据处理与分析库 |
| Position-based indexing | 按位置索引 |
| Masking | 掩码筛选 |
| Missing values | 缺失值 |
| Series | 带标签的一维数据结构 |
| Structured data | 结构化数据 |

## 原文第 48 页：复习题 1—5

请填空。

1. ____库是用于____和____的强大 Python 库。
2. Pandas 两种主要数据结构是____和____。
3. Pandas 的主要功能包括____、____和____。
4. Pandas ____是能够容纳多种数据类型的带标签一维数组。
5. Series 每个元素都关联一个____。

原文答案：1. Pandas；数据处理；分析。2. Series（一维）；DataFrame（二维）。3. 数据筛选；聚合；使用透视表重塑数据。4. Series。5. 索引。

## 原文第 49 页：复习题 6—10

6. 可以从____、____或____创建 Series。
7. 按标签访问 Series 元素时，使用____属性。
8. 使用____和____属性，可以获取 Series 的____和____。
9. 使用____和____可以给 Series 元素赋新值。
10. 对 Series 切片，按标签使用____，按位置使用____。

原文答案：6. 列表；字典；NumPy 数组。7. `Series.loc[]`。8. `.values`；`.index`；值；索引。9. `.loc[]`；`.iloc[]`。10. `.loc[]`；`.iloc[]`。

> 译注：第 8 题为中文语序调整，答案也按中文空格顺序排列；原文先问“值与索引”，再问属性名。

## 原文第 50 页：复习题 11—15

11. Pandas 掩码会创建一个____，其中____表示满足条件。
12. 可以把列名放在____中访问 DataFrame 的一列。
13. 在 DataFrame 中分组数据使用____方法。
14. 使用____函数从 CSV 文件加载 DataFrame。
15. 使用____方法把 DataFrame 保存到 CSV 文件。

原文答案：11. 布尔 Series；`True`。12. 方括号 `[]`。13. `groupby()`。14. `pandas.read_csv()`。15. `to_csv()`。

## 原文第 51 页：结束

本讲到此结束！有什么问题吗？

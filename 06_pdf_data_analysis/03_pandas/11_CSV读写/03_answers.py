"""参考答案：读写有说明行的维修记录"""
# 对应 PDF：13-pandas-full.pdf 第 34—36 页
# 课件核心：第34—36页：read_csv的sep/skiprows/na_values，以及to_csv(index=False)。
# 扩展：StringIO把题面文本作为可读文件，pathlib保证工作目录独立，均为输入输出补充。
# 案例数据（据此自行创建对象，不能照抄 examples 的数据）：
# | source_row | 内容（CSV以分号分隔） |
# |---|---|
# | 1 | maintenance export |
# | 2 | device;cost;hours |
# | 3 | M1;120;2 |
# | 4 | M2;Missing;3 |
# | 5 | M3;80;N/A |
# | 6 | M4;0;0 |
# 建议先做练习，再逐段对照下面的实现；assert 用于验证结果。

from io import StringIO
from pathlib import Path
import pandas as pd

raw = 'maintenance export\ndevice;cost;hours\nM1;120;2\nM2;Missing;3\nM3;80;N/A\nM4;0;0\n'
# StringIO接收文本，提供read_csv所需的文件式读取接口；skiprows=1跳过说明行。
data = pd.read_csv(StringIO(raw),sep=';',skiprows=1,na_values=['Missing','N/A'])
print('\n===== data.to_markdown(index=False) =====')
print(data.to_markdown(index=False))
assert data['cost'].sum() == 200 and data['cost'].isna().sum() == 1
assert data['hours'].isna().sum() == 1 and data.loc[3,['cost','hours']].eq(0).all()
out = Path(__file__).resolve().parent / 'outputs'
out.mkdir(exist_ok=True)
path = out / 'maintenance.csv'
data.to_csv(path,index=False)
loaded = pd.read_csv(path)
assert data.equals(loaded) and loaded.columns.tolist() == ['device','cost','hours']
assert loaded.shape == (4,3)

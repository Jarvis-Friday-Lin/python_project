"""参考答案：读取有说明行和缺失标记的文件"""
# 对应 PDF：13-pandas-full.pdf 第 34—36 页
# 建议先完成 02_exercises.py；下面的实现与该题数据、要求一一对应。

from pathlib import Path
import pandas as pd
course=Path(__file__).resolve().parents[2]
data=pd.read_csv(course/"datasets"/"employees_semicolon.csv",sep=";",skiprows=1,na_values=["N/A","Missing"])
assert data["salary"].isna().sum()==1 and data["experience"].isna().sum()==2
target=Path(__file__).resolve().parent/"outputs"/"exercise_employees.csv"
target.parent.mkdir(exist_ok=True)
data.to_csv(target,index=False,encoding="utf-8-sig")
again=pd.read_csv(target,encoding="utf-8-sig")
print('\n===== again.to_markdown(index=False) =====')
print(again.to_markdown(index=False))
pd.testing.assert_frame_equal(data,again)
assert not any(str(c).startswith("Unnamed") for c in again.columns)

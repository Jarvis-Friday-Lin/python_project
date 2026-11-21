"""案例驱动示例：读取有说明行和缺失标记的文件"""
# 对应 PDF：13-pandas-full.pdf 第 34—36 页
# 任务：读取部门员工表，文件首行是说明，分号分隔，用Missing与N/A表示未填写。
# 读取参数必须对应文件真实格式，输出时也要明确是否保存索引。
# 案例数据：
# | name | department | salary | experience |
# |---|---|---:|---:|
# | Alice | HR | 60000 | N/A |
# | Bob | IT | 75000 | 5 |
# | Charlie | Finance | 80000 | 7 |
# | Diana | IT | 90000 | Missing |
# | Eve | HR | N/A | 3 |
# 先看整体路线：
# 第 1 步：查看实际CSV文本，确定表头位置与分隔符。
# 第 2 步：用read_csv识别缺失标记。
# 第 3 步：保存到outputs后重新读取验证。

from pathlib import Path
import pandas as pd
course=Path(__file__).resolve().parents[2]
source=course/"datasets"/"employees_semicolon.csv"
print('\n===== source.read_text(encoding="utf-8-sig") =====')
print(source.read_text(encoding="utf-8-sig"))
# sep=";"指定分隔符；skiprows=1跳过说明行；下一行自动作为表头。
# na_values补充自定义缺失文本，常见N/A默认也会识别。
data=pd.read_csv(source,sep=";",skiprows=1,na_values=["N/A","Missing"],encoding="utf-8-sig")
print('\n===== data.to_markdown(index=False) =====')
print(data.to_markdown(index=False))
print('\n===== data.isna().sum() =====')
print(data.isna().sum())
output=Path(__file__).resolve().parent/"outputs"/"employees_export.csv"
output.parent.mkdir(parents=True,exist_ok=True)
# index=False不把自动行号写成额外一列；utf-8-sig方便Excel识别中文。
data.to_csv(output,index=False,encoding="utf-8-sig",na_rep="")
again=pd.read_csv(output,encoding="utf-8-sig")
print('\n===== again.to_markdown(index=False) =====')
print(again.to_markdown(index=False))
pd.testing.assert_frame_equal(data,again)
assert data["salary"].isna().sum()==1
assert data["experience"].isna().sum()==2

# 学完先自己回答，再看下面的参考答案：
# 1. 这个知识点解决什么类型的问题？
# 2. 为什么当前案例需要它？
# 3. 每一步代码为什么要在此时出现？
# 4. 如果换一种做法，代价和风险是什么？

# 参考答案：
# 1. 正确解析文件结构，并把结果可靠保存。
# 2. 说明行和分号与默认CSV假设不同，Missing也不是数字。
# 3. 先看原文再定读取参数，检查缺失后导出，再读一次防止丢列或多索引。
# 4. csv模块可完成但需自己做类型和缺失转换；默认参数读错不一定报错。

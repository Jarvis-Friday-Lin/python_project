# Pandas 学习路线：从表格对象到分析结果

## Pandas 是什么

Pandas 是一个建立在 Python 之上的开源数据分析库，专门帮助我们处理带有行、列和字段含义的表格数据。Python 的列表、字典和循环可以完成小规模任务；Pandas 进一步提供了带标签的 Series、二维表 DataFrame，以及读取、筛选、统计、清洗和导出等工具。

学习时先从第一节的教务处成绩案例开始：先用基础语法完成，再对比 Pandas 如何减少手工维护，让数据结构和分析步骤更容易检查、复用和扩展。

## 学习主线

先建立 Series 与 DataFrame 的对象概念，再学习读取和检查；之后依次完成选择、筛选、派生列、清洗、时间处理、分组聚合、表连接、透视重塑、自定义转换，最后处理异常值并导出结果。

每节都按同一学习流程进行：

1. 真实业务场景导入。
2. 说明为什么需要这个能力。
3. 拆解对象、输入、输出和形状。
4. 运行示例并停下来思考。
5. 完成练习和边界案例。
6. 对照答案，复盘统计口径。

## 知识点顺序

1. [Series 与 DataFrame](01_series_dataframe/01_examples.py)
2. [读取与观察数据](02_read_inspect/01_examples.py)
3. [选择数据：loc 与 iloc](03_select_loc_iloc/01_examples.py)
4. [条件筛选与 query](04_filter_query/01_examples.py)
5. [新增、修改与删除列](05_modify_assign/01_examples.py)
6. [类型转换与缺失值](06_types_missing/01_examples.py)
7. [重复值与字符串清洗](07_duplicates_strings/01_examples.py)
8. [日期时间处理](08_datetime/01_examples.py)
9. [排序、分组与聚合](09_sort_groupby/01_examples.py)
10. [merge、join 与 concat](10_merge_concat/01_examples.py)
11. [透视表与交叉表](11_pivot_crosstab/01_examples.py)
12. [map、apply 与 transform](12_apply_transform/01_examples.py)
13. [异常值处理与导出](13_outliers_export/01_examples.py)

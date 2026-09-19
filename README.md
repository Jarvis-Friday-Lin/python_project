# Python 学习工程

一套可以直接用 PyCharm 打开的中文 Python 学习资料，覆盖基础语法和数据分析。

## 学习顺序

1. [Python 基础语法](01_python_core/00_course_overview.md)：16 个章节，67 个细分知识点。
2. [Python 数据分析](02_data_analysis/00_course_overview.md)：6 个章节，46 个细分知识点。
3. NumPy → Pandas → Matplotlib → Seaborn → 完整分析流程 → 综合项目。

每个知识点目录都包含：

- `01_examples.py`：带中文注释，按案例逐步推导，并在代码旁解释原因、参数和结果。
- `02_exercises.py`：留给你独立完成的练习。
- `03_answers.py`：完成练习后再查看的参考实现。

## 在 PyCharm 中打开

1. 选择 **Open**，打开本目录，而不是单独打开某个 `.py` 文件。
2. 在项目设置中选择 Python 3.11 或更高版本解释器。
3. 建议在本项目创建 `.venv`，然后在终端执行：`python -m pip install -r requirements.txt`。
4. 从 `01_python_core/00_guide/01_learning_route/01_examples.py` 开始，按编号阅读并运行示例。
5. 右键代码文件选择 **Run**；需要观察执行过程时，在行号处设置断点并选择 **Debug**。

## 学习方法

阅读文档 → 预测示例输出 → 运行示例 → 修改并观察 → 完成练习 → 对照答案 → 勾选检查项。

原项目说明：python 相关。

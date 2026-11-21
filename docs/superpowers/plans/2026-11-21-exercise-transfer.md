# 课件配套迁移练习 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 将 06_pdf_data_analysis 的 53 组练习与答案改为独立迁移案例，而非示例挖空。

**Architecture:** 原有 01_examples.py 不变；02_exercises.py 提供完整 Markdown 注释数据、分级任务与课件页码；03_answers.py 对新任务给出实现、解释和断言。以本目录三份 PDF 为准，扩展 API 就近标注。

**Tech Stack:** Python、NumPy、Pandas、Matplotlib；现有课程虚拟环境。

**Spec:** 本次用户指示及此前确认的 examples / exercises / answers 分工；课程 00_学习路线与文档对应.md。

## Global Constraints

- 只调整本课程，不动用户其他目录、PDF、中文译文和示例代码。
- 练习换场景、换数据、换问题，不仅换数值；数据就在注释表中，不要求学生自编输入。
- 每节注明 PDF 文件、页码、核心考点；课件没有的用法标为“扩展”。
- 基础准备标为前置补充；综合案例注明跨课件组合及扩展。
- 每次数据输出前有表达式分隔符；DataFrame 优先直接 to_markdown。
- 不提交、不推送；不改原始 datasets。输出只写各节 outputs。

## Review Focus

- 练习表与示例表相同：检查 53 对案例表不相等。
- 页码存在但知识点不对应：逐节对照本地 PDF 标题与正文，建立清单。
- 练习写了数据但答案不一致：答案带相同表格，断言验证具体结果。
- 空值、边界、并列、标签错位：在相关节安排指定测试，不一刀切套模板。
- 工作目录与图形环境：答案从任意工作目录可运行，绘图批测使用 Agg。

### Task 1：基线、对应与回归门槛

- [x] 检查本地 PDF 页数、主题及 53 组练习，确认重复问题。
- [x] 增强 tools/verify_course.py：练习与示例数据不得重复、答案表与练习表一致、要求与扩展标记完整。
- [x] 运行增强检查，确认旧练习因重复或缺少新范围标记而失败（53份练习未通过新门槛）。

### Task 2：逐节改写

- [x] 改写基础准备 3、NumPy 19、Pandas 15、Matplotlib 13、综合案例 3 组 02_exercises.py / 03_answers.py。
- [x] 每节提供任务描述、完整输入表、基础/应用任务、可检验结果、必要扩展声明。
- [x] 更新学习路线说明及练习—课件对应清单，保持原有目录和示例导航。

### Task 3：验证与交付

- [x] 运行完整 verify_course.py，106 个示例/答案运行通过、159 文件语法通过；项目目录与/private/tmp工作目录均验证。
- [x] 核对输出文件、Markdown 数据、页码和新任务各项答案覆盖情况；抽查六图报告图片。
- [x] 校验 53 个 examples 与操作前散列一致且git无变更，不提交、不推送。

## 执行记录

本地 PDF 已检查，页数 67 / 51 / 29，章节结构与现有课程对应。原文目录的文件已不存在或字节不同，因此不以外部路径作为来源，后续只引用课程根目录 PDF。
用户已直接授权本项目原目录调整；不创建额外工作树、不改变分支。此次主要为教学内容改写，使用现有运行验证器与新增内容回归检查验证。

最终验证：53组均不再使用示例完整数据表；练习/答案表格相同；53节范围标记齐全。53张题面表格列数一致，学习路线及新清单全部本地链接有效，git diff --check通过。原示例有一项既存DataFrame.drop(inplace=...)弃用警告，未修改原示例以遵守保留要求。

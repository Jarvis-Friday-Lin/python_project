"""案例驱动示例：重复值与字符串清洗"""

# 案例任务：
# 客户名单中邮箱大小写不同、姓名带空格，还有重复导入记录。

# ===== 第一步：先用已经学过的基础语法解决案例 =====
# 任务已经明确，接下来先用列表、字典、循环和算术运算完成它。
# 先看整体路线：
# 第 1 步：先确定真正代表客户身份的业务主键，例如 email。
# 第 2 步：使用 str 访问器统一空格、大小写和文本格式。
# 第 3 步：用 duplicated 找出重复记录，再决定保留哪一条。
# 第 4 步：比较清洗前后的客户数量，并保留重复记录供复核。
# 顺序不能随意交换：先准备并理解输入，才能进行后续转换、分析和检查。

rows = [{"email": "A@X.COM"}, {"email": "a@x.com"}, {"email": "b@x.com"}]
seen = set()
unique = []
for row in rows:
    row["email"] = row["email"].strip().lower()
    if row["email"] not in seen:
        seen.add(row["email"])
        unique.append(row)
print("手工去重：", unique)

# 对不用 Pandas 方案的评价：
# 上面的对照代码可以得到结果，但它把很多工作留给我们自己：也可以把每行转成集合后手工比较；但空格、大小写和业务主键很容易漏掉。str 访问器和 drop_duplicates 更稳定且可复现。所以我们自然会问：有没有一种现成的数据对象，能把这些重复工作统一起来？有，Pandas 的“重复值与字符串清洗”正是为这类表格问题准备的。接下来先用最小步骤试用它，每一步都看清楚输入、输出和为什么要继续下一步。

# ===== 第二步：使用 Pandas 的实现 =====
# 具体函数的入参、关键字参数和返回值，放在每个调用的上一行或下一行说明。
# 进入代码前先确认：本节是在处理哪种表格对象？核心方法要解决什么问题？输入是什么，返回结果的形状会怎样变化？
# 本节是在处理哪种表格对象？主要处理带行索引和列名的 DataFrame，部分方法会先取出其中一列 Series。
# 核心方法要解决什么问题？解决“重复值与字符串清洗”这一类表格分析任务：统一文本格式并根据业务主键识别重复记录。
# 输入是什么，返回结果的形状会怎样变化？输入是案例中的原始表格；主要方法的参数和返回结果如下：Series.str 是字符串方法访问器，strip() 去首尾空白、lower() 转小写；duplicated(subset=...) 标记重复行，drop_duplicates(subset=..., keep=...) 删除重复并决定保留第一条、最后一条或全部。
# 第 1 步：先确定真正代表客户身份的业务主键，例如 email。
# 为什么：先确定业务主键，是因为“重复”不是两行长得像，而是代表了同一个业务实体。
# 调用提示：Series.str 是字符串方法访问器，strip() 去首尾空白、lower() 转小写；duplicated(subset=...) 标记重复行，drop_duplicates(subset=..., keep=...) 删除重复并决定保留第一条、最后一条或全部。
import pandas as pd
data = pd.DataFrame({"name": [" Alice ", "alice", "Bob"], "email": ["A@X.COM", "a@x.com", "b@x.com"]})
# str 是字符串方法访问器；strip() 去空格，title() 统一姓名大小写，lower() 统一邮箱大小写。
data["name_clean"] = data["name"].str.strip().str.title()
data["email"] = data["email"].str.strip().str.lower()
# drop_duplicates(subset=...) 按 email 判断重复，并返回去重后的 DataFrame。
print('\n===== data.drop_duplicates(subset="email").to_markdown(index=False) =====')
print(data.drop_duplicates(subset="email").to_markdown(index=False))
# duplicated(keep=False) 标记重复记录；keep=False 会把重复组中的每一行都标为 True。
print('\n===== data[data["email"].duplicated(keep=False)].to_markdown(index=False) =====')
print(data[data["email"].duplicated(keep=False)].to_markdown(index=False))
# value_counts() 统计每个值出现的次数，适合检查清洗后的频数。
print('\n===== data["email"].value_counts() =====')
print(data["email"].value_counts())
# str.contains(pattern, na=False) 判断文本是否包含指定内容；na=False 把缺失值当作不匹配。
print('\n===== data[data["email"].str.contains("@", na=False)].to_markdown(index=False) =====')
print(data[data["email"].str.contains("@", na=False)].to_markdown(index=False))
# str.replace(old, new, regex=False) 只替换真正的字符，不把 old 当成正则表达式。
print('\n===== data["name"].str.replace(" ", "", regex=False) =====')
print(data["name"].str.replace(" ", "", regex=False))

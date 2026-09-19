"""参考答案：重复值与字符串清洗

这份文件用于自我核对，不要求你写出完全相同的代码。
核对时请思考：如果输入为空、含缺失值或列名改变，代码需要怎样调整？
"""

import pandas as pd


def main():
    # 以下是本节核心操作的参考实现。
    import pandas as pd
    data = pd.DataFrame({"name": [" Alice ", "alice", "Bob"], "email": ["A@X.COM", "a@x.com", "b@x.com"]})
    # str 是字符串方法访问器；strip() 去空格，title() 统一姓名大小写，lower() 统一邮箱大小写。
    data["name_clean"] = data["name"].str.strip().str.title()
    data["email"] = data["email"].str.strip().str.lower()
    # drop_duplicates(subset=...) 按 email 判断重复，并返回去重后的 DataFrame。
    print(data.drop_duplicates(subset="email").to_markdown(index=False))
    # duplicated(keep=False) 标记重复记录；keep=False 会把重复组中的每一行都标为 True。
    print(data[data["email"].duplicated(keep=False)].to_markdown(index=False))
    # value_counts() 统计每个值出现的次数，适合检查清洗后的频数。
    print(data["email"].value_counts())
    # str.contains(pattern, na=False) 判断文本是否包含指定内容；na=False 把缺失值当作不匹配。
    print(data[data["email"].str.contains("@", na=False)].to_markdown(index=False))
    # str.replace(old, new, regex=False) 只替换真正的字符，不把 old 当成正则表达式。
    print(data["name"].str.replace(" ", "", regex=False))


if __name__ == "__main__":
    main()

"""输入与输出：参考答案。

这份答案演示核心写法。练习任务通常还有其他正确实现；请重点比较思路。
"""


def main():
    # 先运行本答案，再逐行对照自己的实现。
    name = "小林"  # 练习时可替换为 input("请输入姓名：")
    age_text = "18"
    age = int(age_text)
    print(f"{name} 明年 {age + 1} 岁")


if __name__ == "__main__":
    main()

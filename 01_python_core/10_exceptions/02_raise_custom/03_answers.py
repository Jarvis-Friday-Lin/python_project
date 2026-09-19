"""抛出与自定义异常：参考答案。

这份答案演示核心写法。练习任务通常还有其他正确实现；请重点比较思路。
"""


def main():
    # 先运行本答案，再逐行对照自己的实现。
    class InvalidAgeError(ValueError):
        """年龄超出允许范围。"""

    def validate_age(age):
        if not 0 <= age <= 150:
            raise InvalidAgeError(f"非法年龄：{age}")
        return age
    print(validate_age(20))


if __name__ == "__main__":
    main()

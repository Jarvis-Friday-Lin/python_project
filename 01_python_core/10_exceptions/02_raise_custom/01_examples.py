"""可运行示例：先预测结果，再执行。"""

class InvalidAgeError(ValueError):
    """年龄超出允许范围。"""

def validate_age(age):
    if not 0 <= age <= 150:
        raise InvalidAgeError(f"非法年龄：{age}")
    return age
print(validate_age(20))

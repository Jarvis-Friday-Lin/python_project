"""参考答案：Series 与 DataFrame"""

import pandas as pd


def main():
    students = pd.DataFrame({
        "name": ["小林", "小周", "小陈", "小李"],
        "class": ["一班", "一班", "二班", "二班"],
        "math": [92, 76, 85, 68],
        "python": [95, 84, 90, 75],
    })
    python_scores = students["python"]  # 单列选择结果是 Series
    average_score = python_scores.mean()
    selected = students.loc[python_scores >= 85, ["name", "class", "python"]]
    print("Series 类型：", type(python_scores).__name__)
    print("Python 平均分：", average_score)
    print("成绩不低于 85 的学生：")
    print(selected)


if __name__ == "__main__":
    main()

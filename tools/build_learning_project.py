from __future__ import annotations

"""一次性生成 Python 基础语法与数据分析学习工程。

本脚本只写入本学习工程约定的目录和文件，方便以后统一补充课程。
"""

from dataclasses import dataclass
from pathlib import Path
from textwrap import dedent


ROOT = Path(__file__).resolve().parents[1]


@dataclass(frozen=True)
class Lesson:
    slug: str
    title: str
    summary: str
    points: tuple[str, ...]
    code: str
    exercise: str


def lesson(slug: str, title: str, summary: str, points: str, code: str, exercise: str) -> Lesson:
    return Lesson(slug, title, summary, tuple(points.split("|")), dedent(code).strip() + "\n", exercise)


CORE = {
    "00_guide": [
        lesson("01_learning_route", "课程使用方法与学习路线", "建立固定学习节奏，按编号完成阅读、运行、练习和复盘。", "一次只学习一个知识点|先预测再运行比直接抄代码更有效|完成练习后再看答案，并记录差异", '''
            steps = ["阅读 README", "预测输出", "运行 examples.py", "完成 exercises.py", "对照 answers.py"]
            for number, step in enumerate(steps, 1):
                print(f"{number}. {step}")
        ''', "制定一周学习计划，写出每天学习时间和目标知识点。"),
        lesson("02_pycharm_usage", "PyCharm 打开与运行项目", "正确打开项目根目录、选择解释器、运行文件并查看控制台。", "Open 应选择整个 python 目录|每个项目应确认解释器路径|Run 直接运行，Debug 可暂停并观察变量", '''
            import sys
            from pathlib import Path
            print("当前解释器：", sys.executable)
            print("当前脚本：", Path(__file__).resolve())
            print("工作目录：", Path.cwd())
        ''', "在 PyCharm 运行本文件，并记录解释器与工作目录的实际路径。"),
        lesson("03_read_errors", "阅读错误与调试步骤", "从 Traceback 最后一行开始识别异常类型、原因和出错位置。", "最后一行通常给出异常类型和原因|向上查找自己代码中的文件与行号|一次只修改一个可验证的原因", '''
            values = ["10", "20", "错误"]
            for text in values:
                try:
                    print(int(text))
                except ValueError as error:
                    print(f"无法转换 {text!r}：{error}")
        ''', "故意制造 NameError、TypeError 和 IndexError，并记录各自的最后一行信息。"),
    ],
    "01_python_basics": [
        lesson("01_first_program", "第一个 Python 程序", "认识源文件、解释器和从上到下的执行顺序。", "`.py` 是 Python 源文件|程序默认从第一条语句向下执行|`print()` 用于把结果显示到控制台", '''
            print("Hello, Python!")  # 字符串需要放在引号中
            print("第一行先执行")
            print("第二行后执行")
        ''', "输出你的姓名、学习目标和今天的日期，每项占一行。"),
        lesson("02_comments_indent", "注释、缩进与代码块", "掌握单行注释、文档字符串和 Python 最重要的缩进规则。", "`#` 后面的内容不会执行|缩进通常使用 4 个空格|同一代码块必须保持相同缩进", '''
            score = 88  # 行尾注释：说明变量含义
            if score >= 60:
                # 缩进表示这条语句属于 if 代码块
                print("考试通过")
        ''', "判断一个温度是否高于 30，并在条件成立时输出提示。"),
        lesson("03_variables_naming", "变量与命名规范", "理解变量是对象的名字，并养成清晰一致的命名习惯。", "变量无需提前声明类型|使用小写字母和下划线命名|不要使用 Python 关键字作为变量名", '''
            student_name = "小林"
            age = 18
            age = age + 1  # 右侧先计算，再把新结果绑定给 age
            print(student_name, age)
        ''', "创建商品名、单价和数量变量，并计算总价。"),
        lesson("04_input_output", "输入与输出", "使用 input 接收文本，并用 print 和 f-string 输出结果。", "`input()` 的返回值永远是字符串|数值计算前通常需要类型转换|f-string 可把表达式嵌入字符串", '''
            name = "小林"  # 练习时可替换为 input("请输入姓名：")
            age_text = "18"
            age = int(age_text)
            print(f"{name} 明年 {age + 1} 岁")
        ''', "接收姓名和出生年份，输出用户的大致年龄。"),
    ],
    "02_data_types": [
        lesson("01_numbers", "整数、浮点数与复数", "学习 Python 的三种主要数字类型及浮点精度特点。", "int 表示任意精度整数|float 通常采用双精度浮点表示|complex 使用 j 表示虚部", '''
            count = 10
            price = 19.9
            point = 3 + 4j
            print(type(count), type(price), type(point))
            print(0.1 + 0.2)  # 浮点数可能出现微小精度误差
        ''', "计算半径为 3.5 的圆面积，并保留两位小数。"),
        lesson("02_bool_none", "布尔值与 None", "理解真假值、比较结果以及表示“暂无值”的 None。", "bool 只有 True 和 False|None 是独立的空值对象|判断 None 推荐使用 `is None`", '''
            is_active = True
            result = None
            print(bool(0), bool(""), bool([]))  # 都是假值
            print(result is None)
        ''', "定义一个可能没有查询结果的变量，并正确判断它是否为 None。"),
        lesson("03_type_conversion", "类型检查与类型转换", "使用 type、isinstance 观察类型，并安全地转换数据。", "`type()` 返回精确类型|`isinstance()` 适合判断继承关系|转换非法文本会抛出 ValueError", '''
            text = "42"
            number = int(text)
            print(number + 8)
            print(type(number))
            print(isinstance(number, int))
        ''', "把字符串 '12.5' 转为浮点数，再转为整数，观察结果。"),
        lesson("04_mutable_immutable", "可变对象与不可变对象", "理解修改对象和重新绑定变量之间的区别。", "数字、字符串、元组通常不可变|列表、字典、集合可变|多个变量可能引用同一个可变对象", '''
            first = [1, 2]
            second = first
            second.append(3)  # 修改的是二者共同引用的列表
            print(first)
            text = "hi"
            text = text + "!"  # 创建新字符串并重新绑定
        ''', "比较列表直接赋值与 `copy()` 后修改产生的不同结果。"),
    ],
    "03_operators_and_expressions": [
        lesson("01_arithmetic", "算术与赋值运算符", "掌握常用数值计算、整除、取余和幂运算。", "+ - * / 是基础算术|`//` 是向下取整除法，`%` 是余数|`**` 表示幂，复合赋值先运算再赋值", '''
            a, b = 17, 5
            print(a / b, a // b, a % b, a ** 2)
            a += 3
            print(a)
        ''', "把 367 秒换算成多少分、多少秒。"),
        lesson("02_comparison_logic", "比较、逻辑与短路求值", "组合多个条件，并理解 and、or 可能跳过后续表达式。", "比较表达式产生布尔值|优先使用括号表达复杂逻辑|and/or 会在结果确定后停止计算", '''
            age = 20
            has_ticket = True
            can_enter = age >= 18 and has_ticket
            print(can_enter)
            print(1 < age < 100)  # Python 支持链式比较
        ''', "判断一个年份是否为闰年。"),
        lesson("03_membership_identity", "成员运算符与身份运算符", "区分“值是否相等”“是否同一对象”“是否包含元素”。", "in/not in 检查成员|== 比较值|is 比较对象身份，通常只用于 None 等单例", '''
            colors = ["red", "blue"]
            print("red" in colors)
            a = [1, 2]
            b = [1, 2]
            print(a == b)  # True：内容相等
            print(a is b)  # False：不是同一个列表
        ''', "分别用 == 和 is 比较两个内容相同的列表，并解释结果。"),
    ],
    "04_control_flow": [
        lesson("01_if_elif_else", "条件分支", "用 if、elif、else 表达互斥或嵌套的业务规则。", "条件从上到下判断|第一个成立的分支执行后跳过其余分支|分支必须正确缩进", '''
            score = 86
            if score >= 90:
                level = "优秀"
            elif score >= 60:
                level = "合格"
            else:
                level = "待提高"
            print(level)
        ''', "根据年龄输出儿童、青少年、成年人或老年人。"),
        lesson("02_match_case", "结构化模式匹配", "使用 match/case 清晰处理多个离散值和简单结构。", "match 从上到下匹配 case|`_` 是兜底模式|适合结构匹配，不是所有 if 的替代品", '''
            command = "start"
            match command:
                case "start":
                    print("开始")
                case "stop":
                    print("停止")
                case _:
                    print("未知命令")
        ''', "用 match/case 把 1～7 转换成星期名称。"),
        lesson("03_for_range", "for 循环与 range", "遍历可迭代对象，并控制整数序列的起点、终点和步长。", "for 逐个取得元素|range 的终点不包含在结果中|enumerate 可同时取得序号和值", '''
            total = 0
            for number in range(1, 6):
                total += number
            print(total)
            for index, name in enumerate(["甲", "乙"], start=1):
                print(index, name)
        ''', "使用 for 计算 1 到 100 之间所有偶数的和。"),
        lesson("04_while", "while 循环", "在次数不确定但继续条件明确时重复执行代码。", "每轮开始前检查条件|循环体应更新条件变量|无法结束的循环称为死循环", '''
            count = 3
            while count > 0:
                print(count)
                count -= 1
            print("开始！")
        ''', "用 while 计算 1 到 10 的乘积。"),
        lesson("05_break_continue_else", "break、continue 与循环 else", "控制单轮或整个循环，并理解循环正常结束时的 else。", "break 立即结束最近一层循环|continue 跳过本轮剩余语句|循环未被 break 打断时执行 else", '''
            numbers = [2, 4, 7, 8]
            for number in numbers:
                if number % 2:
                    print("找到奇数：", number)
                    break
            else:
                print("没有奇数")
        ''', "在列表中查找第一个能被 7 整除的数；找不到时输出提示。"),
    ],
    "05_functions": [
        lesson("01_define_return", "定义函数与返回值", "把可复用逻辑封装为函数，区分打印和返回。", "def 定义函数|return 把结果交给调用者并结束函数|没有显式 return 时返回 None", '''
            def rectangle_area(width, height):
                """计算并返回矩形面积。"""
                return width * height

            area = rectangle_area(3, 4)
            print(area)
        ''', "编写函数，接收摄氏温度并返回华氏温度。"),
        lesson("02_parameter_kinds", "位置、关键字与默认参数", "正确设计和调用带多种参数形式的函数。", "位置参数依赖顺序|关键字参数提高可读性|默认值应放在无默认值参数之后", '''
            def greet(name, message="你好"):
                return f"{message}，{name}"

            print(greet("小林"))
            print(greet(name="小林", message="早上好"))
        ''', "编写计算订单金额的函数，折扣参数默认为 1。"),
        lesson("03_args_kwargs", "可变参数与参数解包", "使用 *args、**kwargs 接收不定数量参数，并解包容器。", "*args 收集额外位置参数为元组|**kwargs 收集额外关键字参数为字典|调用时 * 和 ** 可解包容器", '''
            def report(title, *scores, **info):
                print(title, sum(scores) / len(scores))
                print(info)

            values = [80, 90, 100]
            report("成绩", *values, name="小林")
        ''', "编写函数，接收任意数量价格并返回总价。"),
        lesson("04_scope", "作用域、global 与 nonlocal", "理解名字查找的 LEGB 顺序，谨慎修改外部状态。", "局部变量只在函数中可见|读取全局变量通常无需 global|nonlocal 用于修改最近外层函数变量", '''
            count = 100
            def outer():
                count = 0
                def increase():
                    nonlocal count
                    count += 1
                    return count
                return increase

            counter = outer()
            print(counter(), counter())
        ''', "实现一个闭包计数器，每次调用增加指定步长。"),
        lesson("05_lambda_higher_order", "Lambda 与高阶函数", "把函数作为值传递，使用简短匿名函数描述简单规则。", "函数可以存入变量或作为参数|lambda 只能包含一个表达式|复杂逻辑应使用 def", '''
            students = [("甲", 88), ("乙", 95), ("丙", 81)]
            ordered = sorted(students, key=lambda item: item[1], reverse=True)
            print(ordered)
        ''', "按字符串长度对一个姓名列表排序。"),
        lesson("06_recursion", "递归", "理解函数调用自身、终止条件和调用栈。", "递归必须有终止条件|每次调用应靠近终止条件|深度过大时迭代通常更合适", '''
            def factorial(number):
                if number <= 1:
                    return 1
                return number * factorial(number - 1)

            print(factorial(5))
        ''', "递归计算 1 到 n 的和，并处理 n=0。"),
        lesson("07_decorators", "装饰器基础", "在不改动原函数代码的情况下包装额外行为。", "装饰器接收函数并返回新函数|@语法在定义阶段完成包装|functools.wraps 可保留原函数信息", '''
            from functools import wraps
            def log_call(func):
                @wraps(func)
                def wrapper(*args, **kwargs):
                    print(f"调用 {func.__name__}")
                    return func(*args, **kwargs)
                return wrapper

            @log_call
            def add(a, b):
                return a + b
            print(add(2, 3))
        ''', "编写装饰器，在函数运行前后分别输出提示。"),
    ],
    "06_data_structures": [
        lesson("01_list", "列表", "掌握有序可变序列的增删改查、切片和排序。", "列表可保存不同类型对象|索引从 0 开始，负索引从末尾开始|切片通常不会修改原列表", '''
            values = [3, 1, 2]
            values.append(4)
            values[0] = 30
            print(values[1:3])
            print(sorted(values))  # 返回新列表
            values.sort()          # 原地排序
        ''', "维护一个购物清单，完成添加、删除、替换和排序。"),
        lesson("02_tuple", "元组", "使用不可变序列表达固定记录，并掌握拆包。", "单元素元组必须带逗号|元组本身不可修改|拆包变量数量必须匹配", '''
            point = (10, 20)
            x, y = point
            only_one = (42,)
            print(x, y, only_one)
        ''', "用元组保存 RGB 颜色并拆包到三个变量。"),
        lesson("03_dict", "字典", "用键值映射表示结构化信息并安全访问数据。", "键必须可哈希且唯一|`get()` 可提供缺省值|遍历 items() 可同时获得键和值", '''
            student = {"name": "小林", "score": 90}
            student["age"] = 18
            print(student.get("city", "未知"))
            for key, value in student.items():
                print(key, value)
        ''', "统计一句话中每个字符出现的次数。"),
        lesson("04_set", "集合与 frozenset", "用无序不重复集合完成去重和集合运算。", "set 元素必须可哈希|集合没有位置索引|frozenset 是不可变集合", '''
            a = {1, 2, 3}
            b = {3, 4}
            print(a | b)  # 并集
            print(a & b)  # 交集
            print(a - b)  # 差集
        ''', "求两个班级选课学生的共同成员和全部成员。"),
        lesson("05_comprehensions", "推导式与生成器表达式", "用紧凑表达式完成映射和筛选，同时避免过度嵌套。", "推导式包含结果表达式、循环和可选条件|字典推导式生成键值对|圆括号形式按需生成值", '''
            squares = [n * n for n in range(10) if n % 2 == 0]
            mapping = {n: n * n for n in range(3)}
            lazy_total = sum(n * n for n in range(1000))
            print(squares, mapping, lazy_total)
        ''', "用推导式筛选 1～100 中同时能被 3 和 5 整除的数。"),
        lesson("06_copy", "浅拷贝与深拷贝", "理解嵌套可变对象共享引用导致的连带修改。", "浅拷贝只复制最外层容器|深拷贝递归复制子对象|不可变对象通常可以安全共享", '''
            from copy import copy, deepcopy
            original = [[1], [2]]
            shallow = copy(original)
            deep = deepcopy(original)
            shallow[0].append(9)
            print(original, shallow, deep)
        ''', "构造嵌套列表，分别验证赋值、浅拷贝和深拷贝的效果。"),
    ],
    "07_strings": [
        lesson("01_create_slice", "字符串、转义与切片", "掌握字符串字面量、原始字符串、索引和切片。", "字符串不可变|反斜杠引入转义字符|切片遵循左闭右开区间", '''
            text = "Python"
            print(text[0], text[-1], text[1:4], text[::-1])
            path = r"C:\\new\\test"  # 生成文件中保留反斜杠，演示原始字符串
            print(path)
        ''', "提取邮箱地址中的用户名和域名。"),
        lesson("02_methods", "查找、替换、拆分与连接", "熟悉高频字符串方法并理解它们返回新字符串。", "find 找不到时返回 -1|replace 不修改原字符串|join 的调用者是分隔符", '''
            raw = "  apple,banana,orange  "
            cleaned = raw.strip()
            fruits = cleaned.split(",")
            print(" | ".join(fruits))
            print(cleaned.replace("banana", "pear"))
        ''', "清理一串用逗号分隔且含多余空格的标签。"),
        lesson("03_formatting", "f-string 与格式化", "格式化数值、宽度、对齐和日期，让输出易读。", "f-string 在花括号中求值|`.2f` 保留两位小数|格式说明可控制千位符、百分比和对齐", '''
            name, score, rate = "小林", 93.456, 0.875
            print(f"{name:<8}{score:>8.2f}{rate:>8.1%}")
            amount = 1234567.8
            print(f"金额：{amount:,.2f}")
        ''', "把商品名称、数量、单价和总价输出成对齐的小票。"),
        lesson("04_encoding_bytes", "Unicode、编码与 bytes", "区分字符与字节，正确进行 UTF-8 编码和解码。", "str 表示 Unicode 文本|bytes 表示原始字节|编码是 str→bytes，解码方向相反", '''
            text = "你好，Python"
            data = text.encode("utf-8")
            restored = data.decode("utf-8")
            print(data)
            print(restored)
        ''', "把一段中英文文本编码为 UTF-8，再解码并验证是否相等。"),
        lesson("05_regex", "正则表达式基础", "使用模式完成文本查找、提取和校验。", "优先使用原始字符串书写模式|search 查找一个匹配，findall 查找全部|复杂正则要拆解并配测试样例", '''
            import re
            text = "订单 A102，金额 299 元"
            numbers = re.findall(r"\\d+", text)
            order = re.search(r"[A-Z]\\d+", text)
            print(numbers, order.group() if order else None)
        ''', "从文本中提取所有邮箱地址。"),
    ],
    "08_modules_and_packages": [
        lesson("01_import", "模块导入", "使用 import 复用标准库和自定义模块，并避免名称污染。", "import module 保留命名空间|from 导入具体名称|别名应简短且符合惯例", '''
            import math
            from statistics import mean
            print(math.sqrt(16))
            print(mean([80, 90, 100]))
        ''', "导入 random，生成 1～10 的随机整数。"),
        lesson("02_main_guard", "__name__ 与程序入口", "区分模块被直接运行和被导入两种场景。", "直接运行时 __name__ 为 '__main__'|被导入时值为模块名|入口保护避免导入时执行脚本逻辑", '''
            def main():
                print("程序主入口")

            if __name__ == "__main__":
                main()
        ''', "把一段顶层业务代码移动到 main 函数并添加入口保护。"),
        lesson("03_package_structure", "包结构与导入路径", "理解 __init__.py、绝对导入、相对导入和循环导入。", "包是组织模块的目录|应用代码优先使用清晰的绝对导入|共享定义可下沉以避免循环导入", '''
            # 示例结构：shop/models.py、shop/services.py、shop/__init__.py
            # 在实际包内可写：from shop.models import Product
            print("请结合 README 中的目录图理解包结构")
        ''', "设计一个 calculator 包，包含加减法模块和统一入口。"),
    ],
    "09_files_and_io": [
        lesson("01_pathlib", "路径与 pathlib", "以跨平台方式拼接、检查和遍历文件路径。", "Path 对象比手工拼字符串可靠|`/` 运算符可拼接路径|运行位置和脚本位置不是同一概念", '''
            from pathlib import Path
            project = Path(__file__).resolve().parent
            data_file = project / "sample.txt"
            print(project)
            print(data_file.name, data_file.suffix)
        ''', "打印当前脚本目录，并构造其下 data/example.csv 的路径。"),
        lesson("02_text_files", "文本文件读写", "使用 with 和显式编码安全读写文本。", "with 会自动关闭文件|中文文本推荐指定 encoding='utf-8'|w 会覆盖，a 会追加", '''
            from pathlib import Path
            path = Path(__file__).with_name("demo_output.txt")
            path.write_text("第一行\\n第二行\\n", encoding="utf-8")
            print(path.read_text(encoding="utf-8"))
        ''', "写入三条学习笔记，再逐行读取并显示行号。"),
        lesson("03_json_csv", "JSON 与 CSV", "使用标准库读写两种常见交换格式。", "JSON 支持对象、数组和基础标量|CSV 是表格文本格式|读写文件时都应明确编码和 newline", '''
            import json
            data = {"name": "小林", "skills": ["Python", "Pandas"]}
            text = json.dumps(data, ensure_ascii=False, indent=2)
            restored = json.loads(text)
            print(text)
            print(restored["skills"])
        ''', "把三名学生的字典列表写入 CSV，再读取回来。"),
        lesson("04_context_manager", "上下文管理器", "理解 with 背后的进入、退出和资源清理协议。", "__enter__ 返回 with 绑定的对象|__exit__ 无论正常或异常都会执行|适用于文件、锁和数据库连接", '''
            class Managed:
                def __enter__(self):
                    print("获取资源")
                    return self
                def __exit__(self, exc_type, exc, traceback):
                    print("释放资源")

            with Managed():
                print("使用资源")
        ''', "实现一个计时上下文管理器，输出代码块耗时。"),
    ],
    "10_exceptions": [
        lesson("01_try_except", "try、except、else 与 finally", "只捕获能够处理的异常，并保证必要清理逻辑执行。", "try 只包围可能失败的最小范围|else 在没有异常时执行|finally 无论是否异常都执行", '''
            text = "12a"
            try:
                number = int(text)
            except ValueError as error:
                print("不是合法整数：", error)
            else:
                print(number)
            finally:
                print("转换结束")
        ''', "安全计算两个文本数字的商，分别处理格式错误和除零。"),
        lesson("02_raise_custom", "抛出与自定义异常", "用 raise 主动拒绝非法状态，并定义有业务含义的异常。", "raise 可抛出异常实例|自定义异常通常继承 Exception|异常消息应说明失败原因和输入", '''
            class InvalidAgeError(ValueError):
                """年龄超出允许范围。"""

            def validate_age(age):
                if not 0 <= age <= 150:
                    raise InvalidAgeError(f"非法年龄：{age}")
                return age
            print(validate_age(20))
        ''', "定义余额不足异常，并在取款金额超过余额时抛出。"),
        lesson("03_best_practices", "异常处理最佳实践", "避免静默吞错、超大 try 块和裸 except。", "不要用异常代替普通条件判断|记录足够上下文后再传播异常|`raise ... from ...` 可保留异常因果", '''
            def parse_count(text):
                try:
                    return int(text)
                except ValueError as error:
                    raise ValueError(f"数量必须是整数，收到：{text!r}") from error

            try:
                parse_count("abc")
            except ValueError as error:
                print(error)
        ''', "重构一个使用裸 except 的示例，使其只处理预期异常。"),
    ],
    "11_object_oriented": [
        lesson("01_class_object", "类、对象与构造方法", "用类描述具有共同数据和行为的对象。", "类是对象的模板|self 指向当前实例|__init__ 负责初始化实例状态", '''
            class Student:
                school = "Python 学院"  # 类属性
                def __init__(self, name, score):
                    self.name = name      # 实例属性
                    self.score = score
                def introduce(self):
                    return f"我是{self.name}，成绩{self.score}"

            print(Student("小林", 90).introduce())
        ''', "设计 Product 类，包含名称、价格及计算折后价的方法。"),
        lesson("02_method_types", "实例方法、类方法与静态方法", "根据是否需要实例状态或类状态选择方法类型。", "实例方法首参是 self|类方法用 @classmethod，首参是 cls|静态方法不自动接收实例或类", '''
            class Temperature:
                def __init__(self, celsius): self.celsius = celsius
                @classmethod
                def from_fahrenheit(cls, value): return cls((value - 32) * 5 / 9)
                @staticmethod
                def is_freezing(value): return value <= 0
            temp = Temperature.from_fahrenheit(32)
            print(temp.celsius, Temperature.is_freezing(temp.celsius))
        ''', "为日期类设计一个从 YYYY-MM-DD 文本创建实例的类方法。"),
        lesson("03_encapsulation_property", "封装与 property", "通过受控接口维护对象不变量。", "下划线表示内部实现约定|property 让方法以属性形式访问|setter 可验证赋值", '''
            class Account:
                def __init__(self, balance=0): self._balance = balance
                @property
                def balance(self): return self._balance
                def deposit(self, amount):
                    if amount <= 0: raise ValueError("金额必须为正数")
                    self._balance += amount
            account = Account(100)
            account.deposit(50)
            print(account.balance)
        ''', "创建 Rectangle 类，并用 property 验证宽高必须为正数。"),
        lesson("04_inheritance_super", "继承、重写与 super", "复用基类协议并在子类中扩展行为。", "继承表达 is-a 关系|重写保持方法契约|super() 按方法解析顺序调用父类实现", '''
            class Animal:
                def __init__(self, name): self.name = name
                def speak(self): return "..."
            class Dog(Animal):
                def speak(self): return f"{self.name}: 汪"
            print(Dog("豆豆").speak())
        ''', "建立 Employee 基类及 Manager 子类，重写奖金计算方法。"),
        lesson("05_polymorphism_abc", "多态与抽象类", "面向共同协议编程，并用抽象类约束必要方法。", "多态关注对象能做什么|抽象方法要求子类实现|Python 也常使用鸭子类型", '''
            from abc import ABC, abstractmethod
            class Shape(ABC):
                @abstractmethod
                def area(self): ...
            class Square(Shape):
                def __init__(self, side): self.side = side
                def area(self): return self.side ** 2
            print(Square(3).area())
        ''', "为支付方式定义抽象接口，并实现现金和银行卡支付。"),
        lesson("06_special_methods", "特殊方法与运算符重载", "通过 Python 数据模型让自定义对象支持打印、比较和运算。", "__repr__ 提供开发者表示|__len__ 响应 len()|重载应符合运算符直觉", '''
            class Vector:
                def __init__(self, x, y): self.x, self.y = x, y
                def __repr__(self): return f"Vector({self.x}, {self.y})"
                def __add__(self, other): return Vector(self.x + other.x, self.y + other.y)
            print(Vector(1, 2) + Vector(3, 4))
        ''', "为购物车实现 __len__ 和友好的 __repr__。"),
        lesson("07_dataclass", "dataclass 数据类", "减少以保存数据为主的类的样板代码。", "@dataclass 自动生成 init/repr/eq|default_factory 用于可变默认值|frozen=True 可创建近似不可变对象", '''
            from dataclasses import dataclass, field
            @dataclass
            class Student:
                name: str
                scores: list[int] = field(default_factory=list)
                def average(self): return sum(self.scores) / len(self.scores)
            print(Student("小林", [80, 90, 100]))
        ''', "用 dataclass 表示订单项并计算小计。"),
    ],
    "12_advanced_syntax": [
        lesson("01_iterators", "可迭代对象与迭代器", "理解 for 循环如何通过 iter 和 next 消费数据。", "iter() 获取迭代器|next() 取得下一项|耗尽时抛出 StopIteration", '''
            values = [10, 20]
            iterator = iter(values)
            print(next(iterator))
            print(next(iterator))
        ''', "手动迭代一个字符串，并安全处理迭代结束。"),
        lesson("02_generators", "生成器与 yield", "按需产生值，降低处理大序列时的内存占用。", "含 yield 的函数调用后返回生成器|状态在每次 yield 处暂停|生成器通常只能消费一次", '''
            def countdown(start):
                while start > 0:
                    yield start
                    start -= 1
            print(list(countdown(3)))
        ''', "编写生成器，逐个产生不超过上限的偶数。"),
        lesson("03_contextlib", "contextlib", "用生成器简洁创建上下文管理器。", "@contextmanager 装饰生成器函数|yield 前获取资源，之后释放|清理部分通常放在 finally", '''
            from contextlib import contextmanager
            @contextmanager
            def managed_resource():
                print("打开")
                try: yield "资源"
                finally: print("关闭")
            with managed_resource() as value: print(value)
        ''', "使用 contextmanager 临时切换工作目录并确保恢复。"),
        lesson("04_builtin_tools", "enumerate、zip、map、filter", "熟练使用常见迭代工具，同时优先保证代码可读性。", "enumerate 提供序号|zip 并行组合多个序列|推导式通常比 map/filter 更易读", '''
            names = ["甲", "乙"]
            scores = [90, 85]
            for index, (name, score) in enumerate(zip(names, scores), 1):
                print(index, name, score)
        ''', "把两个等长列表组合成姓名到成绩的字典。"),
        lesson("05_sort_any_all", "排序、any 与 all", "使用 key 描述排序依据，并完成“任一/全部”判断。", "sorted 返回新列表，list.sort 原地修改|key 每个元素通常只计算一次|空序列上 any 为 False、all 为 True", '''
            records = [{"name": "甲", "score": 80}, {"name": "乙", "score": 95}]
            print(sorted(records, key=lambda row: row["score"], reverse=True))
            print(any(row["score"] >= 90 for row in records))
            print(all(row["score"] >= 60 for row in records))
        ''', "按成绩降序、姓名升序对学生记录排序。"),
    ],
    "13_type_hints": [
        lesson("01_basic_hints", "基础类型注解", "为变量、参数和返回值标注预期类型，提高可读性和工具检查能力。", "注解默认不做运行时强制检查|使用 `list[str]` 等内置泛型|`T | None` 表示可能没有值", '''
            def average(values: list[float]) -> float:
                return sum(values) / len(values)
            name: str = "小林"
            result: float | None = average([80.0, 90.0])
            print(name, result)
        ''', "为一个接收商品列表并返回总价的函数添加类型注解。"),
        lesson("02_alias_literal_typeddict", "类型别名、Literal 与 TypedDict", "精确描述有限取值和结构固定的字典。", "type 语句适用于 Python 3.12+ 的类型别名|Literal 限制字面量取值|TypedDict 描述字典字段", '''
            from typing import Literal, TypedDict
            class User(TypedDict):
                name: str
                role: Literal["admin", "member"]
            user: User = {"name": "小林", "role": "member"}
            print(user)
        ''', "用 TypedDict 描述包含名称、价格和库存的商品。"),
        lesson("03_protocol_generic", "Protocol 与泛型", "用结构化协议和类型参数编写可复用接口。", "Protocol 关注所需行为而非继承关系|TypeVar 表示相关位置使用同一类型|泛型可保留容器输入输出类型关系", '''
            from typing import Protocol, TypeVar
            class SupportsClose(Protocol):
                def close(self) -> None: ...
            T = TypeVar("T")
            def first(items: list[T]) -> T:
                return items[0]
            print(first([1, 2, 3]))
        ''', "编写泛型函数 last，返回列表最后一个元素。"),
    ],
    "14_testing_and_debugging": [
        lesson("01_assert_unittest", "assert 与 unittest", "为确定性行为编写自动化测试，并理解断言失败信息。", "assert 适合内部不变量而非用户输入校验|测试应相互独立|覆盖正常、边界和异常情况", '''
            import unittest
            def add(a, b): return a + b
            class AddTests(unittest.TestCase):
                def test_positive(self): self.assertEqual(add(2, 3), 5)
            if __name__ == "__main__": unittest.main()
        ''', "为判断闰年的函数编写至少四个测试。"),
        lesson("02_pytest", "pytest 入门", "使用简洁断言、参数化和异常断言组织测试。", "测试文件和函数通常以 test_ 开头|普通 assert 会被 pytest 增强|参数化适合相同逻辑的多组输入", '''
            # 安装 pytest 后运行：pytest 当前文件
            def divide(a, b): return a / b
            def test_divide():
                assert divide(6, 3) == 2
            print("pytest 示例已定义")
        ''', "使用参数化思路测试多个温度转换输入。"),
        lesson("03_debug_logging", "PyCharm 调试与 logging", "使用断点观察状态，并用日志替代散乱的 print 调试。", "断点会暂停而不修改代码逻辑|单步进入和单步跳过用途不同|日志级别从 DEBUG 到 CRITICAL", '''
            import logging
            logging.basicConfig(level=logging.INFO, format="%(levelname)s:%(message)s")
            values = [1, 2, 3]
            logging.info("开始处理，共 %d 项", len(values))
            for value in values:
                logging.debug("当前值=%s", value)
            logging.info("处理完成")
        ''', "为一个数据清洗函数添加开始、警告和结束日志。"),
    ],
    "15_python_tools": [
        lesson("01_environment_pip", "解释器、虚拟环境与 pip", "让每个项目拥有独立依赖，并确认 PyCharm 使用正确解释器。", "`python -m venv .venv` 创建环境|`python -m pip` 可确保 pip 属于当前解释器|不要提交 .venv 目录", '''
            import sys
            print("解释器：", sys.executable)
            print("版本：", sys.version)
        ''', "在 PyCharm 中查看当前解释器路径并运行本示例核对。"),
        lesson("02_pep8_docs", "PEP 8、命名与文档字符串", "通过一致格式、清晰命名和说明文字降低维护成本。", "函数变量使用 snake_case|类名使用 CapWords|文档字符串说明用途、参数、返回值和异常", '''
            def calculate_total(price: float, quantity: int) -> float:
                """计算订单总价。

                Args:
                    price: 单件价格。
                    quantity: 商品数量。
                Returns:
                    未折扣的订单总价。
                """
                return price * quantity
            print(calculate_total(12.5, 3))
        ''', "重命名一段含 a、b、x 等模糊变量的代码并补充文档字符串。"),
    ],
}


DATA = {
    "00_environment": [
        lesson("01_install_and_pycharm", "安装依赖与配置 PyCharm", "创建独立环境，安装 requirements.txt 并在 PyCharm 中选择解释器。", "先确认 Python 版本|项目解释器应指向当前项目环境|安装后用 import 和版本号验证", '''
            import importlib
            for package in ["numpy", "pandas", "matplotlib", "seaborn"]:
                module = importlib.import_module(package)
                print(package, module.__version__)
        ''', "配置环境后运行示例，记录四个库的版本。"),
        lesson("02_paths_datasets", "数据集与文件路径", "从脚本位置稳定定位 datasets，避免依赖当前工作目录。", "使用 Path(__file__) 定位脚本|原始数据与输出分开存放|不要直接覆盖原始数据", '''
            from pathlib import Path
            data_dir = Path(__file__).resolve().parents[2] / "datasets"
            print(data_dir)
            print([path.name for path in data_dir.glob("*.csv")])
        ''', "定位 sales.csv，并判断文件是否存在。"),
    ],
    "01_numpy": [
        lesson("01_create_array", "创建 ndarray", "使用多种构造函数创建规则数组。", "np.array 从现有数据创建|arange 按步长，linspace 按数量|zeros/ones/full 创建预填充数组", '''
            import numpy as np
            print(np.array([1, 2, 3]))
            print(np.arange(0, 10, 2))
            print(np.linspace(0, 1, 5))
            print(np.zeros((2, 3)))
        ''', "创建一个 3×4、元素全为 5 的数组。"),
        lesson("02_attributes_dtype", "数组属性与 dtype", "查看维度、形状、大小、字节数并控制元素类型。", "ndim 是维数，shape 是各轴长度|size 是元素总数|astype 返回转换类型后的数组", '''
            import numpy as np
            values = np.array([[1, 2], [3, 4]], dtype=np.float64)
            print(values.ndim, values.shape, values.size, values.dtype, values.itemsize)
            print(values.astype(np.int32))
        ''', "创建整数数组并分别转换为 float32 和字符串。"),
        lesson("03_index_slice", "索引、切片与视图", "访问多维元素并理解多数基础切片共享原数据。", "多维索引用逗号分隔|切片是左闭右开|基础切片通常返回视图，修改会影响原数组", '''
            import numpy as np
            matrix = np.arange(12).reshape(3, 4)
            view = matrix[:2, 1:3]
            print(matrix, view, sep="\\n")
            copied = view.copy()
            copied[0, 0] = 999
            print(matrix)
        ''', "从 4×5 数组提取中间两行、后三列。"),
        lesson("04_boolean_fancy", "布尔索引与花式索引", "按条件或指定位置批量选择元素。", "布尔掩码形状需兼容|多个条件使用 & 和 | 并加括号|花式索引通常返回副本", '''
            import numpy as np
            values = np.array([12, 5, 18, 3, 20])
            print(values[values >= 10])
            print(values[(values >= 10) & (values < 20)])
            print(values[[0, 3, 4]])
        ''', "筛选数组中 20～80 之间且能被 3 整除的数。"),
        lesson("05_vectorization_broadcast", "向量化与广播", "用数组运算替代 Python 循环，并理解形状兼容规则。", "向量化把循环交给底层实现|从末尾维度比较广播形状|维度相等或其中一个为 1 才兼容", '''
            import numpy as np
            matrix = np.array([[1, 2, 3], [4, 5, 6]])
            column_offsets = np.array([[10], [20]])
            print(matrix * 2)
            print(matrix + column_offsets)
        ''', "对成绩矩阵的每一科分别加上不同的加分值。"),
        lesson("06_reshape_axes", "形状变换、转置与轴", "在不改变数据的前提下改变观察方式，并正确指定聚合轴。", "reshape 要保持元素总数|T 对二维数组转置|axis=0 跨行聚合，axis=1 跨列聚合", '''
            import numpy as np
            matrix = np.arange(12).reshape(3, 4)
            print(matrix.T)
            print(matrix.sum(axis=0))
            print(matrix.sum(axis=1))
            print(matrix.ravel())
        ''', "把长度 24 的数组变成 2×3×4，并分别沿各轴求和。"),
        lesson("07_combine_split", "数组拼接与拆分", "沿正确轴组合或拆分形状兼容的数组。", "concatenate 在已有轴连接|stack 创建新轴|split 要求可均分，array_split 可不均分", '''
            import numpy as np
            left = np.array([[1], [2]])
            right = np.array([[3], [4]])
            matrix = np.concatenate([left, right], axis=1)
            print(matrix)
            print(np.array_split(matrix, 2, axis=0))
        ''', "分别用 concatenate 和 stack 组合两个一维数组并比较形状。"),
        lesson("08_statistics_nan", "统计函数与缺失值", "计算描述统计并在需要时忽略 NaN。", "mean/median/std 描述集中和离散程度|NaN 会传播到普通聚合|nanmean 等函数可忽略 NaN", '''
            import numpy as np
            values = np.array([10.0, np.nan, 30.0, 40.0])
            print(np.isnan(values))
            print(np.nanmean(values), np.nanmedian(values), np.nanstd(values))
            print(np.nanpercentile(values, [25, 50, 75]))
        ''', "计算含缺失值成绩的均值，并用均值填补缺失项。"),
        lesson("09_random", "随机数生成器", "使用现代 Generator API 生成可复现的随机数据。", "default_rng 创建生成器|固定种子便于复现实验|choice 支持抽样，shuffle 原地打乱", '''
            import numpy as np
            rng = np.random.default_rng(42)
            print(rng.integers(1, 7, size=10))
            print(rng.normal(loc=100, scale=15, size=5))
            print(rng.choice(["A", "B", "C"], size=4, replace=True))
        ''', "模拟投掷两枚骰子 10000 次并估计点数和为 7 的概率。"),
        lesson("10_linear_algebra_io", "线性代数与文件保存", "完成矩阵乘法、方程求解和 NumPy 原生文件读写。", "@ 表示矩阵乘法|linalg.solve 解线性方程|npy 保留形状和 dtype，npz 可保存多个数组", '''
            import numpy as np
            a = np.array([[2.0, 1.0], [1.0, 3.0]])
            b = np.array([5.0, 6.0])
            solution = np.linalg.solve(a, b)
            print(solution)
            print(a @ solution)
        ''', "用矩阵乘法计算两个商品数量与单价构成的总费用。"),
    ],
    "02_pandas": [
        lesson("01_series_dataframe", "Series 与 DataFrame", "理解带标签的一维和二维数据结构。", "Series 由值和索引组成|DataFrame 的列通常代表变量、行代表记录|列可能具有不同 dtype", '''
            import pandas as pd
            scores = pd.Series([88, 95, 82], index=["甲", "乙", "丙"], name="成绩")
            frame = pd.DataFrame({"name": ["甲", "乙"], "score": [88, 95]})
            print(scores)
            print("Series 类型：", type(scores).__name__)
            print("Series 索引：", scores.index.tolist())
            print(frame)
            print("DataFrame 形状：", frame.shape)
            print("DataFrame 列：", frame.columns.tolist())
            students = pd.DataFrame({
                "name": ["小林", "小周", "小陈", "小李"],
                "class": ["一班", "一班", "二班", "二班"],
                "python": [95, 84, 90, 75],
            })
            python_scores = students["python"]  # 选择一列：Series
            print("全班平均分：", python_scores.mean())
            print(students.loc[python_scores >= 85])  # 条件筛选：DataFrame
        ''', "创建 students DataFrame，包含 name、class、math、python 四列；再取出 python 成绩这一列，计算平均分，并筛选平均分不低于 85 的学生。"),
        lesson("02_read_inspect", "读取与观察数据", "读取 CSV/Excel 后先检查形状、列、类型、样例和统计摘要。", "read_csv/read_excel 负责加载|head/info/describe 从不同角度检查|先理解数据再开始清洗", '''
            from pathlib import Path
            import pandas as pd
            path = Path(__file__).resolve().parents[2] / "datasets" / "sales.csv"
            data = pd.read_csv(path)
            print(data.head().to_markdown(index=False))
            # info() 会直接把列名、非空数量和 dtype 打印出来；它主要用于检查结构，返回值本身是 None。
            data.info()
            # describe() 默认偏重数值列；include="all" 才会同时概览 price、quantity 等数值列和 city、product 等文本列。
            # count：非缺失值数量；unique：不同值数量；top：出现次数最多的值；freq：top 出现的次数。
            # mean/std/min/25%/50%/75%/max：数值列的平均值、标准差、最小值、四分位数、中位数、四分之三位数和最大值。
            # 文本列在这些数值统计位置会显示 NaN，这是“该统计不适用于文本”的意思，不是原数据凭空多了缺失。
            print(data.describe(include="all"))
        ''', "读取 students.csv，报告行列数、字段类型和数值摘要。"),
        lesson("03_select_loc_iloc", "选择数据：loc 与 iloc", "按标签或整数位置选择行列，并避免含糊的链式索引。", "loc 使用标签且切片终点通常包含|iloc 使用位置且切片终点不包含|选择单列返回 Series，多列返回 DataFrame", '''
            import pandas as pd
            data = pd.DataFrame({"name": ["甲", "乙", "丙"], "score": [88, 95, 76]})
            # loc[行条件, 列标签] 按标签选择；这里的行条件会保留 score >= 80 的行，列列表只保留 name 和 score。
            # 返回值是 DataFrame，因为我们选择了多列；如果只写 data.loc[条件, "name"]，结果会是 Series。
            print(data.loc[data["score"] >= 80, ["name", "score"]].to_markdown(index=False))
            # iloc[行位置, 列位置] 按整数位置选择；:2 表示第 0、1 行，: 表示保留所有列。
            # iloc 的切片终点不包含 2，返回仍是 DataFrame，因为这里保留了二维表结构。
            print(data.iloc[:2, :].to_markdown(index=False))
        ''', "选择销售额大于 1000 的订单编号、城市和销售额。"),
        lesson("04_filter_query", "条件筛选与 query", "组合多个条件，并处理字符串和集合成员判断。", "多个 Series 条件用 &/|/~|isin 判断是否属于集合|query 可让复杂筛选更接近表达式", '''
            import pandas as pd
            data = pd.DataFrame({"city": ["上海", "北京", "上海"], "amount": [500, 1200, 1800]})
            # 先把条件拆开：每个比较表达式都会生成一列 True/False，便于单独检查。
            is_shanghai = data["city"] == "上海"
            is_expensive = data["amount"] >= 1000
            # & 表示逐行“并且”；两侧条件必须分别加括号，不能写 Python 的 and。
            selected_and = data[is_shanghai & is_expensive]
            print(selected_and.to_markdown(index=False))
            # | 表示逐行“或者”；~ 表示逐行取反，可以组合出“上海或金额达标”“不是上海”等条件。
            selected_or = data[(data["city"] == "上海") | (data["amount"] >= 1000)]
            selected_not = data[~(data["city"] == "上海")]
            print(selected_or.to_markdown(index=False))
            print(selected_not.to_markdown(index=False))
            # isin(values) 判断每行是否属于 values 列表，适合“城市在多个候选值中”的场景。
            selected_cities = data[data["city"].isin(["上海", "北京"])]
            print(selected_cities.to_markdown(index=False))
            # between(left, right, inclusive=...) 判断区间；inclusive="both" 表示包含两端。
            selected_range = data[data["amount"].between(500, 1500, inclusive="both")]
            print(selected_range.to_markdown(index=False))
            # query 接收字符串条件，列名可以直接写在字符串中；适合条件较长时提高可读性。
            selected_query = data.query("city == '上海' and amount >= 1000")
            print(selected_query.to_markdown(index=False))
        ''', "筛选指定城市中销售额位于某一区间的订单。"),
        lesson("05_modify_assign", "新增、修改与删除列", "以显式赋值或 assign 构造派生字段，并正确删除数据。", "向新列名赋值可新增列|loc 可条件更新|drop 默认返回新对象，inplace 并非总是更优", '''
            import pandas as pd
            data = pd.DataFrame({"price": [10, 20], "quantity": [3, 2]})
            # 用列名赋值会新增 amount；右侧是逐行相乘得到的 Series，长度与 data 行数一致。
            data["amount"] = data["price"] * data["quantity"]
            # loc[行条件, 列名] 只给满足条件的行写入 level，其余行暂时保持缺失。
            data.loc[data["amount"] >= 40, "level"] = "高"
            # fillna(value) 用 value 填补缺失等级，返回新 Series，需要重新赋回原列。
            data["level"] = data["level"].fillna("普通")
            print(data.to_markdown(index=False))
        ''', "根据销售额新增等级列，再删除一个不需要的临时列。"),
        lesson("06_types_missing", "类型转换与缺失值", "识别空值、选择删除或填补策略，并使用稳健转换。", "isna 识别缺失|to_numeric/to_datetime 支持 errors 参数|填补方法应符合字段的业务意义", '''
            import pandas as pd
            data = pd.DataFrame({"age": ["18", "错误", None], "score": [90, None, 80]})
            # to_numeric 的 errors="coerce" 会把无法转换的文本变成 NaN，而不是让程序直接报错。
            data["age"] = pd.to_numeric(data["age"], errors="coerce")
            # median() 求中位数；fillna(中位数) 用统计值补齐 score 的缺失项。
            data["score"] = data["score"].fillna(data["score"].median())
            print(data.to_markdown(index=False))
            print(data.isna().sum())
        ''', "把混合格式金额转为数值，并处理转换产生的缺失值。"),
        lesson("07_duplicates_strings", "重复值与字符串清洗", "统一文本格式并根据业务主键识别重复记录。", "duplicated 标记重复|drop_duplicates 可指定 subset 和保留策略|str 访问器向量化处理文本", '''
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
        ''', "清理商品类别的空格和大小写后再统计唯一类别。"),
        lesson("08_datetime", "日期时间处理", "解析日期、提取组成部分、计算时间差并按时间索引。", "to_datetime 统一解析|dt 访问器提取年月日|时间差产生 Timedelta", '''
            import pandas as pd
            data = pd.DataFrame({"date": ["2026-01-01", "2026-02-15"]})
            # to_datetime 把字符串解析为日期时间，返回可使用 dt 访问器的 Series。
            data["date"] = pd.to_datetime(data["date"])
            # dt.to_period("M") 把日期转换为月份周期，便于按月统计。
            data["month"] = data["date"].dt.to_period("M")
            # 两个日期相减得到 Timedelta，再用 dt.days 取出天数整数。
            data["days_from_start"] = (data["date"] - data["date"].min()).dt.days
            print(data.to_markdown(index=False))
        ''', "解析订单日期，统计每月订单数量。"),
        lesson("09_sort_groupby", "排序、分组与聚合", "使用 split-apply-combine 思路计算分组统计。", "sort_values 可多列多方向排序|groupby 先分组再计算|agg 可一次生成多个指标", '''
            import pandas as pd
            data = pd.DataFrame({"city": ["上海", "北京", "上海"], "amount": [100, 200, 300]})
            # groupby("city") 按城市分组；as_index=False 让 city 继续作为普通列保留。
            summary = data.groupby("city", as_index=False).agg(
                # agg 中每个命名参数定义一个输出列：原列 amount 使用 size/sum/mean 计算不同指标。
                orders=("amount", "size"),
                total=("amount", "sum"),
                average=("amount", "mean"),
            )
            print(summary.sort_values("total", ascending=False).to_markdown(index=False))
        ''', "按商品类别统计订单数、总销售额和平均销售额。"),
        lesson("10_merge_concat", "merge、join 与 concat", "根据键横向关联表格或沿轴拼接同构数据。", "merge 类似数据库连接|连接前检查键是否唯一|concat 适合按行或按列堆叠", '''
            import pandas as pd
            orders = pd.DataFrame({"customer_id": [1, 2], "amount": [100, 200]})
            customers = pd.DataFrame({"customer_id": [1, 2], "name": ["甲", "乙"]})
            # merge 按 customer_id 连接两张表；how="left" 保留全部订单，validate 检查连接关系。
            print(orders.merge(customers, on="customer_id", how="left", validate="many_to_one").to_markdown(index=False))
            # concat 沿行方向拼接表；ignore_index=True 重新生成连续索引。
            print(pd.concat([orders, orders], ignore_index=True).to_markdown(index=False))
        ''', "连接订单表和商品表，并检查未匹配的商品编号。"),
        lesson("11_pivot_crosstab", "透视表与交叉表", "把长表重塑为汇总矩阵，比较分类变量关系。", "pivot 要求组合键唯一|pivot_table 可聚合重复组合|crosstab 适合频数或比例交叉统计", '''
            import pandas as pd
            data = pd.DataFrame({"city": ["上海", "上海", "北京"], "product": ["A", "B", "A"], "amount": [100, 200, 150]})
            # pivot_table 按 index/columns 重塑表格，values 是要汇总的列，aggfunc="sum" 指定求和。
            print(pd.pivot_table(data, values="amount", index="city", columns="product", aggfunc="sum", fill_value=0).to_markdown())
            # crosstab 统计两个分类字段的频数，这里回答“每个城市有多少种商品记录”。
            print(pd.crosstab(data["city"], data["product"]).to_markdown())
        ''', "制作月份×商品类别的销售额透视表。"),
        lesson("12_apply_transform", "map、apply 与 transform", "根据输入输出形状选择自定义转换方式，优先使用向量化操作。", "Series.map 逐元素映射|DataFrame.apply 按行或列调用|groupby.transform 返回与原数据等长结果", '''
            import pandas as pd
            data = pd.DataFrame({"group": ["A", "A", "B"], "score": [80, 100, 70]})
            # transform("mean") 计算组均值，但返回长度与原表相同，所以可以安全赋回新列。
            data["group_mean"] = data.groupby("group")["score"].transform("mean")
            # 逐行相减得到每条记录相对本组均值的差异。
            data["difference"] = data["score"] - data["group_mean"]
            print(data.to_markdown(index=False))
        ''', "计算每笔订单金额占所在城市总销售额的比例。"),
        lesson("13_outliers_export", "异常值处理与导出", "用 IQR 等规则标记异常值，并保存清洗结果而不覆盖原始数据。", "异常不等于错误，应结合业务判断|IQR 上下界是常见稳健规则|to_csv/to_excel 导出时明确索引和编码", '''
            import pandas as pd
            values = pd.Series([10, 11, 12, 13, 100])
            # quantile([0.25, 0.75]) 一次取得 Q1、Q3；IQR 是两者之差。
            q1, q3 = values.quantile([0.25, 0.75])
            iqr = q3 - q1
            # 布尔条件标记异常值；这里先标记，不直接删除，方便后续业务复核。
            mask = (values < q1 - 1.5 * iqr) | (values > q3 + 1.5 * iqr)
            result = pd.DataFrame({"value": values, "is_outlier": mask})
            print(result.to_markdown(index=False))
        ''', "标记销售额异常订单，并把结果导出到 outputs。"),
    ],
    "03_matplotlib": [
        lesson("01_figure_axes", "Figure 与 Axes", "使用面向对象接口创建画布、坐标系和多子图。", "Figure 是整张画布|Axes 是具体绘图区|subplots 同时创建二者", '''
            import matplotlib.pyplot as plt
            fig, axes = plt.subplots(1, 2, figsize=(9, 3))
            axes[0].plot([1, 2, 3], [2, 4, 3])
            axes[1].bar(["A", "B"], [5, 8])
            fig.tight_layout()
            plt.show()
        ''', "创建 2×2 子图并为每个坐标系设置标题。"),
        lesson("02_line_scatter", "折线图与散点图", "分别表达随序列变化的趋势和两个数值变量的关系。", "折线图强调顺序和趋势|散点图强调分布、相关和异常点|不要把无顺序类别强行连线", '''
            import matplotlib.pyplot as plt
            x = [1, 2, 3, 4]
            y = [2, 5, 4, 8]
            fig, axes = plt.subplots(1, 2)
            axes[0].plot(x, y, marker="o")
            axes[1].scatter(x, y, s=60, alpha=0.7)
            plt.show()
        ''', "用折线图绘制月销售趋势，用散点图绘制价格和销量关系。"),
        lesson("03_bar", "柱状图与堆积柱状图", "比较类别大小，并通过排序和基线减少误导。", "柱长代表数值，通常从零开始|水平柱图适合长标签|堆积图适合展示总量和组成", '''
            import matplotlib.pyplot as plt
            categories = ["A", "B", "C"]
            online = [10, 15, 12]
            offline = [5, 6, 8]
            plt.bar(categories, online, label="线上")
            plt.bar(categories, offline, bottom=online, label="线下")
            plt.legend()
            plt.show()
        ''', "按销售额排序后绘制水平柱状图，并添加数值标签。"),
        lesson("04_hist_box", "直方图与箱线图", "观察连续变量的分布形状、离散程度和潜在异常值。", "直方图对结果受分箱数影响|箱线图展示四分位数和离群点|比较分组分布时保持同一尺度", '''
            import matplotlib.pyplot as plt
            values = [55, 62, 68, 70, 72, 75, 80, 82, 90, 100]
            fig, axes = plt.subplots(1, 2)
            axes[0].hist(values, bins=5, edgecolor="black")
            axes[1].boxplot(values)
            plt.show()
        ''', "用不同 bins 绘制同一数据的直方图并比较。"),
        lesson("05_labels_legend", "标题、坐标轴、图例与网格", "补齐读者理解图表所需的上下文信息。", "标题回答图表讲什么|坐标轴注明变量和单位|图例只在存在多个系列时使用", '''
            import matplotlib.pyplot as plt
            plt.plot([1, 2, 3], [100, 130, 125], label="销售额", marker="o")
            plt.title("第一季度销售趋势")
            plt.xlabel("月份")
            plt.ylabel("销售额（万元）")
            plt.grid(alpha=0.3)
            plt.legend()
            plt.show()
        ''', "为一张缺少说明的图补齐标题、单位、图例和数据来源注释。"),
        lesson("06_style_annotation", "颜色、样式与标注", "使用有限视觉编码突出重点，不让装饰压过数据。", "颜色应有语义且兼顾可辨识性|alpha 控制透明度|annotate 可解释关键点", '''
            import matplotlib.pyplot as plt
            x, y = [1, 2, 3, 4], [10, 14, 13, 20]
            plt.plot(x, y, color="#2f6f9f", linewidth=2)
            plt.annotate("峰值", xy=(4, 20), xytext=(3.2, 18), arrowprops={"arrowstyle": "->"})
            plt.show()
        ''', "突出折线图的最大值和最小值并添加箭头说明。"),
        lesson("07_chinese_fonts", "中文字体与负号", "按系统字体情况设置中文显示，并解决负号方块问题。", "字体是否可用取决于系统|rcParams 可全局设置|发布环境也要安装所选字体", '''
            import matplotlib.pyplot as plt
            plt.rcParams["font.sans-serif"] = ["Arial Unicode MS", "SimHei", "DejaVu Sans"]
            plt.rcParams["axes.unicode_minus"] = False
            plt.plot([1, 2, 3], [-1, 2, 3])
            plt.title("中文标题与负数")
            plt.show()
        ''', "检查本机可用中文字体并保存一张中文测试图。"),
        lesson("08_dates_save", "日期坐标与保存图片", "格式化时间轴并以合适分辨率和边界导出图表。", "日期轴应控制刻度密度|autofmt_xdate 可旋转日期标签|savefig 应在 show 前调用", '''
            from datetime import datetime
            import matplotlib.pyplot as plt
            dates = [datetime(2026, m, 1) for m in range(1, 5)]
            fig, ax = plt.subplots()
            ax.plot(dates, [10, 15, 13, 20], marker="o")
            fig.autofmt_xdate()
            fig.savefig("matplotlib_example.png", dpi=150, bbox_inches="tight")
            print("已保存 matplotlib_example.png")
        ''', "绘制六个月趋势并导出 PNG 和 SVG 两种格式。"),
    ],
    "04_seaborn": [
        lesson("01_theme_palette", "主题与调色板", "用统一主题和语义化颜色建立清晰的视觉风格。", "set_theme 设置整体风格|color_palette 选择离散颜色|连续变量使用连续色带", '''
            import matplotlib.pyplot as plt
            import seaborn as sns
            sns.set_theme(style="whitegrid", palette="deep")
            sns.lineplot(x=[1, 2, 3], y=[2, 5, 4], marker="o")
            plt.show()
        ''', "比较 whitegrid、darkgrid 和 ticks 三种主题。"),
        lesson("02_relational", "关系图：scatterplot 与 lineplot", "使用 hue、style、size 编码更多变量并观察关系。", "scatterplot 展示观测点关系|lineplot 默认可能展示估计与误差|语义通道不宜同时使用过多", '''
            import matplotlib.pyplot as plt
            import pandas as pd
            import seaborn as sns
            tips = pd.DataFrame({
                "total_bill": [80, 120, 160, 200, 240, 280],
                "tip": [8, 14, 18, 25, 24, 35],
                "time": ["Lunch", "Lunch", "Dinner", "Dinner", "Dinner", "Lunch"],
                "sex": ["女", "男", "女", "男", "女", "男"],
            })
            sns.scatterplot(data=tips, x="total_bill", y="tip", hue="time", style="sex", alpha=0.75)
            plt.show()
        ''', "使用本地 sales.csv 绘制销量与销售额散点图并按城市着色。"),
        lesson("03_categorical", "分类图：bar、count 与 point", "比较类别频数或聚合统计，并区分原始值和估计值。", "countplot 统计行数|barplot 默认展示聚合估计|pointplot 强调类别间变化模式", '''
            import matplotlib.pyplot as plt
            import pandas as pd
            import seaborn as sns
            data = pd.DataFrame({"city": ["上海", "北京", "上海", "深圳"], "amount": [100, 200, 300, 180]})
            sns.barplot(data=data, x="city", y="amount", errorbar=None)
            plt.show()
        ''', "分别用 countplot 和 barplot 回答订单数、平均销售额两个问题。"),
        lesson("04_distribution", "分布图：histplot 与 kdeplot", "观察单变量或分组分布，并谨慎解释平滑密度。", "histplot 展示分箱计数或密度|kdeplot 是平滑估计且可能超出实际范围|hue 可比较分组分布", '''
            import matplotlib.pyplot as plt
            import numpy as np
            import seaborn as sns
            rng = np.random.default_rng(42)
            values = rng.normal(100, 15, 500)
            sns.histplot(values, bins=20, kde=True)
            plt.show()
        ''', "比较两个城市订单金额的直方图和密度曲线。"),
        lesson("05_box_violin", "箱线图与小提琴图", "比较多个类别的分布、离散程度与异常值。", "boxplot 概括中位数和四分位数|violinplot 增加密度形状|样本很小时小提琴形状不稳定", '''
            import matplotlib.pyplot as plt
            import pandas as pd
            import seaborn as sns
            tips = pd.DataFrame({
                "day": ["周一", "周一", "周二", "周二", "周三", "周三"],
                "total_bill": [80, 150, 90, 210, 120, 260],
            })
            sns.violinplot(data=tips, x="day", y="total_bill", inner="quartile")
            plt.show()
        ''', "按商品类别比较销售额分布，并同时尝试箱线图和小提琴图。"),
        lesson("06_heatmap", "热力图", "用颜色矩阵展示相关系数、交叉表或二维汇总值。", "输入通常是二维矩阵|annot 显示数值|相关不等于因果，冗余半矩阵可使用 mask", '''
            import matplotlib.pyplot as plt
            import pandas as pd
            import seaborn as sns
            data = pd.DataFrame({"price": [10, 12, 20, 22], "quantity": [8, 7, 4, 3], "amount": [80, 84, 80, 66]})
            sns.heatmap(data.corr(numeric_only=True), annot=True, cmap="coolwarm", center=0)
            plt.show()
        ''', "计算数值字段相关矩阵并绘制带数值标注的热力图。"),
        lesson("07_pair_joint", "pairplot 与 jointplot", "快速浏览多变量两两关系或深入查看一对变量的联合分布。", "pairplot 适合少量数值列|变量过多会生成大量子图|jointplot 同时显示关系和边缘分布", '''
            import matplotlib.pyplot as plt
            import pandas as pd
            import seaborn as sns
            iris = pd.DataFrame({
                "sepal_length": [5.1, 4.9, 6.2, 5.9, 6.5, 6.3],
                "sepal_width": [3.5, 3.0, 3.4, 3.0, 3.0, 2.5],
                "petal_length": [1.4, 1.4, 5.4, 5.1, 5.8, 5.0],
                "species": ["setosa", "setosa", "virginica", "virginica", "virginica", "virginica"],
            })
            sns.pairplot(iris, hue="species", corner=True)
            plt.show()
        ''', "选取三个最重要数值字段绘制 pairplot，避免无意义的全字段组合。"),
        lesson("08_faceting", "分面绘图", "按类别拆成共享尺度的小图，比较不同子群体模式。", "FacetGrid 控制分面布局|relplot/catplot/displot 是 figure-level 接口|共享坐标尺度便于比较", '''
            import matplotlib.pyplot as plt
            import pandas as pd
            import seaborn as sns
            tips = pd.DataFrame({
                "total_bill": [80, 120, 160, 200, 240, 280],
                "tip": [8, 14, 18, 25, 24, 35],
                "time": ["午餐", "午餐", "晚餐", "晚餐", "晚餐", "午餐"],
                "smoker": ["否", "是", "否", "是", "否", "是"],
            })
            sns.relplot(data=tips, x="total_bill", y="tip", col="time", hue="smoker")
            plt.show()
        ''', "按城市分面绘制各商品销量和销售额的关系。"),
    ],
    "05_data_analysis_workflow": [
        lesson("01_questions_quality", "定义问题与检查数据质量", "先明确分析对象、指标、粒度和时间范围，再评估数据能否回答问题。", "问题应可验证|一行代表什么决定聚合方式|检查完整性、一致性、唯一性和有效性", '''
            questions = [
                "哪个城市销售额最高？",
                "各月销售趋势如何？",
                "哪些订单金额可能异常？",
            ]
            for index, question in enumerate(questions, 1):
                print(index, question)
        ''', "为学生成绩数据提出三个明确、可计算的分析问题。"),
        lesson("02_clean_transform", "清洗与转换", "保留原始数据，记录清洗规则并构造可解释的分析字段。", "复制或另存清洗结果|转换前后记录行数和缺失量|派生字段要写清单位和计算公式", '''
            from pathlib import Path
            import pandas as pd
            path = Path(__file__).resolve().parents[2] / "datasets" / "sales.csv"
            data = pd.read_csv(path)
            data["date"] = pd.to_datetime(data["date"])
            data["amount"] = data["price"] * data["quantity"]
            data = data.drop_duplicates(subset="order_id")
            print(data.info())
        ''', "制定并执行一份包含类型、缺失、重复和异常值的清洗清单。"),
        lesson("03_eda", "探索性数据分析", "从单变量、分组和变量关系逐步寻找模式与异常。", "先总体后分组|同时观察中心、离散和分布|探索结论需要后续验证", '''
            from pathlib import Path
            import pandas as pd
            data = pd.read_csv(Path(__file__).resolve().parents[2] / "datasets" / "sales.csv")
            data["amount"] = data["price"] * data["quantity"]
            print(data["amount"].describe())
            print(data.groupby("city")["amount"].agg(["count", "sum", "mean"]))
        ''', "从销售数据中找出三个值得进一步调查的现象。"),
        lesson("04_visual_story", "可视化与结论表达", "让每张图回答一个问题，并区分数据事实、解释和建议。", "图表类型由问题和变量类型决定|标题可直接表达主要发现|结论应注明范围、限制和不确定性", '''
            finding = "上海样本中的总销售额最高"
            evidence = "按城市汇总订单金额后比较"
            limitation = "样本量较小，不能代表长期趋势"
            print("发现：", finding)
            print("依据：", evidence)
            print("限制：", limitation)
        ''', "为一张月销售趋势图撰写发现、证据、限制和建议。"),
        lesson("05_export_reproducible", "导出与可复现分析", "固定输入、依赖、随机种子和输出位置，让别人可以重复分析。", "requirements 记录依赖|随机过程固定种子|结果文件不覆盖原始数据，并记录生成时间", '''
            from pathlib import Path
            output_dir = Path(__file__).resolve().parents[2] / "outputs"
            output_dir.mkdir(exist_ok=True)
            print("所有清洗表格、图表和摘要统一写入：", output_dir)
        ''', "列出让你的分析在另一台电脑上可复现所需的全部材料。"),
    ],
}


PANDAS_CHAPTER_CONTEXT = {
    "01_series_dataframe": (
        "教务处收到一张包含姓名、班级和多门成绩的表格，老师既要看单独一列，也要同时筛选多列记录。",
        "列表需要手工维护列名和对应关系；Series 和 DataFrame 能让一列或整张表带着标签参与选择、计算和统计。",
    ),
    "02_read_inspect": (
        "销售数据来自 CSV 或 Excel 文件，分析师必须先确认行数、字段、类型和缺失情况。",
        "外部文件不会自动变成可靠的数据表；读取和检查是发现格式错误、类型误判与异常值的第一道关。",
    ),
    "03_select_loc_iloc": (
        "班主任只想查看二班学生的姓名和成绩，教务员则要取原表前五行。",
        "真实分析很少需要整张表，按标签、位置和条件选择可以减少误取和误改数据。",
    ),
    "04_filter_query": (
        "运营人员要找出指定城市、金额区间和商品类别的订单。",
        "业务条件必须被准确翻译成布尔条件；括号、isin 和 query 是可靠筛选的基础。",
    ),
    "05_modify_assign": (
        "订单表只有单价和数量，课堂需要增加销售额、折扣后金额和订单等级。",
        "分析要根据业务公式构造派生字段，同时保留原始字段以便回溯。",
    ),
    "06_types_missing": (
        "报名表中的年龄有数字、未知和空白，成绩也存在缺失。",
        "类型错误和缺失值会直接影响排序、平均值和图表，必须先识别再决定转换、删除或填补。",
    ),
    "07_duplicates_strings": (
        "客户名单中存在多余空格、大小写差异和重复导入的客户。",
        "格式不统一会让人数和订单量被重复计算；标准化文本后才能依据业务主键去重。",
    ),
    "08_datetime": (
        "销售趋势需要按月汇总，配送分析还要计算日期间隔。",
        "日期字符串不能可靠地排序、加减和分组；日期类型让时间真正成为可计算的数据。",
    ),
    "09_sort_groupby": (
        "管理层希望看到各城市订单数、总销售额、平均金额和排名。",
        "排序回答谁最高，groupby 和聚合回答每个群体怎样，这是明细表变成管理指标的核心。",
    ),
    "10_merge_concat": (
        "订单表只有客户编号，客户姓名在另一张表；不同月份订单还要上下合并。",
        "真实数据分散在多张表，必须区分按键关联的 merge 和沿轴拼接的 concat。",
    ),
    "11_pivot_crosstab": (
        "汇报表要求行是城市、列是商品类别、单元格是销售额。",
        "长表适合计算，透视表适合汇报；重塑能让复杂分组结果变成一眼可读的矩阵。",
    ),
    "12_apply_transform": (
        "老师要把每个学生与本班平均分比较，并把班级统计结果对齐回每一行。",
        "自定义处理有不同粒度，map、apply 和 transform 的输入输出形状不同，选错会产生错位结果。",
    ),
    "13_outliers_export": (
        "销售表出现一笔远高于其他订单的金额，分析师要标记、调查并交付清洗结果。",
        "异常值可能是真实大客户，也可能是录入错误；IQR 用于标记，导出用于交付，二者都不能替代业务判断。",
    ),
}

PANDAS_CASE_STEPS = {
    "01_series_dataframe": [
        "案例任务：教务处要找出 Python 成绩不低于 85 分的学生，并计算全班平均分。",
        "第 1 步：把一列 Python 成绩表示成 Series，把姓名、班级和多门成绩表示成 DataFrame。",
        "第 2 步：观察 type、index、columns 和 shape，确认“单列”和“整张表”的区别。",
        "第 3 步：从 DataFrame 选择 python 列，计算平均分，再用条件选择符合要求的行。",
        "第 4 步：打印结果并用人工计算抽查一行，验证数据没有错位。",
    ],
    "02_read_inspect": [
        "案例任务：接手 sales.csv，向主管汇报这份数据能否用于销售分析。",
        "第 1 步：使用 read_csv 把文件加载为 DataFrame，先不做任何清洗。",
        "第 2 步：用 head、shape、columns 和 info 检查结构，再用 isna 统计空值。",
        "第 3 步：用 describe 查看数值字段范围，判断金额、数量是否被正确识别。",
        "第 4 步：把发现的问题写成检查清单，决定下一节要清洗什么。",
    ],
    "03_select_loc_iloc": [
        "案例任务：从订单明细中找出上海订单，并只交付编号、商品和金额三列。",
        "第 1 步：先明确需要的列名和筛选条件，避免先打印整张大表。",
        "第 2 步：使用 loc 按标签和条件选择，观察返回结果的行列数。",
        "第 3 步：使用 iloc 取前两行，比较位置选择和标签选择的差异。",
        "第 4 步：检查选择结果是否保留原索引，并验证没有误取列。",
    ],
    "04_filter_query": [
        "案例任务：运营人员要找出上海或北京、数量至少 2 且单价大于 100 的订单。",
        "第 1 步：把自然语言拆成三个独立的布尔条件。",
        "第 2 步：分别打印每个条件，确认每一行得到 True 或 False。",
        "第 3 步：使用括号和位运算符组合条件，再与 query 写法对照。",
        "第 4 步：检查结果为空和条件边界值时的表现。",
    ],
    "05_modify_assign": [
        "案例任务：订单只有 price 和 quantity，需要增加 amount、折扣金额和等级。",
        "第 1 步：先写出业务公式，明确金额单位和折扣口径。",
        "第 2 步：通过新列赋值构造 amount，不修改原始 price 和 quantity。",
        "第 3 步：用 loc 按条件填写等级，观察缺省行如何处理。",
        "第 4 步：抽查一笔订单，用手算结果验证派生列。",
    ],
    "06_types_missing": [
        "案例任务：报名表的年龄包含数字、未知和空白，成绩也有缺失。",
        "第 1 步：先查看 dtype 和 isna 统计，不要把缺失直接当成 0。",
        "第 2 步：用 to_numeric 的 errors 参数把非法文本转为可识别的缺失。",
        "第 3 步：根据业务决定删除、保留或用中位数填补。",
        "第 4 步：比较处理前后的行数、缺失量和统计结果。",
    ],
    "07_duplicates_strings": [
        "案例任务：客户名单中邮箱大小写不同、姓名带空格，还有重复导入记录。",
        "第 1 步：先确定真正代表客户身份的业务主键，例如 email。",
        "第 2 步：使用 str 访问器统一空格、大小写和文本格式。",
        "第 3 步：用 duplicated 找出重复记录，再决定保留哪一条。",
        "第 4 步：比较清洗前后的客户数量，并保留重复记录供复核。",
    ],
    "08_datetime": [
        "案例任务：统计 sales.csv 每月订单数和销售额。",
        "第 1 步：把 date 从字符串解析为 datetime，并检查无效日期。",
        "第 2 步：用 dt 访问器提取月份或生成 Period。",
        "第 3 步：按 month 分组并聚合订单数、销售额。",
        "第 4 步：按时间顺序排序，确认月份没有按字符串字典序排列。",
    ],
    "09_sort_groupby": [
        "案例任务：制作各城市销售排名，包含订单数、总额、平均额和最大单笔。",
        "第 1 步：先明确分组字段和每个指标的统计口径。",
        "第 2 步：groupby 后使用 agg 一次计算多个指标。",
        "第 3 步：按 total 降序排序，给结果增加排名或序号。",
        "第 4 步：同时报告样本量，避免只看平均数造成误判。",
    ],
    "10_merge_concat": [
        "案例任务：把订单表的 customer_id 与客户表匹配，并合并两个月订单。",
        "第 1 步：先检查两张表连接键的类型和唯一性。",
        "第 2 步：使用 left merge 保留全部订单，再检查未匹配客户。",
        "第 3 步：使用 concat 沿行拼接结构相同的月份表。",
        "第 4 步：比较连接前后行数，排查意外重复和丢失。",
    ],
    "11_pivot_crosstab": [
        "案例任务：制作城市×商品类别销售额汇报矩阵。",
        "第 1 步：确认行变量、列变量、数值变量和聚合方式。",
        "第 2 步：使用 pivot_table 把长表重塑成矩阵。",
        "第 3 步：用 crosstab 另算订单数量，比较金额和数量的区别。",
        "第 4 步：检查空白组合是没有数据还是被填成了 0。",
    ],
    "12_apply_transform": [
        "案例任务：计算每笔订单占所在城市总销售额的比例。",
        "第 1 步：先按城市计算总额，再思考如何把城市结果对齐回每一行。",
        "第 2 步：用 transform 生成与原表等长的城市总额列。",
        "第 3 步：相除得到比例，并按城市检查比例之和。",
        "第 4 步：说明为什么这里不能随意用 apply 替代 transform。",
    ],
    "13_outliers_export": [
        "案例任务：标记异常金额，调查原因后把结果交付给同事。",
        "第 1 步：先计算金额的 Q1、Q3 和 IQR，不急着删除记录。",
        "第 2 步：生成 is_outlier 布尔列，保留原金额方便复核。",
        "第 3 步：查看异常订单的商品、城市和日期，区分错误与真实大单。",
        "第 4 步：把带标记的结果导出到 outputs，原始 datasets 文件不动。",
    ],
}

PANDAS_CASE_DATA = {
    "01_series_dataframe": """| name | class | math | python |
|---|---|---:|---:|
| 小林 | 一班 | 92 | 95 |
| 小周 | 一班 | 76 | 84 |
| 小陈 | 二班 | 85 | 90 |
| 小李 | 二班 | 68 | 75 |""",
    "02_read_inspect": "本节使用 datasets/sales.csv：10 条订单记录，字段包括 order_id、date、city、product、category、price、quantity；金额需要由 price × quantity 得到。",
    "03_select_loc_iloc": """| order_id | city | product | amount |
|---|---|---|---:|
| S001 | 上海 | 键盘 | 798 |
| S002 | 北京 | 鼠标 | 1200 |
| S003 | 上海 | 显示器 | 1800 |
| S004 | 深圳 | 耳机 | 650 |""",
    "04_filter_query": "本节使用订单表：city 有上海、北京、深圳，quantity 有 1、2、3，price 有 129、399、899 等数值；目标是组合城市、数量和价格条件。",
    "05_modify_assign": "本节使用只含 order_id、price、quantity 的订单表；amount=price×quantity，discount_amount=amount×0.9，level 根据金额划分。",
    "06_types_missing": "本节准备 age=['18','未知',None]、score=[90,None,80]；其中字符串、非法文本和缺失值混在同一列中。",
    "07_duplicates_strings": "本节准备 name=[' Alice ','alice','Bob']、email=['A@X.COM','a@x.com','b@x.com']；前两行代表同一邮箱的重复记录。",
    "08_datetime": "本节使用 date=['2026-01-03','2026-02-14','2026-02-20']，目标是按月统计订单数量，并计算日期间隔。",
    "09_sort_groupby": "本节使用 city=['上海','北京','上海']、amount=[100,200,300]；目标是得到每个城市的订单数、总额、平均额和最大额。",
    "10_merge_concat": "本节有两张表：orders(customer_id, amount) 与 customers(customer_id, name)，另有两个月的同结构订单表需要上下拼接。",
    "11_pivot_crosstab": "本节使用 city、product、amount 三列的长表；同一城市和商品可能出现多行，需要汇总为城市×商品矩阵。",
    "12_apply_transform": "本节使用 group=['A','A','B']、score=[80,100,70]；目标是把每组平均分对齐回每一行并计算差值。",
    "13_outliers_export": "本节使用金额 [10,11,12,13,100]；最后一个值明显偏高，但在删除前必须保留订单信息并调查原因。",
}

PANDAS_STEP_WHY = {
    "01_series_dataframe": [
        "先明确一列和多列的形状，因为后续选择、平均和筛选依赖对象结构；选错对象会让代码和结果都不清晰。",
        "先观察 type、index、columns、shape，是为了验证我们的数据建模是否正确，而不是盲目相信打印结果。",
        "选择 Series 后才能直接计算一列平均分；用布尔条件筛选 DataFrame，是因为最终要保留学生的完整信息。",
        "最后验证是为了排除索引错位、列名错误和人工计算错误，确保结果能回答教务处问题。",
    ],
    "02_read_inspect": [
        "先读取文件，是因为分析对象还在磁盘上，内存中没有 DataFrame 就无法使用 Pandas 的检查能力。",
        "先看样例和形状，是为了知道一行代表什么、数据量有多大，避免在错误粒度上分析。",
        "检查类型和缺失，是因为字符串金额不能直接可靠求和，缺失也会改变统计结果。",
        "把发现写成清单，是为了让清洗有依据、有顺序，而不是看到一个问题就随意修改。",
    ],
    "03_select_loc_iloc": [
        "先列出需要的字段和条件，是为了把业务需求翻译成最小结果集，减少误取和内存浪费。",
        "用 loc 是因为我们知道列名和业务条件，标签选择比位置猜测更稳定、更容易复查。",
        "用 iloc 做对照，是为了理解按位置选择适合快速抽样，但不能代替有业务含义的标签选择。",
        "检查索引和形状，是为了确认没有丢行、错列或把 Series 误当成 DataFrame。",
    ],
    "04_filter_query": [
        "先拆成独立条件，是为了让每个条件都能单独检查，避免一条长表达式隐藏错误。",
        "先打印布尔掩码，是为了看到每一行为什么通过或不通过，而不是只接受最终名单。",
        "组合条件时使用 Pandas 的位运算，是因为每个条件其实是一整列 True/False，而不是一个普通布尔值。",
        "检查空结果和边界值，是为了区分“确实没有记录”和“条件写错”两种情况。",
    ],
    "05_modify_assign": [
        "先写公式，是为了让派生字段有明确业务口径，避免把代码结果误当成正确结果。",
        "新建 amount 而不是覆盖 price，是为了保留原始事实，方便复算和审计。",
        "用 loc 条件赋等级，是因为条件只适用于部分行，显式定位可以避免链式赋值问题。",
        "抽查一行，是为了把程序计算和人工公式对应起来，尽早发现单位或折扣比例错误。",
    ],
    "06_types_missing": [
        "先查看 dtype 和缺失，是因为处理策略取决于问题是类型错误、真正缺失还是业务上的未知。",
        "用 errors=coerce，是为了把无法转换的文本统一标记为 NaN，后续能用同一套缺失逻辑处理。",
        "删除或填补必须由业务决定，因为填补均值可能改变分布，删除也可能丢失重要样本。",
        "比较前后统计，是为了证明清洗确实改善了数据，而不是悄悄改变了结论。",
    ],
    "07_duplicates_strings": [
        "先确定业务主键，是因为“重复”不是两行长得像，而是代表了同一个业务实体。",
        "先统一文本，是为了让同一个邮箱在大小写和空格不同的情况下仍能被识别为同一值。",
        "先标记再删除，是为了保留复核证据，并能向业务人员解释为什么只保留一行。",
        "比较数量，是为了量化清洗影响，避免不知不觉删除大量有效客户。",
    ],
    "08_datetime": [
        "先统一日期类型，是因为字符串排序可能按字符顺序而不是时间顺序，日期加减也无法可靠进行。",
        "提取月份是为了把时间粒度转换为业务问题需要的月度粒度。",
        "按月聚合是因为管理层问的是趋势和总量，不是逐条日期文本。",
        "最后排序和检查，是为了防止月份被当作普通字符串导致 2026-10 排在 2026-2 前面。",
    ],
    "09_sort_groupby": [
        "先定义指标，是为了避免把订单数、金额总和和平均金额混成一个没有意义的数字。",
        "先分组再聚合，是因为每个城市需要独立计算，不能把全表结果复制给所有城市。",
        "再排序，是为了把汇总结果转换成管理层可以直接阅读的排名。",
        "报告样本量，是因为平均值相同但订单数差异很大时，业务解释完全不同。",
    ],
    "10_merge_concat": [
        "先检查键，是为了避免类型不同导致全部匹配失败，或键不唯一导致行数意外膨胀。",
        "使用 left merge，是因为订单是主表，任何订单都不应因缺少客户信息而消失。",
        "使用 concat，是因为月份表结构相同，需求是上下增加记录而不是按键匹配字段。",
        "比较连接前后行数，是为了用数量证据发现重复、丢失和未匹配记录。",
    ],
    "11_pivot_crosstab": [
        "先确定行、列、值和聚合方式，是因为透视表的每个单元格都必须有明确统计口径。",
        "使用 pivot_table，是因为同一城市和商品可能有多条记录，需要先聚合才能放进一个单元格。",
        "另算订单数，是为了提醒学生金额矩阵和数量矩阵回答的是不同问题。",
        "检查空白组合，是为了区分没有发生交易和被错误填充为零。",
    ],
    "12_apply_transform": [
        "先算每组总量，是因为每笔订单的比例分母取决于它所在的城市或组别。",
        "选择 transform，是因为它会返回与原数据等长的结果，能安全地逐行对齐。",
        "再相除得到比例，是因为每一步都可检查，出错时能定位分母还是分子。",
        "检查每组比例和，是为了验证对齐没有错位，并确认结果符合比例的数学性质。",
    ],
    "13_outliers_export": [
        "先计算 IQR，是因为需要一个相对稳健、可解释的标记规则，而不是凭肉眼删除。",
        "保留布尔标记，是为了同时保留原值和调查线索，异常不等于错误。",
        "查看相关字段，是为了结合商品、城市和日期判断业务原因。",
        "导出新文件，是为了交付结果同时保护原始数据，保证分析可回溯。",
    ],
}

PANDAS_ALTERNATIVES = {
    "01_series_dataframe": "也可以用 Python 列表、字典或 Excel 手工完成；但它们需要自己维护列名、筛选、对齐和统计。Series/DataFrame 的优势是标签对齐、向量化计算和后续清洗分析接口统一。",
    "02_read_inspect": "也可以用 csv 模块逐行读取或手工打开 Excel；但需要自己处理类型、缺失和汇总。Pandas 能一次得到结构检查、统计摘要和后续分析对象。",
    "03_select_loc_iloc": "也可以用 for 循环逐行判断或先转成列表；但代码更长、容易漏列。loc/iloc 的优势是表达清晰、批量操作和结果形状可预测。",
    "04_filter_query": "也可以用 for 循环和 if 拼出新列表；但难以组合复杂条件且丢失列标签。Pandas 掩码/query 能保留表结构并让条件可检查。",
    "05_modify_assign": "也可以逐行循环计算并 append 字典；但速度慢、代码冗长且容易改错原数据。列运算和 loc 是向量化、可审计的表达。",
    "06_types_missing": "也可以逐个值 try/except；但规则分散且难以统计影响。Pandas 的转换、NaN 和填补方法能批量处理并保留缺失语义。",
    "07_duplicates_strings": "也可以把每行转成集合后手工比较；但空格、大小写和业务主键很容易漏掉。str 访问器和 drop_duplicates 更稳定且可复现。",
    "08_datetime": "也可以切字符串的前 7 位得到月份；但遇到格式变化、无效日期和时区就会失败。datetime/dt 提供可靠的时间运算和时间粒度。",
    "09_sort_groupby": "也可以先把每个城市分成多个列表再循环统计；但指标增加后重复代码很多。groupby/agg 能统一定义多个指标并保持结果表结构。",
    "10_merge_concat": "也可以写嵌套循环查找客户或手工复制文件；但复杂度高且容易重复。merge/concat 使用明确连接语义，并可用 validate 检查关系。",
    "11_pivot_crosstab": "也可以手工创建二维字典；但要自己补齐组合、聚合和排序。pivot_table/crosstab 直接表达表格重塑意图，便于复核。",
    "12_apply_transform": "也可以循环计算每组平均数再逐行回填；但容易发生索引错位。transform 保持原长度，适合把组级指标安全返回明细表。",
    "13_outliers_export": "也可以凭经验写固定阈值或直接删除最大值；但不可迁移且可能误删真实大单。IQR 标记加业务复核更稳健，导出新文件更安全。",
}


def pandas_readme_for(item: Lesson, number: int) -> str:
    scene, why = PANDAS_CHAPTER_CONTEXT[item.slug]
    case_steps = PANDAS_CASE_STEPS[item.slug]
    step_whys = PANDAS_STEP_WHY[item.slug]
    case_data = PANDAS_CASE_DATA[item.slug]
    alternatives = PANDAS_ALTERNATIVES[item.slug]
    points = "\n".join(f"- {point}" for point in item.points)
    step_items = [step.split("：", 1)[-1] for step in case_steps[1:]]
    step_table = "\n".join(
        f"| {step_number} | {step} | {step_whys[step_number - 1]} |"
        for step_number, step in enumerate(step_items, 1)
    )
    if item.slug == "01_series_dataframe":
        concept = (
            "Series 是带索引标签的一维数据，适合表示一个字段，例如全班 Python 成绩；"
            "DataFrame 是带行索引和列名的二维表，适合表示多条完整记录。"
            "DataFrame 可以看作多个长度相同、按索引对齐的 Series 组成的表。"
        )
        without = (
            "不用 Pandas 时，可以用列表保存姓名、班级和成绩，再用 for 循环逐行判断、"
            "自己累加求平均。这样做并非错误，但列名、索引、筛选和统计都要手工维护。"
        )
    else:
        concept = f"{item.title} 的核心，是把原始表格中的信息转换成可检查、可复用的分析结果。{item.summary}"
        without = "不用 Pandas 时，可以使用 Python 列表、字典、csv 模块或手工表格逐步完成；这种方式适合极小数据，但字段一多就需要自己维护大量循环、对齐和检查逻辑。"
    return f"""# {number:02d}. {item.title}

> 所属课程：Python 数据分析  
> 所属章节：02_pandas

## 一、今天要学什么

本节要学习：{item.title}。

## 二、先从问题源头开始

### 真实场景

{scene}

### 案例任务

{case_steps[0]}

这不是为了“练习一个函数”而虚构的任务，而是一个需要从原始数据得到明确结论的小型分析问题。

## 三、在引入 Pandas 之前，问题本身是什么

我们手里的数据通常是多行、多列、带字段含义的表格；最终却只想得到少量答案，例如平均分、符合条件的学生、每月销售额或各城市排名。

{without}

因此，真正的困难不是把某个数字算出来，而是同时保持：

- 数据和字段的对应关系不丢失。
- 筛选后仍能知道每一行是谁。
- 计算过程可以批量执行、重复运行和检查。
- 数据规模变大后，不需要重写一套循环。

## 四、为什么要引入今天的新知识

{why}

Pandas 把“带标签的数据”和“对整列、整表的批量操作”放在同一个对象模型中。这样我们可以先表达数据的结构，再表达对结构的操作，代码会更接近业务语言，也更容易复查。

## 五、这个概念到底是什么，用来干什么

{concept}

本节的关键点：

{points}

判断自己是否真正理解的方法：不要先背函数名，先说出输入对象是一列还是一张表、输出应该保留哪些标签、结果的形状应该是什么。

## 六、案例数据：我们具体拿什么来解决

{case_data}

请先圈出：

1. 每一行代表的业务实体。
2. 每一列的含义和预期类型。
3. 哪些列只是描述信息，哪些列会参与计算。
4. 最终答案需要保留哪些字段。

如果连输入数据都没有说清楚，直接开始写 API，后面的结果即使能运行也不一定有意义。

## 七、从问题到答案：每一步为什么自然出现

| 步骤 | 这一刻做什么 | 为什么必须先做或接着做 |
|---|---|---|
{step_table}

这里的逻辑是：先建立正确的数据对象，再确认对象结构；结构确认后才能选择和计算；得到结果后还要验证，最后才适合交付。

## 八、把推导落成代码

请严格按上面的步骤运行，不要一次性把整段代码粘贴出来。每运行一步，都先自己预测：

- 当前变量是什么类型？
- 它有几行几列？
- 索引和列名是否还在？
- 这一步是否创建了新对象？

~~~python
{item.code.rstrip()}
~~~

## 九、把一行代码拆开看：入参、关键字参数和返回值

{PANDAS_API_DETAILS[item.slug]}

阅读一个 Pandas 调用时，按这个顺序检查：

1. 谁被调用了？
2. 第一个位置参数代表什么？
3. 每个关键字参数改变什么行为？
4. 哪些参数可以省略，默认值是什么？
5. 返回的是 Series、DataFrame、标量还是新的对象？

### 代码如何对应推导

1. 先导入 Pandas，是因为接下来要使用它提供的数据对象和批量操作。
2. 再创建或读取数据，是因为任何分析都必须有明确输入。
3. 然后观察对象，是为了验证“我们以为的数据结构”和“程序实际拿到的结构”一致。
4. 接着进行本节核心操作，是因为前面的结构和口径已经确定。
5. 最后打印、统计或导出，是为了把程序内部结果变成可以检查和沟通的答案。

## 十、如果不用它，还有什么办法

{alternatives}

选择 Pandas 不是因为其他方法完全不能做，而是因为当前问题同时需要标签、批量计算、缺失处理和可复查流程。数据量、字段数量和后续任务越大，这个优势越明显。

## 十一、还要特别关注哪些细节

- 结果是 Series 还是 DataFrame，直接影响后续方法和形状。
- 标签对齐可能改变结果对应关系，不能只凭位置猜测。
- 缺失值不等于 0，空结果也不一定代表代码正确。
- 绝大多数操作返回新对象；需要修改原表时必须显式赋值并检查结果。
- 统计前要确认粒度、单位、分母和筛选条件，否则数字精确也没有业务意义。

## 十二、自己动手练习

{item.exercise}

请模仿本节的推导顺序完成：

1. 先写出数据说明和目标。
2. 再写不用 Pandas 时的思路。
3. 然后逐步实现并在每一步打印中间结果。
4. 最后增加一个空数据、缺失值、边界值或未匹配记录案例。

完成后再打开 03_answers.py，比较的重点不是代码长得像不像，而是每个决策是否有理由。

## 十三、完成后的自我检查

请先合上前面的内容，独立回答下面四个问题，再展开参考答案。

### 问题 1：这个知识点解决什么类型的问题？

你的回答：

### 问题 2：为什么当前案例需要它？

你的回答：

### 问题 3：每一步代码为什么要在此时出现？

你的回答：

### 问题 4：如果换一种做法，代价和风险是什么？

你的回答：

## 十四、参考答案

### 问题 1 的参考答案

本节解决的是：{concept}

### 问题 2 的参考答案

当前案例需要它，是因为：{why} 只有把数据组织成适合批量操作的对象，后面的选择、计算和验证才不会依赖大量手工循环。

### 问题 3 的参考答案

每一步都有前置关系：先准备并确认输入，才能知道对象类型和形状；确认结构后，才能选择或计算；得到结果后，还要验证是否错位、漏行或统计口径错误。

### 问题 4 的参考答案

替代方案是：{without} 当前方法的优势在于保留标签、支持批量操作、减少重复代码，并且更容易扩展到更多数据和后续分析。
"""


def readme_for(course: str, chapter: str, item: Lesson, number: int) -> str:
    if course == "Python 数据分析" and chapter == "02_pandas":
        return pandas_readme_for(item, number)
        scene, why = PANDAS_CHAPTER_CONTEXT[item.slug]
        case_steps = "\n".join(f"{step_number}. {step}" for step_number, step in enumerate(PANDAS_CASE_STEPS[item.slug], 1))
        step_whys = "\n".join(
            f"| 第 {step_number} 步 | {step} | {why} |"
            for step_number, (step, why) in enumerate(
                zip(PANDAS_CASE_STEPS[item.slug][1:], PANDAS_STEP_WHY[item.slug]), 1
            )
        )
        points = "\n".join(f"- {point}" for point in item.points)
        if item.slug == "01_series_dataframe":
            what = (
                "Series 是带有索引标签的一维数据，适合表示一个字段，例如全班成绩、商品价格或日期序列。"
                "DataFrame 是带行索引和列名的二维表，适合表示多条记录；它可以看作多个长度相同、按索引对齐的 Series 组成的表。"
                "选择一列通常得到 Series，选择多列通常仍得到 DataFrame；这也是初学者最需要通过 type 和 shape 观察的差异。"
            )
        else:
            what = f"本节围绕“{item.title}”把一组原始数据转换成可检查、可解释的分析结果。"
        return f"""# {number:02d}. {item.title}

> 所属课程：{course}  
> 所属章节：{chapter}

## 一、授课导入：先看场景

{scene}

请先让学生回答：场景中有哪些数据？每一行代表什么？我们最终想回答什么问题？

## 二、今天要解决的小案例

{case_steps}

每完成一步就暂停提问：当前拿到的对象是什么？它的形状是什么？下一步为什么需要这个操作？

## 三、案例数据：我们手里具体有什么

{PANDAS_CASE_DATA[item.slug]}

这些数据不是装饰。授课时应先让学生指出：每一行代表什么、每一列是什么类型、哪些字段会参与计算。只有明确输入，后面的代码才有可解释性。

## 四、逐步解决：每一步为什么这样做

| 步骤 | 做什么 | 为什么现在做 |
|---|---|---|
{step_whys}

## 五、为什么需要这个知识点

{why}

本节解决的不是“记住一个函数”，而是把一个实际数据问题转换成可检查的 Pandas 操作。

## 六、这个知识点具体做什么

{item.summary}

{what}

本节的关键概念：

{points}

## 七、教师讲解顺序

1. 先展示原始数据的形状、列名和一两行样例。
2. 让学生预测操作后对象的类型、形状和结果。
3. 运行 01_examples.py，逐段解释每个参数和返回值。
4. 修改一个输入，让学生观察结果如何变化。
5. 最后再布置 02_exercises.py 中的练习。

## 八、完整代码实例

~~~python
{item.code.rstrip()}
~~~

## 九、代码逐段解释

- 导入：import pandas as pd 是社区约定的别名，后续通过 pd 调用 Pandas。
- 输入：先确认数据是一列值、多个字段的记录，还是来自文件的长表。
- 标签：index 和 columns 参与定位、对齐和展示，不是可有可无的装饰。
- 结果：同时观察 type、shape、index、columns 和 dtype，不能只看打印出来的表格。
- 复现：课堂代码应保留原始数据，派生结果通过新变量或新列保存。

## 十、替代方案与当前方案优势

{PANDAS_ALTERNATIVES[item.slug]}

课堂追问：如果不用 Pandas，学生会怎样写？哪种写法在数据量变大、字段变多或需要复查时更容易出错？

## 十一、课堂提问

- 如果把输入换成空表，结果会是什么？
- 哪一步返回了新对象？哪一步真正修改了原对象？
- 如果列名拼写错误，应该从哪一行开始排查？
- 这个结果能回答场景中的业务问题吗？统计口径是否一致？

## 十二、学生练习

{item.exercise}

要求学生至少完成一个正常案例和一个边界案例，并在代码中写出中文注释说明每一步的目的。

提交前检查：

- [ ] 我能用自己的话说清场景和为什么需要本节知识。
- [ ] 我能解释输入、输出、类型和形状。
- [ ] 我处理了空值、空表或没有匹配记录的情况。
- [ ] 我用 print、shape 或 assert 验证了结果。

## 十三、常见错误与教师提醒

- 把 Series 和 DataFrame 混用，导致选择结果的形状不符合预期。
- 多条件筛选忘记括号，或把 Python 的 and/or 直接用于 Series。
- 直接覆盖原始数据，导致无法回溯清洗前的结果。
- 只关注代码能运行，不检查 dtype、缺失值和统计口径。

## 十四、本节小结

请学生用一句话完成复述：在“{scene.split("，")[0]}”这个场景中，我使用 Pandas 的本节能力把什么输入转换成了什么结果。

完成练习后，再打开 03_answers.py 对照实现，并记录自己与参考答案的一个差异。
"""
    points = "\n".join(f"- {point}" for point in item.points)
    return f"""# {number:02d}. {item.title}

> 所属课程：{course}  
> 所属章节：{chapter}

## 学习目标

{item.summary}

完成本节后，你应该能够不用照抄示例，独立解释概念、运行代码并完成练习。

## 核心知识

{points}

## 示例代码

```python
{item.code.rstrip()}
```

请先预测输出，再运行 01_examples.py。遇到结果与预测不一致时，在代码旁写下原因。

## 常见错误

- 只记住写法，没有观察输入、输出、类型和对象是否被修改。
- 修改示例时一次改动太多，导致无法判断是哪一步产生了差异。
- 看到异常就删除代码；更好的做法是阅读最后一行错误类型和信息，再定位对应行。

## 本节练习

{item.exercise}

建议先完成 02_exercises.py，运行并自行检查，再打开 03_answers.py。参考答案只是其中一种实现。

## 学习检查

- [ ] 我能用自己的话解释“{item.title}”。
- [ ] 我能不看文档重新写出核心示例。
- [ ] 我完成了练习，并比较了参考答案。
- [ ] 我记录了至少一个易错点。

## 下一步

回到本章 00_chapter_overview.md，按编号进入下一知识点。不要跳过尚未理解的基础概念。
"""


def exercises_for(item: Lesson) -> str:
    return f'''"""{item.title}：练习文件。

任务：{item.exercise}
请先独立完成。允许复制 01_examples.py 后逐步修改，但不要先看 03_answers.py。
"""


def main():
    # TODO 1：按照 README 的任务描述实现核心功能。
    # TODO 2：至少增加一个边界输入，并观察程序行为。
    # TODO 3：使用 print 或 assert 验证结果，而不是只凭感觉判断。
    pass


if __name__ == "__main__":
    main()
'''


def answer_for(item: Lesson) -> str:
    indented = "\n".join("    " + line if line else "" for line in item.code.rstrip().splitlines())
    return f'''"""{item.title}：参考答案。

这份答案演示核心写法。练习任务通常还有其他正确实现；请重点比较思路。
"""


def main():
    # 先运行本答案，再逐行对照自己的实现。
{indented}


if __name__ == "__main__":
    main()
'''


PANDAS_ALTERNATIVE_CODE = {
    "01_series_dataframe": '''# 先用已经学过的列表和字典保存案例数据：每个字典是一名学生的一行记录。
# 现在先不急着学习 Pandas，而是问：只靠基础语法，这个任务能不能完成？
# 先看整体路线：第 1 步取出成绩，第 2 步根据成绩计算平均分，第 3 步逐行筛选达标学生。
# 之所以按这个顺序，是因为后面的计算需要先有 scores，筛选则需要回到完整的 students 记录中。
students = [
    {"name": "小林", "class": "一班", "python": 95},
    {"name": "小周", "class": "一班", "python": 84},
    {"name": "小陈", "class": "二班", "python": 90},
    {"name": "小李", "class": "二班", "python": 75},
]
# 第 1 步：先取出所有 Python 成绩。
# 为什么：平均分只针对 python 这一列，字典不会自动把它变成一列，所以要自己按键名取值。
scores = [row["python"] for row in students]

# 第 2 步：把成绩相加，再除以人数，得到平均分。
# 为什么：这是我们在基础语法阶段已经学过的 sum 和 len；先完成任务，再观察代码代价。
average_score = sum(scores) / len(scores)
print("列表平均分：", average_score)

# 第 3 步：逐行判断成绩是否达到 85 分，并保留整条学生记录。
# 为什么：只保留分数会丢掉姓名和班级，所以筛选结果仍然应该是字典列表。
qualified = []
for row in students:
    if row["python"] >= 85:
        qualified.append(row)
print("列表筛选：", qualified)''',
    "02_read_inspect": '''import csv
from pathlib import Path
path = Path(__file__).resolve().parents[2] / "datasets" / "sales.csv"
with path.open(encoding="utf-8", newline="") as file:
    rows = list(csv.DictReader(file))
print("csv 行数：", len(rows))
print("csv 列名：", list(rows[0]) if rows else [])''',
    "03_select_loc_iloc": '''rows = [
    {"order_id": "S001", "city": "上海", "amount": 798},
    {"order_id": "S002", "city": "北京", "amount": 387},
]
selected = [row for row in rows if row["city"] == "上海"]
print("列表筛选：", selected)
print("列表位置切片：", rows[:1])''',
    "04_filter_query": '''rows = [
    {"city": "上海", "quantity": 2, "price": 399},
    {"city": "北京", "quantity": 1, "price": 899},
]
selected = [row for row in rows if row["city"] in {"上海", "北京"} and row["quantity"] >= 2 and row["price"] > 100]
print("列表多条件筛选：", selected)''',
    "05_modify_assign": '''rows = [{"price": 100, "quantity": 2}, {"price": 50, "quantity": 1}]
for row in rows:
    row["amount"] = row["price"] * row["quantity"]
    row["level"] = "高" if row["amount"] >= 100 else "普通"
print("逐行新增字段：", rows)''',
    "06_types_missing": '''raw_values = ["18", "未知", None]
values = []
for value in raw_values:
    try:
        values.append(float(value))
    except (TypeError, ValueError):
        values.append(None)
print("逐个转换后的值：", values)''',
    "07_duplicates_strings": '''rows = [{"email": "A@X.COM"}, {"email": "a@x.com"}, {"email": "b@x.com"}]
seen = set()
unique = []
for row in rows:
    row["email"] = row["email"].strip().lower()
    if row["email"] not in seen:
        seen.add(row["email"])
        unique.append(row)
print("手工去重：", unique)''',
    "08_datetime": '''from datetime import datetime
dates = [datetime.strptime(value, "%Y-%m-%d") for value in ["2026-01-03", "2026-02-14"]]
months = {}
for value in dates:
    key = value.strftime("%Y-%m")
    months[key] = months.get(key, 0) + 1
print("手工按月计数：", months)''',
    "09_sort_groupby": '''rows = [{"city": "上海", "amount": 100}, {"city": "上海", "amount": 300}, {"city": "北京", "amount": 200}]
groups = {}
for row in rows:
    groups.setdefault(row["city"], []).append(row["amount"])
summary = [{"city": city, "total": sum(values)} for city, values in groups.items()]
print("手工分组汇总：", sorted(summary, key=lambda row: row["total"], reverse=True))''',
    "10_merge_concat": '''orders = [{"customer_id": 1, "amount": 100}, {"customer_id": 2, "amount": 200}]
customers = [{"customer_id": 1, "name": "甲"}, {"customer_id": 2, "name": "乙"}]
customer_map = {row["customer_id"]: row for row in customers}
merged = [{**order, **customer_map.get(order["customer_id"], {})} for order in orders]
print("字典关联：", merged)
print("列表拼接：", orders + orders)''',
    "11_pivot_crosstab": '''rows = [{"city": "上海", "product": "A", "amount": 100}, {"city": "上海", "product": "B", "amount": 200}]
pivot = {}
for row in rows:
    pivot.setdefault(row["city"], {})
    pivot[row["city"]][row["product"]] = pivot[row["city"]].get(row["product"], 0) + row["amount"]
print("嵌套字典透视：", pivot)''',
    "12_apply_transform": '''rows = [{"group": "A", "score": 80}, {"group": "A", "score": 100}, {"group": "B", "score": 70}]
totals = {}
for row in rows:
    totals[row["group"]] = totals.get(row["group"], 0) + row["score"]
for row in rows:
    row["ratio"] = row["score"] / totals[row["group"]]
print("逐行回填比例：", rows)''',
    "13_outliers_export": '''values = [10, 11, 12, 13, 100]
ordered = sorted(values)
q1, q3 = ordered[1], ordered[3]
iqr = q3 - q1
outliers = [value for value in values if value > q3 + 1.5 * iqr]
print("手工标记异常值：", outliers)''',
}


PANDAS_API_DETAILS = {
    "01_series_dataframe": """先看这一行：pd.Series([88, 95, 82], index=["甲", "乙", "丙"], name="成绩")。

- pd.Series 是 Pandas 提供的构造函数，用来创建一维 Series 对象。
- 第一个参数 [88, 95, 82] 是 data，放在位置上，是这一列真正保存的值。
- index=["甲", "乙", "丙"] 是关键字参数，给每个值提供标签；关键字写法让人一眼看出它的用途。
- name="成绩" 也是关键字参数，为这一列取名，打印、合并或放入 DataFrame 时更容易识别。
- data 可以不写名字，但 index 和 name 如果写出来，最好保留关键字形式，不要依赖参数位置。
- 这行代码返回一个 Series，索引和值会一一对应；如果 data 和 index 长度不同，会报错。

再看 DataFrame：pd.DataFrame({...})。

- 字典作为 data，每个键变成列名，每个列表变成一列；各列长度必须一致。
- 这个调用返回二维 DataFrame，所以后面既能按列取 Series，也能按行筛选完整记录。
- students["python"] 使用列名取一列，结果是 Series；students[["python"]] 使用双层列表取列，结果仍是 DataFrame。
- students.loc[条件] 中，条件是一个与行数相同的布尔 Series，loc 按标签和条件选择行。""",
    "02_read_inspect": "read_csv(path, ...) 用来把 CSV 文件读成 DataFrame，path 是文件路径；head(n) 返回前 n 行，info() 汇报列名、非空数量和 dtype，describe(include=...) 返回统计摘要。它们都用于先认识数据，而不是直接开始计算。",
    "03_select_loc_iloc": "loc[行条件, 列标签] 按标签选择，行条件可以是标签或布尔 Series；iloc[行位置, 列位置] 按整数位置选择。loc 的列参数可写一个列名或列名列表，结果可能是 Series 或 DataFrame。",
    "04_filter_query": "isin(values) 判断每行值是否属于 values；query(expr) 接收条件字符串并返回筛选后的 DataFrame。多个布尔 Series 要用括号配合 &、|、~，因为它们是逐行运算。",
    "05_modify_assign": "给 data[列名] 赋值可以新增或覆盖整列，右侧可为标量或等长 Series；loc[行条件, 列名] 只更新指定行列，返回赋值后的表需要再次检查。",
    "06_types_missing": "to_numeric(arg, errors=...) 把 arg 转为数值，errors='coerce' 把无法转换的值变为 NaN；isna() 统计缺失，fillna(value) 用 value 填补。每个方法都返回结果，除非显式赋回原列，否则不会自动修改原表。",
    "07_duplicates_strings": "Series.str 是字符串方法访问器，strip() 去首尾空白、lower() 转小写；duplicated(subset=...) 标记重复行，drop_duplicates(subset=..., keep=...) 删除重复并决定保留第一条、最后一条或全部。",
    "08_datetime": "to_datetime(arg, errors=...) 把 arg 转为日期时间；dt.to_period(freq) 按 freq='M' 提取月份周期；groupby(by) 按 by 指定的字段分组。日期解析失败时要先决定是否转成 NaT。",
    "09_sort_groupby": "groupby(by, as_index=False) 按 by 分组，as_index=False 让分组键保留为普通列；agg 用命名关键字定义每个输出指标，例如 total=('amount','sum')，返回汇总 DataFrame。",
    "10_merge_concat": "merge(right, on=..., how=..., indicator=...) 把 right 表按连接键合并，how 决定保留哪边记录，indicator 增加匹配状态；concat(objs, ignore_index=True) 沿轴拼接表列表，ignore_index 重建行号。",
    "11_pivot_crosstab": "pivot_table(data, values=..., index=..., columns=..., aggfunc=..., fill_value=...) 把长表重塑为汇总矩阵；values 是要统计的值，index/columns 定义行列维度，aggfunc 定义聚合方法。",
    "12_apply_transform": "apply(func) 可按行或列执行自定义函数，返回形状取决于 func；transform(func) 也接收规则，但保证结果与原表等长，适合把分组指标对齐回明细行。",
    "13_outliers_export": "quantile(q) 返回 q 位置的分位数，q 通常在 0 到 1 之间；to_csv(path, index=False) 把结果写到 path，index=False 表示不把索引另写成一列。",
}


PANDAS_COMMON_VARIANTS = {
    "02_read_inspect": '''
# 常用读取与观察方式：同一个任务不只有一种 API。
# read_csv 的 usecols 只读指定列，nrows 只读前几行，parse_dates 尝试把日期列直接解析为日期。
sample = pd.read_csv(path, usecols=["order_id", "city", "amount"], nrows=3)
print("\\n===== pd.read_csv(usecols=..., nrows=...) =====")
print(sample)
# head(n) 看开头，tail(n) 看结尾，sample(n, random_state=...) 随机抽样且可复现。
print("\\n===== data.tail(2) =====")
print(data.tail(2))
print("\\n===== data.sample(2, random_state=42) =====")
print(data.sample(2, random_state=42))
# shape、columns、dtypes、isna().sum() 分别回答大小、字段、类型和缺失数量。
print("\\n===== data.shape / data.columns / data.dtypes / data.isna().sum() =====")
print(data.shape)
print(data.columns.tolist())
print(data.dtypes)
print(data.isna().sum())
''',
    "03_select_loc_iloc": '''
# loc/iloc 的常用变体：选单列、选多列、选单行和切片。
one_column = data.loc[:, "score"] if "score" in data.columns else data.loc[:, "city"]
many_columns = data.loc[:, ["name", "score"]] if "name" in data.columns else data.loc[:, ["city", "amount"]]
first_row = data.iloc[0]
first_two_rows = data.iloc[:2, :]
print("\\n===== 单列 Series =====")
print(one_column)
print("\\n===== 多列 DataFrame =====")
print(many_columns)
print("\\n===== iloc[0] 单行 =====")
print(first_row)
print("\\n===== iloc[:2, :] 前两行 =====")
print(first_two_rows)
''',
    "04_filter_query": '''
# 条件筛选的常用变体：单条件、多个条件、集合、区间和缺失值。
print("\\n===== 单条件 =====")
print(data[data["amount"] >= 1000].to_markdown(index=False))
print("\\n===== isin 集合 =====")
print(data[data["city"].isin(["上海", "北京"])].to_markdown(index=False))
print("\\n===== between 区间 =====")
print(data[data["amount"].between(500, 1500)].to_markdown(index=False))
print("\\n===== isna / notna =====")
print(data[data["amount"].notna()].to_markdown(index=False))
''',
    "05_modify_assign": '''
# 新增和修改列的常用变体：直接赋值、assign、条件赋值和删除列。
data_copy = data.assign(total=data["price"] * data["quantity"])
print("\\n===== assign 新增列 =====")
print(data_copy)
data_copy.loc[data_copy["total"] >= 100, "tag"] = "高"
data_copy["tag"] = data_copy["tag"].fillna("普通")
print("\\n===== loc 条件修改 =====")
print(data_copy)
remaining = data_copy.drop(columns=["tag"])
print("\\n===== drop(columns=...) 删除列 =====")
print(remaining)
''',
    "06_types_missing": '''
# 类型与缺失值的常用变体：查看、删除、填充和不同错误策略。
print("\\n===== isna / notna =====")
print(data.isna())
print(data.notna())
print("\\n===== dropna(subset=...) =====")
# dropna(subset=["score"]) 只删除 score 缺失的行，不会把数值重新转回整数。
# score 原本包含 None/NaN，Pandas 为了同时容纳整数和缺失值，通常会把这一列提升为 float，所以看到 90.0、80.0 是正常的。
print(data.dropna(subset=["score"]))
# age 经过 to_numeric(errors="coerce") 后，"错误" 变成 NaN，同样可能导致这一列显示为浮点数。
print(data.dropna(subset=["age"]))
print("\\n===== fillna(标量) =====")
print(data["score"].fillna(0))
print("\\n===== to_numeric(errors='ignore') 对比 =====")
# 注意：前面已经用 errors="coerce" 把“错误”转换成 NaN；现在再用 errors="raise"，检查的是已经清洗过的列，所以不会报错。
print(pd.to_numeric(data["age"], errors="raise"))
# 如果要观察 errors="raise" 的报错，必须对仍含有非法文本的原始数据执行转换。
raw_age = pd.Series(["18", "错误", None])
# print(pd.to_numeric(raw_age, errors="raise"))  # 会因为“错误”无法转换而抛出 ValueError
print(pd.to_numeric(data["age"], errors="coerce"))
''',
    "07_duplicates_strings": "",
    "08_datetime": '''
# 日期时间的常用变体：解析、提取组成部分、格式化和日期差。
print("\\n===== dt.year / dt.month / dt.day =====")
print(data["date"].dt.year)
print(data["date"].dt.month)
print(data["date"].dt.day)
print("\\n===== dt.strftime() =====")
print(data["date"].dt.strftime("%Y-%m"))
print("\\n===== 日期范围筛选 =====")
print(data[data["date"].between("2026-01-01", "2026-02-28")])
''',
    "09_sort_groupby": '''
# 排序和分组的常用变体：升降序、取前几名、计数和多指标聚合。
print("\\n===== sort_values 多列排序 =====")
print(data.sort_values(["amount", "city"], ascending=[False, True]))
print("\\n===== nlargest 取前几名 =====")
print(data.nlargest(2, "amount"))
print("\\n===== groupby.size 计数 =====")
print(data.groupby("city").size())
print("\\n===== groupby.agg 多指标 =====")
print(data.groupby("city", as_index=False).agg(total=("amount", "sum"), average=("amount", "mean")))
''',
    "10_merge_concat": '''
# 表连接的常用变体：inner、left、right、outer，以及按行和按列拼接。
print("\\n===== inner merge =====")
print(orders.merge(customers, on="customer_id", how="inner"))
print("\\n===== outer merge + indicator =====")
print(orders.merge(customers, on="customer_id", how="outer", indicator=True))
print("\\n===== concat 按行 =====")
print(pd.concat([orders, orders], axis=0, ignore_index=True))
print("\\n===== concat 按列 =====")
print(pd.concat([orders.reset_index(drop=True), customers[["name"]]], axis=1))
''',
    "11_pivot_crosstab": '''
# 重塑表格的常用变体：pivot_table、crosstab、margins 和 melt。
print("\\n===== pivot_table 多种聚合 =====")
print(pd.pivot_table(data, values="amount", index="city", columns="product", aggfunc=["sum", "mean"], fill_value=0))
print("\\n===== crosstab normalize =====")
print(pd.crosstab(data["city"], data["product"], normalize="index"))
print("\\n===== melt 宽表转长表 =====")
wide = pd.DataFrame({"city": ["上海", "北京"], "A": [100, 150], "B": [200, 80]})
print(wide.melt(id_vars="city", var_name="product", value_name="amount"))
''',
    "12_apply_transform": '''
# 自定义处理的常用变体：map 逐元素、apply 按行/列、transform 保持原长度。
data["level"] = data["score"].map(lambda value: "优秀" if value >= 90 else "普通")
print("\\n===== Series.map =====")
print(data)
print("\\n===== DataFrame.apply(axis=1) =====")
print(data.apply(lambda row: row["score"] - row["group_mean"], axis=1))
print("\\n===== groupby.transform =====")
print(data.groupby("group")["score"].transform("mean"))
''',
    "13_outliers_export": '''
# 异常值与导出的常用变体：上下界、布尔标记、clip 截断和不同导出格式。
lower = q1 - 1.5 * iqr
upper = q3 + 1.5 * iqr
print("\\n===== IQR 上下界 =====")
print(lower, upper)
print("\\n===== clip 截断极端值 =====")
print(values.clip(lower=lower, upper=upper))
print("\\n===== to_csv 参数 =====")
print("to_csv(path, index=False) 会导出 CSV，index=False 不写索引列。")
''',
}


def pandas_guided_code(item: Lesson) -> str:
    if item.slug == "01_series_dataframe":
        return '''import pandas as pd

# Series 像 Excel 的一列：每个值除了内容，还有一个 index 标签和可选的 name。
# DataFrame 像 Excel 的一张表：有 index 行标签、columns 列名和二维 values。
# 先理解这两个对象，后面才知道为什么一列适合统计、整张表适合筛选完整记录。

# 第 1 步：先把“一列成绩”变成 Series。
# 为什么：基础语法方案需要我们手工循环取 python；Series 可以把“成绩”和“学生标签”放在同一个对象里。
# pd.Series(data, index=..., name=...)：data 是位置参数，index/name 是关键字参数。
# data 是真正保存的值；index 为每个值提供标签；name 给这一列命名；返回值是 Series。
# data 和 index 长度必须一致，否则一个值无法对应一个标签。
scores_series = pd.Series([88, 95, 82], index=["甲", "乙", "丙"], name="成绩")
print("\\n===== 观察 Series =====")
print("scores_series：")
print("\\n===== Series 数据 =====")
print(scores_series)
print("\\n===== 检查 Series 的组成 =====")
print("\\n===== Series 类型 =====")
print("类型：", type(scores_series).__name__)
print("\\n===== Series 索引 =====")
print("索引：", scores_series.index.tolist())
print("\\n===== Series 名称 =====")
print("名称：", scores_series.name)

# 第 2 步：案例还要保留姓名、班级和多门成绩，所以一列不够，需要 DataFrame。
# 为什么：DataFrame(data=...) 接收字典时，键成为列名，列表成为列值；所有列表长度必须一致。
# data= 是关键字参数；省略名字也能运行，但显式写出更容易读懂。返回值是二维 DataFrame。

# 中文表格在不同终端中的宽度可能显示不齐；这两个全局选项只影响显示，不会改变数据本身。
pd.set_option("display.unicode.east_asian_width", True)
pd.set_option("display.unicode.ambiguous_as_wide", True)

students = pd.DataFrame(data={
    "name": ["小林", "小周", "小陈", "小李"],
    "class": ["一班", "一班", "二班", "二班"],
    "math": [92, 76, 85, 68],
    "python": [95, 84, 90, 75],
})
print("\\n===== 观察 DataFrame =====")
print(students)

# to_markdown(index=False) 把 DataFrame 转成 Markdown 表格文本，方便复制到笔记或报告。
# index=False 是关键字参数，表示不把 Pandas 的行索引额外输出成一列。
# 本节优先使用 Markdown 格式观察表格；如果本机尚未安装 tabulate，再单独改成 print(students) 即可。
print("\\n===== 使用 Markdown 格式观察 DataFrame =====")
print(students.to_markdown(index=False))

# shape 返回 (行数, 列数)，columns 返回列标签；先检查它们，是为了确认字段没有错位。
print("\\n===== 检查 DataFrame 结构 =====")
print("形状：", students.shape)
print("\\n===== DataFrame 列名 =====")
print("列名：", students.columns.tolist())

# 第 3 步：对比单层和双层方括号，理解返回对象不同。
# students["python"]：传入一个列名字符串，返回 Series，适合对一列求平均。
python_scores_series = students["python"]
print("\\n===== 比较单层和双层方括号 =====")
print("单层选择类型：", type(python_scores_series).__name__)
# students[["python"]]：传入“列名列表”，返回仍是 DataFrame，适合保留二维表形状。
python_scores_frame = students[["python"]]
print("\\n===== 双层方括号选择类型 =====")
print("双层选择类型：", type(python_scores_frame).__name__)

# mean() 用来求平均值；这里没有必填参数，返回一个数值。
# Series 已经知道这一列的全部值，所以不必再手写 sum(...) / len(...)。
average_score = python_scores_series.mean()
print("\\n===== 计算平均分 =====")
print("全班 Python 平均分：", average_score)

# 第 4 步：根据成绩条件筛选，但保留整行信息。
# python_scores_series >= 85 会产生布尔 Series；每个 True/False 与原表的一行对齐。
# loc[行条件, 列选择] 按标签选择数据；只写一个条件时表示筛选行，返回 DataFrame。
qualified = students.loc[python_scores_series >= 85]
print("\\n===== 筛选完整达标记录 =====")
print("Python 成绩不低于 85 分的学生：")
print("\\n===== 达标学生表 =====")
print(qualified)

# 同一个筛选也可以写成 students[students["python"] >= 85]；loc 更明确地表达了“按标签筛选”。
qualified_short = students.loc[students["python"] >= 85, ["name", "python"]]
print("\\n===== 筛选指定列 =====")
print("只保留姓名和 Python 成绩：")
print("\\n===== 指定列结果 =====")
print(qualified_short)

# 最后手算 (95 + 84 + 90 + 75) / 4，验证平均分没有错位。
assert average_score == (95 + 84 + 90 + 75) / 4
'''
    # 其他知识点的示例代码也按空行切成若干小段，在每段代码旁放置对应原因。
    # 这样学习者可以逐段运行，而不是一次执行一整块代码。
    blocks = [block.strip() for block in item.code.split("\n\n") if block.strip()]
    step_items = [step.split("：", 1)[-1] for step in PANDAS_CASE_STEPS[item.slug][1:]]
    rendered = []
    for number, block in enumerate(blocks, 1):
        output_lines = []
        for line in block.splitlines():
            stripped = line.strip()
            if stripped.startswith("print(") or stripped.endswith(".info()"):
                expression = stripped[6:-1] if stripped.startswith("print(") else stripped
                separator = repr(f"\n===== {expression} =====")
                output_lines.append(f"print({separator})")
            output_lines.append(line)
        block = "\n".join(output_lines)
        api_hint = ""
        if item.slug in PANDAS_API_DETAILS:
            # 每个代码段旁都保留本节 API 的用途和参数提示，避免学习者只看到调用却不知道入参和返回值。
            api_hint = "\n".join(f"# 调用提示：{line}" for line in PANDAS_API_DETAILS[item.slug].splitlines() if line.strip()) + "\n"
        if number <= len(step_items):
            rendered.append(
                f"# 第 {number} 步：{step_items[number - 1]}\n"
                f"# 为什么：{PANDAS_STEP_WHY[item.slug][number - 1]}\n"
                f'{api_hint}{block}'
            )
        else:
            rendered.append(f'{api_hint}{block}')
    return "\n\n".join(rendered)


def pandas_notes_for(item: Lesson) -> str:
    scene, why = PANDAS_CHAPTER_CONTEXT[item.slug]
    case_steps = PANDAS_CASE_STEPS[item.slug]
    step_whys = PANDAS_STEP_WHY[item.slug]
    case_data = PANDAS_CASE_DATA[item.slug]
    alternatives = PANDAS_ALTERNATIVES[item.slug]
    points = "；".join(item.points)
    step_items = [step.split("：", 1)[-1] for step in case_steps[1:]]
    if item.slug == "01_series_dataframe":
        concept = "Series 是带索引标签的一维数据；DataFrame 是带行索引和列名的二维表，适合保存多条完整记录。"
    else:
        concept = f"{item.title} 的核心，是把原始表格转换成可检查、可复用的分析结果。"
    step_notes = "\n".join(
        f"第 {step_number} 步：{step}\n为什么：{step_whys[step_number - 1]}"
        for step_number, step in enumerate(step_items, 1)
    )
    return f'''学习笔记：{item.title}

一、今天要学什么
{item.summary}
学习时不要只记函数名，要能说明问题类型、使用原因、步骤关系和替代方案。

二、问题源头与案例
真实场景：{scene}
案例任务：{case_steps[0].removeprefix("案例任务：")}
案例数据：
{case_data}

三、不用 Pandas 时会怎样
{alternatives}

四、为什么引入这个概念
{why}

五、概念和用途
{points}

六、逐步推导
{step_notes}

七、写代码时逐项检查
- 当前变量是什么类型？
- 当前对象有几行几列？
- 索引和列名是否还在？
- 这一步为什么必须在现在出现？
- 结果是否真的回答了案例任务？

八、需要关注的细节
- Series 和 DataFrame 的形状不同。
- 标签对齐可能影响结果对应关系。
- 缺失值不等于 0，空结果也需要解释。
- 大多数操作返回新对象，修改必须显式赋值。
- 统计前要确认粒度、单位、分母和筛选条件。

九、完成后自测
1. 这个知识点解决什么类型的问题？
2. 为什么当前案例需要它？
3. 每一步代码为什么要在此时出现？
4. 如果换一种做法，代价和风险是什么？

参考答案提示：
1. {concept}
2. 当前案例需要它，是因为 {why}
3. 步骤有前置关系：先准备并确认输入，再选择或计算，最后验证。
4. {alternatives}
'''


def pandas_examples_for(item: Lesson) -> str:
    # 先只呈现任务；具体步骤在完成基础语法方案后，随着 Pandas 代码自然展开。
    case_steps = f"# {PANDAS_CASE_STEPS[item.slug][0].removeprefix('案例任务：')}"
    alternative_code = PANDAS_ALTERNATIVE_CODE[item.slug]
    alternative_review = PANDAS_ALTERNATIVES[item.slug]
    guided_code = pandas_guided_code(item)
    variant_code = PANDAS_COMMON_VARIANTS.get(item.slug, "")
    if item.slug == "01_series_dataframe":
        transition = (
            "上面的列表和字典代码确实能完成任务，但如果数据从 4 条变成 4 万条，"
            "你就得继续往列表里加记录；如果字段从 python 增加到 math、english，"
            "平均分、筛选和字段对应也要自己维护。这样代码会越来越长，也不容易扩展。"
            "有没有更好的办法？有。Pandas 里的 Series 专门表示带标签的一列数据，"
            "DataFrame 专门表示带列名的二维表。我们先用最小例子看看它们长什么样，"
            "再把它们放回当前成绩案例中。"
        )
    else:
        transition = (
            f"上面的对照代码可以得到结果，但它把很多工作留给我们自己：{alternative_review}"
            f"所以我们自然会问：有没有一种现成的数据对象，能把这些重复工作统一起来？"
            f"有，Pandas 的“{item.title}”正是为这类表格问题准备的。接下来先用最小步骤试用它，"
            "每一步都看清楚输入、输出和为什么要继续下一步。"
        )
    if item.slug == "01_series_dataframe":
        route_overview = ""
        opening_doc = '''阅读顺序：
1. 先运行“不用 Pandas”的代码，观察它怎样完成任务。
2. 阅读评价，理解这种写法的维护成本。
3. 再运行 Pandas 代码，比较对象、步骤和结果。
4. 最后修改一处输入，确认结论不是巧合。
'''
        pandas_intro = '''# Pandas 是什么：它是一个建立在 Python 之上的开源数据分析库。
# Python 本身提供列表、字典和循环；Pandas 在此基础上提供更适合表格数据的 Series、DataFrame 以及批量计算、筛选和清洗方法。
# 我们今天的教务处任务就是一个典型例子：数据有行、有列、有字段含义，还要重复进行统计和筛选。
# 先用基础语法完成一次，再观察为什么 Pandas 能让同类工作更清楚、更容易扩展。'''
        object_answer = "本节是在处理哪种表格对象？主要处理一维 Series 和二维 DataFrame：Series 表示一列，DataFrame 表示完整表格。"
        problem_answer = "核心方法要解决什么问题？解决带标签数据的选择、整列统计和完整记录筛选，减少列表、字典和循环的手工维护。"
        shape_answer = "输入是什么，返回结果的形状会怎样变化？输入是一列成绩或多列学生记录；选择单列返回 Series，选择多列或筛选整行返回 DataFrame，mean() 返回一个数值。"
    else:
        route_names = [step.split("：", 1)[-1] for step in PANDAS_CASE_STEPS[item.slug][1:]]
        route_lines = "\n".join(
            f"# 第 {i} 步：{value.rstrip('。；')}。"
            for i, value in enumerate(route_names, 1)
        )
        route_overview = (
            "# 先看整体路线：\n"
            f"{route_lines}\n"
            "# 顺序不能随意交换：先准备并理解输入，才能进行后续转换、分析和检查。\n"
        )
        opening_doc = ""
        pandas_intro = ""
        object_answer = "本节是在处理哪种表格对象？主要处理带行索引和列名的 DataFrame，部分方法会先取出其中一列 Series。"
        problem_answer = f"核心方法要解决什么问题？解决“{item.title}”这一类表格分析任务：{item.summary}"
        shape_answer = f"输入是什么，返回结果的形状会怎样变化？输入是案例中的原始表格；主要方法的参数和返回结果如下：{PANDAS_API_DETAILS[item.slug]}"
    if item.slug == "01_series_dataframe":
        file_header = f'''"""案例驱动示例：{item.title}

{opening_doc}
"""'''
    else:
        file_header = f'"""案例驱动示例：{item.title}"""'
    intro_block = f"{pandas_intro}\n" if pandas_intro else ""
    # Markdown 输出必须紧跟在有业务意义的结果旁边，不再在文件末尾额外打印一张“为了展示而展示”的表。
    display_code = ""
    return f'''{file_header}
{intro_block}
# 案例任务：
{case_steps}

# ===== 第一步：先用已经学过的基础语法解决案例 =====
# 任务已经明确，接下来先用列表、字典、循环和算术运算完成它。
{route_overview}
{alternative_code}

# 对不用 Pandas 方案的评价：
# {transition}

# ===== 第二步：使用 Pandas 的实现 =====
# 具体函数的入参、关键字参数和返回值，放在每个调用的上一行或下一行说明。
# 进入代码前先确认：本节是在处理哪种表格对象？核心方法要解决什么问题？输入是什么，返回结果的形状会怎样变化？
# {object_answer}
# {problem_answer}
# {shape_answer}
{guided_code}
{variant_code}
{display_code}
'''


PANDAS_EXERCISE_DATA = {
    "02_read_inspect": 'data = pd.DataFrame({"order_id": ["S001", "S002", "S003"], "city": ["上海", "北京", "深圳"], "amount": [798, 1200, 650]})',
    "03_select_loc_iloc": 'data = pd.DataFrame({"order_id": ["S001", "S002", "S003", "S004"], "city": ["上海", "北京", "上海", "深圳"], "product": ["键盘", "鼠标", "显示器", "耳机"], "amount": [798, 1200, 1800, 650]})',
    "04_filter_query": 'data = pd.DataFrame({"city": ["上海", "北京", "深圳", "上海"], "quantity": [2, 3, 1, 4], "price": [399, 129, 899, 120]})',
    "05_modify_assign": 'data = pd.DataFrame({"order_id": ["S001", "S002", "S003"], "price": [100, 50, 80], "quantity": [2, 1, 3]})',
    "06_types_missing": 'data = pd.DataFrame({"age": ["18", "未知", None, "25"], "score": [90, None, 80, 75]})',
    "07_duplicates_strings": 'data = pd.DataFrame({"name": [" Alice ", "alice", "Bob"], "email": ["A@X.COM", "a@x.com", "b@x.com"]})',
    "08_datetime": 'data = pd.DataFrame({"date": ["2026-01-03", "2026-02-14", "2026-02-20"]})',
    "09_sort_groupby": 'data = pd.DataFrame({"city": ["上海", "北京", "上海", "深圳"], "amount": [100, 200, 300, 150]})',
    "10_merge_concat": 'orders = pd.DataFrame({"customer_id": [1, 2, 3], "amount": [100, 200, 150]})\n    customers = pd.DataFrame({"customer_id": [1, 2], "name": ["甲", "乙"]})',
    "11_pivot_crosstab": 'data = pd.DataFrame({"city": ["上海", "上海", "北京"], "product": ["A", "B", "A"], "amount": [100, 200, 150]})',
    "12_apply_transform": 'data = pd.DataFrame({"group": ["A", "A", "B"], "score": [80, 100, 70]})',
    "13_outliers_export": 'data = pd.DataFrame({"order_id": ["S001", "S002", "S003", "S004", "S005"], "amount": [10, 11, 12, 13, 100]})',
}

PANDAS_EXERCISE_TABLES = {
    "01_series_dataframe": """| name | class | math | python |
|---|---|---:|---:|
| 小林 | 一班 | 92 | 95 |
| 小周 | 一班 | 76 | 84 |
| 小陈 | 二班 | 85 | 90 |
| 小李 | 二班 | 68 | 75 |""",
    "02_read_inspect": """| order_id | date | city | product | price | quantity |
|---|---|---|---|---:|---:|
| S001 | 2026-01-03 | 上海 | 键盘 | 399 | 2 |
| S002 | 2026-01-05 | 北京 | 鼠标 | 129 | 3 |
| S003 | 2026-01-12 | 深圳 | 椅子 | 1299 | 1 |
| S004 | 2026-02-02 | 上海 | 显示器 | 1599 | 2 |""",
    "03_select_loc_iloc": """| order_id | city | product | amount |
|---|---|---|---:|
| S001 | 上海 | 键盘 | 798 |
| S002 | 北京 | 鼠标 | 1200 |
| S003 | 上海 | 显示器 | 1800 |
| S004 | 深圳 | 耳机 | 650 |""",
    "04_filter_query": """| order_id | city | quantity | price |
|---|---|---:|---:|
| S001 | 上海 | 2 | 399 |
| S002 | 北京 | 3 | 129 |
| S003 | 深圳 | 1 | 899 |
| S004 | 上海 | 4 | 120 |""",
    "05_modify_assign": """| order_id | price | quantity |
|---|---:|---:|
| S001 | 100 | 2 |
| S002 | 50 | 1 |
| S003 | 80 | 3 |""",
    "06_types_missing": """| name | age | score |
|---|---|---:|
| 甲 | 18 | 90 |
| 乙 | 未知 |  |
| 丙 |  | 80 |
| 丁 | 25 | 75 |""",
    "07_duplicates_strings": """| name | email |
|---|---|
|  Alice  | A@X.COM |
| alice | a@x.com |
| Bob | b@x.com |""",
    "08_datetime": """| order_id | date | amount |
|---|---|---:|
| S001 | 2026-01-03 | 100 |
| S002 | 2026-02-14 | 200 |
| S003 | 2026-02-20 | 150 |""",
    "09_sort_groupby": """| city | amount |
|---|---:|
| 上海 | 100 |
| 北京 | 200 |
| 上海 | 300 |
| 深圳 | 150 |""",
    "10_merge_concat": """订单表 orders：

| customer_id | amount |
|---:|---:|
| 1 | 100 |
| 2 | 200 |
| 3 | 150 |

客户表 customers：

| customer_id | name |
|---:|---|
| 1 | 甲 |
| 2 | 乙 |""",
    "11_pivot_crosstab": """| city | product | amount |
|---|---|---:|
| 上海 | A | 100 |
| 上海 | B | 200 |
| 北京 | A | 150 |""",
    "12_apply_transform": """| group | score |
|---|---:|
| A | 80 |
| A | 100 |
| B | 70 |""",
    "13_outliers_export": """| order_id | amount |
|---|---:|
| S001 | 10 |
| S002 | 11 |
| S003 | 12 |
| S004 | 13 |
| S005 | 100 |""",
}


PANDAS_EXERCISE_REQUIREMENTS = {
    "01_series_dataframe": [
        "根据下方的 Markdown 表格创建 students DataFrame。",
        "分别取出 python 单列和多列结果，观察 Series 与 DataFrame 的区别。",
        "计算 Python 平均分，并筛选成绩不低于 85 分的完整记录。",
        "打印 type、shape、columns，并增加一名边界成绩为 85 分的学生。",
    ],
    "02_read_inspect": [
        "使用案例数据创建或读取 DataFrame，并查看前几行。",
        "分别检查 shape、columns、dtypes 和 info()。",
        "使用 describe() 解释数值字段的范围，并统计缺失值。",
        "增加一列缺失值，观察 head、info 和 describe 的变化。",
    ],
    "03_select_loc_iloc": [
        "根据下方的 Markdown 表格创建订单 DataFrame。",
        "使用 loc 筛选销售额大于 1000 的订单，并只保留 order_id、city、amount。",
        "使用 iloc 取前两行，比较 loc 与 iloc 的选择依据。",
        "打印结果类型和 shape，并增加一个没有符合条件订单的边界案例。",
    ],
    "04_filter_query": [
        "根据 Markdown 表格创建订单 DataFrame。",
        "分别使用 &、|、~、isin、between 和 query 完成条件筛选。",
        "为每种写法保留清晰的中间变量，比较结果是否一致。",
        "测试没有匹配行、刚好等于边界值和空城市集合的情况。",
    ],
    "05_modify_assign": [
        "根据 Markdown 表格创建订单 DataFrame。",
        "新增 amount 列，并使用 loc 按金额填写等级。",
        "至少比较直接赋值和 assign 两种新增列方式。",
        "使用 drop 删除临时列，并抽查一行验证金额公式。",
    ],
    "06_types_missing": [
        "根据下方的 Markdown 数据创建包含非法文本和缺失值的 DataFrame。",
        "使用 to_numeric(errors='coerce') 转换混合类型列。",
        "分别尝试 isna、dropna 和 fillna，并说明各自对行数或数值的影响。",
        "比较填补前后的缺失数量和统计结果，不要把缺失直接当成 0。",
    ],
    "07_duplicates_strings": [
        "根据下方的 Markdown 表格创建客户 DataFrame。",
        "使用 str.strip、lower 或 replace 统一文本格式。",
        "使用 duplicated 的不同 keep 参数观察重复标记，再用 drop_duplicates 去重。",
        "比较清洗前后的客户数量，并保留重复记录供复核。",
    ],
    "08_datetime": [
        "根据下方的 Markdown 数据创建日期 DataFrame，并转换为 datetime。",
        "使用 dt.year、dt.month、dt.day 和 dt.strftime 提取日期信息。",
        "计算日期差，并按月份统计或筛选日期范围。",
        "增加一个无效日期，比较 errors='coerce' 和默认报错行为。",
    ],
    "09_sort_groupby": [
        "根据下方的 Markdown 数据创建销售 DataFrame。",
        "使用单列、多列升降序排序，并用 nlargest 取前几名。",
        "使用 groupby.size 和 groupby.agg 计算订单数、总额和平均额。",
        "检查分组结果的样本量，并验证一个城市的总额。",
    ],
    "10_merge_concat": [
        "根据下方的 Markdown 数据创建 orders 和 customers 两张表。",
        "分别尝试 inner、left 和 outer merge，比较保留的订单。",
        "使用 indicator 找出未匹配记录，并用 validate 检查连接关系。",
        "使用 concat 按行和按列拼接，比较 axis 与 ignore_index 的效果。",
    ],
    "11_pivot_crosstab": [
        "根据下方的 Markdown 数据创建长格式销售 DataFrame。",
        "使用 pivot_table 指定 values、index、columns 和 aggfunc。",
        "使用 crosstab 统计频数，并比较 normalize 前后的结果。",
        "增加一个重复的城市与商品组合，观察 pivot 和 pivot_table 的区别。",
    ],
    "12_apply_transform": [
        "根据下方的 Markdown 数据创建分组成绩 DataFrame。",
        "使用 map 完成逐元素等级映射。",
        "使用 apply(axis=1) 完成逐行计算，并说明返回形状。",
        "使用 transform 生成组级指标，验证结果长度与原表一致。",
    ],
    "13_outliers_export": [
        "根据下方的 Markdown 数据创建金额 DataFrame。",
        "计算 Q1、Q3 和 IQR，并生成上下界。",
        "使用布尔列标记异常值，不要直接删除异常记录。",
        "使用 clip 对比截断效果，并把最终结果导出到 outputs。",
    ],
}


def pandas_exercises_for(item: Lesson) -> str:
    if item.slug == "01_series_dataframe":
        return '''"""动手练习：Series 与 DataFrame

业务任务：创建 students DataFrame，包含 name、class、math、python 四列；
再取出 python 成绩这一列，计算平均分，并筛选平均分不低于 85 的学生。

本题完成要求：
1. 根据 Markdown 表格创建 students DataFrame。
2. 分别取出 python 单列和多列结果，观察 Series 与 DataFrame 的区别。
3. 计算 Python 平均分，并筛选成绩不低于 85 分的完整记录。
4. 打印 type、shape、columns，并增加一名边界成绩为 85 分的学生。
"""

import pandas as pd


def main():
    # 案例数据（请自己把下面内容写成 pd.DataFrame）：
    # | name | class | math | python |
    # |---|---|---:|---:|
    # | 小林 | 一班 | 92 | 95 |
    # | 小周 | 一班 | 76 | 84 |
    # | 小陈 | 二班 | 85 | 90 |
    # | 小李 | 二班 | 68 | 75 |
    # TODO：根据上面的 Markdown 表格编写 students = pd.DataFrame(...)
    # TODO：取出 python 这一列，观察它是 Series 还是 DataFrame。
    # TODO：计算 python 平均分，并用条件筛选成绩不低于 85 的学生。
    # TODO：打印 type、shape 和筛选结果，验证自己的判断。
    pass


if __name__ == "__main__":
    main()
'''
    raw_case_data = PANDAS_EXERCISE_TABLES[item.slug]
    requirements = PANDAS_EXERCISE_REQUIREMENTS[item.slug]
    requirement_lines = "\n".join(
        f"{number}. {requirement}" for number, requirement in enumerate(requirements, 1)
    )
    prepared_data_comment = "\n".join(
        "    # " + line for line in raw_case_data.splitlines()
    )
    return f'''"""动手练习：{item.title}

业务任务：{item.exercise}

本题完成要求：
{requirement_lines}
"""

import pandas as pd


def main():
    # 下面只提供案例数据，不直接提供 DataFrame 代码。
    # 请先阅读并理解字段，再亲自把它写成 pd.DataFrame，这是本节练习的一部分。
    # 可以先运行你写出的数据，再增加一行、修改一个边界值，观察结果如何变化。
    # 案例数据：
{prepared_data_comment}
    # TODO：根据上面的数据，自己编写 pd.DataFrame(...)。
    # TODO：再使用 DataFrame 完成业务任务。
    # TODO：把每个关键步骤拆成清晰的中间变量。
    # TODO：运行后检查结果是否真的回答了业务问题。
    pass


if __name__ == "__main__":
    main()
'''


def pandas_answers_for(item: Lesson) -> str:
    if item.slug == "01_series_dataframe":
        return '''"""参考答案：Series 与 DataFrame"""

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
'''
    indented = "\n".join("    " + line if line else "" for line in item.code.rstrip().splitlines())
    return f'''"""参考答案：{item.title}

这份文件用于自我核对，不要求你写出完全相同的代码。
核对时请思考：如果输入为空、含缺失值或列名改变，代码需要怎样调整？
"""

import pandas as pd


def main():
    # 以下是本节核心操作的参考实现。
{indented}


if __name__ == "__main__":
    main()
'''


def write_text(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content.rstrip() + "\n", encoding="utf-8")


def migrate_legacy_names() -> None:
    """把第一版生成的无编号文件名迁移为可按字典序阅读的编号文件名。"""
    for course_dir in [ROOT / "01_python_core", ROOT / "02_data_analysis"]:
        if not course_dir.exists():
            continue
        for directory in sorted([course_dir, *[path for path in course_dir.rglob("*") if path.is_dir()]], key=lambda p: len(p.parts), reverse=True):
            mapping = None
            if (directory / "examples.py").exists():
                mapping = {"README.md": "00_lesson_legacy.md", "examples.py": "01_examples.py", "exercises.py": "02_exercises.py", "answers.py": "03_answers.py"}
            elif (directory / "main.py").exists():
                mapping = {"README.md": "01_project_guide.md", "main.py": "02_main.py"}
            elif directory.name in {"16_practice_projects", "06_practice_projects"}:
                mapping = {"README.md": "00_projects_overview.md"}
                stale = directory / "00_chapter_overview.md"
                if stale.exists():
                    stale.unlink()
            elif directory.name == "datasets":
                mapping = {"README.md": "00_dataset_guide.md"}
            elif directory.name == "outputs":
                mapping = {"README.md": "00_output_guide.md"}
            elif (directory / "README.md").exists():
                mapping = {"README.md": "00_course_overview.md" if directory == course_dir else "00_chapter_overview.md"}
            if mapping:
                for old_name, new_name in mapping.items():
                    old_path = directory / old_name
                    new_path = directory / new_name
                    if old_path.exists():
                        if new_path.exists():
                            # 新编号文件已经存在时，旧文件只是第一版生成的重复副本。
                            old_path.unlink()
                        else:
                            old_path.rename(new_path)
    for directory, old_name, new_name in [
        (ROOT / "03_other_libraries", "README.md", "00_library_plan.md"),
        (ROOT / "04_real_projects", "README.md", "00_projects_plan.md"),
    ]:
        old_path, new_path = directory / old_name, directory / new_name
        if old_path.exists() and not new_path.exists():
            old_path.rename(new_path)


def build_course(base: Path, title: str, chapters: dict[str, list[Lesson]]) -> tuple[int, int]:
    chapter_links: list[str] = []
    lesson_count = 0
    for chapter, lessons in chapters.items():
        chapter_dir = base / chapter
        chapter_title = chapter.split("_", 1)[1].replace("_", " ").title()
        rows = []
        for number, item in enumerate(lessons, 1):
            lesson_dir = chapter_dir / item.slug
            if title == "Python 数据分析" and chapter == "02_pandas":
                write_text(lesson_dir / "01_examples.py", pandas_examples_for(item))
                write_text(lesson_dir / "02_exercises.py", pandas_exercises_for(item))
                write_text(lesson_dir / "03_answers.py", pandas_answers_for(item))
            else:
                write_text(lesson_dir / "01_examples.py", '"""可运行示例：先预测结果，再执行。"""\n\n' + item.code)
                write_text(lesson_dir / "02_exercises.py", exercises_for(item))
                write_text(lesson_dir / "03_answers.py", answer_for(item))
            rows.append(f"{number}. [{item.title}]({item.slug}/01_examples.py)")
            lesson_count += 1
        if title == "Python 数据分析" and chapter == "02_pandas":
            intro = """# Pandas 学习路线：从表格对象到分析结果

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

"""
            write_text(chapter_dir / "00_chapter_overview.md", intro + "\n".join(rows))
        else:
            write_text(chapter_dir / "00_chapter_overview.md", f"# {chapter_title}\n\n按顺序学习：\n\n" + "\n".join(rows))
        chapter_links.append(f"- [{chapter}]({chapter}/00_chapter_overview.md) — {len(lessons)} 个知识点")
    write_text(base / "00_course_overview.md", f"# {title}\n\n本课程严格按目录编号学习。每节包含讲解、示例、练习和答案。\n\n" + "\n".join(chapter_links))
    return len(chapters), lesson_count


def build_datasets() -> None:
    datasets = ROOT / "02_data_analysis" / "datasets"
    write_text(datasets / "sales.csv", """order_id,date,city,product,category,price,quantity
S001,2026-01-03,上海,机械键盘,数码,399,2
S002,2026-01-05,北京,无线鼠标,数码,129,3
S003,2026-01-12,深圳,人体工学椅,家具,1299,1
S004,2026-02-02,上海,显示器,数码,1599,2
S005,2026-02-14,北京,书桌,家具,899,1
S006,2026-02-20,杭州,笔记本支架,配件,199,5
S007,2026-03-01,深圳,机械键盘,数码,399,4
S008,2026-03-08,上海,无线鼠标,数码,129,6
S009,2026-03-16,杭州,显示器,数码,1599,1
S010,2026-03-28,北京,笔记本支架,配件,199,3""")
    write_text(datasets / "students.csv", """student_id,name,gender,class,math,english,python
1001,小林,女,一班,92,88,95
1002,小周,男,一班,76,91,84
1003,小陈,女,二班,85,79,90
1004,小李,男,二班,68,72,75
1005,小王,女,一班,96,93,98
1006,小赵,男,二班,81,,87""")
    write_text(datasets / "00_dataset_guide.md", """# 本地练习数据

- `sales.csv`：订单、日期、城市、商品、分类、单价和数量。
- `students.csv`：学生基本信息和三科成绩，包含一个缺失值。

数据为教学用途的虚构小样本。练习时始终保留原文件，把清洗结果写入 `../outputs/`。
""")


def build_projects() -> None:
    core_projects = ROOT / "01_python_core" / "16_practice_projects"
    data_projects = ROOT / "02_data_analysis" / "06_practice_projects"
    core = [
        ("01_calculator", "命令行计算器", "函数、条件分支、异常处理"),
        ("02_todo_list", "待办事项管理器", "列表、字典、文件与 JSON"),
        ("03_contact_book", "通讯录", "函数、模块、搜索和持久化"),
        ("04_grade_system", "学生成绩管理系统", "面向对象、CSV、统计和测试"),
    ]
    data = [
        ("01_student_analysis", "学生成绩分析", "缺失值、描述统计、分组和分布图"),
        ("02_sales_analysis", "商品销售分析", "日期、透视表、趋势图和业务结论"),
        ("03_customer_analysis", "用户消费分析", "分层、异常值、关联和可视化"),
        ("04_complete_report", "完整数据分析报告", "从问题定义到可复现输出"),
    ]
    for base, items in [(core_projects, core), (data_projects, data)]:
        links = []
        for slug, title, focus in items:
            content = f"""# {title}

## 项目目标

独立完成一个可以重复运行的小项目，综合训练：{focus}。

## 实施顺序

1. 先把需求拆成输入、处理和输出。
2. 写出最小可运行版本。
3. 增加非法输入、空数据等边界处理。
4. 把重复逻辑拆成函数或类。
5. 添加测试，并在 README 记录运行方法。

## 验收标准

- 程序可以从 PyCharm 直接运行。
- 变量和函数命名清晰，关键逻辑有中文注释。
- 不覆盖原始数据；错误信息能指导用户修正输入。
- 至少包含三个测试场景和一段学习总结。
"""
            write_text(base / slug / "01_project_guide.md", content)
            write_text(base / slug / "02_main.py", f'''"""{title}：请按照 01_project_guide.md 逐步实现。"""\n\n\ndef main():\n    # TODO：先实现最小可运行版本。\n    print("项目：{title}")\n\n\nif __name__ == "__main__":\n    main()\n''')
            links.append(f"- [{title}]({slug}/01_project_guide.md) — {focus}")
        write_text(base / "00_projects_overview.md", "# 综合项目\n\n请完成前置课程后按顺序实践。\n\n" + "\n".join(links))
    core_index = ROOT / "01_python_core" / "00_course_overview.md"
    data_index = ROOT / "02_data_analysis" / "00_course_overview.md"
    write_text(
        core_index,
        core_index.read_text(encoding="utf-8")
        + "\n- [16_practice_projects](16_practice_projects/00_projects_overview.md) — 4 个综合项目\n",
    )
    write_text(
        data_index,
        data_index.read_text(encoding="utf-8")
        + "\n- [06_practice_projects](06_practice_projects/00_projects_overview.md) — 4 个数据分析项目\n"
        + "- [datasets](datasets/00_dataset_guide.md) — 无需联网的教学数据\n"
        + "- [outputs](outputs/00_output_guide.md) — 清洗结果、图表和报告输出位置\n",
    )


def build_root_files(core_stats: tuple[int, int], data_stats: tuple[int, int]) -> None:
    write_text(ROOT / "README.md", f"""# Python 学习工程

一套可以直接用 PyCharm 打开的中文 Python 学习资料，覆盖基础语法和数据分析。

## 学习顺序

1. [Python 基础语法](01_python_core/00_course_overview.md)：{core_stats[0]} 个章节，{core_stats[1]} 个细分知识点。
2. [Python 数据分析](02_data_analysis/00_course_overview.md)：{data_stats[0]} 个章节，{data_stats[1]} 个细分知识点。
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
""")
    write_text(ROOT / "requirements.txt", """numpy>=2.0
pandas>=2.2
matplotlib>=3.9
seaborn>=0.13
jupyter>=1.0
openpyxl>=3.1
pytest>=8.0""")
    write_text(ROOT / ".gitignore", """.venv/
__pycache__/
*.py[cod]
.idea/
.ipynb_checkpoints/
02_data_analysis/outputs/*
!02_data_analysis/outputs/00_output_guide.md
*.png
*.svg""")
    write_text(ROOT / "02_data_analysis" / "outputs" / "00_output_guide.md", "# 分析输出\n\n清洗后的表格、图片和报告放在这里，不要覆盖 datasets 中的原始数据。")
    write_text(ROOT / "03_other_libraries" / "00_library_plan.md", "# 其他 Python 库\n\n完成基础语法和数据分析后，可继续在这里按主题扩展第三方库。")
    write_text(ROOT / "04_real_projects" / "00_projects_plan.md", "# 大型实战项目\n\n用于未来跨多个库、包含完整工程结构的项目。")


def main() -> None:
    migrate_legacy_names()
    core_stats = build_course(ROOT / "01_python_core", "Python 基础语法", CORE)
    data_stats = build_course(ROOT / "02_data_analysis", "Python 数据分析", DATA)
    build_datasets()
    build_projects()
    build_root_files(core_stats, data_stats)
    print(f"生成完成：基础语法 {core_stats[1]} 节，数据分析 {data_stats[1]} 节。")


if __name__ == "__main__":
    main()

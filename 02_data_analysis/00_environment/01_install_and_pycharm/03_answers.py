"""安装依赖与配置 PyCharm：参考答案。

这份答案演示核心写法。练习任务通常还有其他正确实现；请重点比较思路。
"""


def main():
    # 先运行本答案，再逐行对照自己的实现。
    import importlib
    for package in ["numpy", "pandas", "matplotlib", "seaborn"]:
        module = importlib.import_module(package)
        print(package, module.__version__)


if __name__ == "__main__":
    main()

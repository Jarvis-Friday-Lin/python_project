"""PyCharm 调试与 logging：参考答案。

这份答案演示核心写法。练习任务通常还有其他正确实现；请重点比较思路。
"""


def main():
    # 先运行本答案，再逐行对照自己的实现。
    import logging
    logging.basicConfig(level=logging.INFO, format="%(levelname)s:%(message)s")
    values = [1, 2, 3]
    logging.info("开始处理，共 %d 项", len(values))
    for value in values:
        logging.debug("当前值=%s", value)
    logging.info("处理完成")


if __name__ == "__main__":
    main()

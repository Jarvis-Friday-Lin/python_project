"""可运行示例：先预测结果，再执行。"""

import logging
logging.basicConfig(level=logging.INFO, format="%(levelname)s:%(message)s")
values = [1, 2, 3]
logging.info("开始处理，共 %d 项", len(values))
for value in values:
    logging.debug("当前值=%s", value)
logging.info("处理完成")

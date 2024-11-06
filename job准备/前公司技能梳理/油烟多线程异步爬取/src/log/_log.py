import logging


class Logger:
    def __init__(self, log_filename):
        # 设置日志文件
        logging.basicConfig(filename=log_filename, level=logging.INFO,
                            format='[%(asctime)s] [%(name)s] - %(levelname)s - %(message)s',
                            datefmt='%Y-%m-%d %H:%M:%S',
                            encoding='utf-8')

    def get_logger(self):
        return logging.getLogger(__name__)


# 使用示例
if __name__ == '__main__':
    # 初始化日志工具类，并指定输出文件
    logger = Logger('my_log.log')
    # 获取日志器对象
    log = logger.get_logger()

    # 记录一条日志
    log.info('这是一条INFO级别的日志')
    log.warning('这是一条WARNING级别的日志')
    log.error('这是一条ERROR级别的日志')
    logging.info('hello')

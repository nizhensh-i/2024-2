
import time

from src.fume_spider_thread import FumeSpider
from src.request_.request_stable import _my_request_remote, request_update_cookie
from src.request_.request_test_data import _my_request_local
from src.util.remove_dup import RemoveDup
from src.config import config
from src.fume_sprder_asynic import download_many
from src.log._log import Logger
import logging
from src.fume_spider_thread import FumeSpider as thread_fume_spider


# 测试装饰器获取本地数据
def main():
    f_s = FumeSpider()

    # 装饰器请求本地网页
    fume_data = f_s.fetch(_my_request_local)

    logging.info(f'遍历完毕：结果为：fume_data:{fume_data}')
    logging.info(f'遍历完毕：长度为：{len(fume_data)}')

    # 去重
    removed_dup = RemoveDup.remove_duplicates_cls(fume_data)
    logging.info(f'去重后,结果为：removed_dup：{removed_dup}')
    logging.info(f'去重后：长度为：{len(removed_dup)}')

def local_spider():
    Logger('local_log.log')
    t0 = time.perf_counter()
    f = FumeSpider()
    r = f.fetch_many(config['development'].shop_name, _my_request_local)
    time_sum = time.perf_counter()-t0
    logging.info('数据总数为: %s', len(r))
    logging.info('总用时: %s', time_sum)

def order_spider():
    Logger('order_log.log')
    request_update_cookie(config['development'].cookies)
    t0 = time.perf_counter()
    f = FumeSpider()
    r = f.fetch_many(config['development'].shop_name, _my_request_remote)
    time_sum = time.perf_counter() - t0
    logging.info('数据总数为: %s', len(r))
    logging.info('总用时: %s', time_sum)


def thread_spider():
    Logger('thread_log.log')
    request_update_cookie(config['development'].cookies)
    t0 = time.perf_counter()
    f = thread_fume_spider()
    r = f.fetch_many_thread(config['development'].shop_name, _my_request_remote)
    time_sum = time.perf_counter() - t0
    logging.info('数据总数为: %s', len(r))
    logging.info('总用时: %s', time_sum)


def async_spider():
    Logger('async_log.log')
    t0 = time.perf_counter()
    r = download_many(config['development'].shop_name)
    time_sum = time.perf_counter() - t0
    logging.info('数据总数为: %s', len(r))
    logging.info('总用时: %s', time_sum)


if __name__ == '__main__':

    local_spider()

    # 1320条数据
    # order_spider()

    # 1300条  1320 1320条 1320条
    # thread_spider()

    # 1020条 0条 1020条 1020条 1020条
    # async_spider()
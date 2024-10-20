# from src.fume_spider import FumeSpider
import random
import time

from src.fume_spider_thread import FumeSpider
from src.request_.request_stable import _my_request_remote, request_update_cookie
from src.request_.request_test_data import _my_request_local
from src.util.remove_dup import RemoveDup
from src.config import config
from src.fume_sprder_asynic import download_many
from src.log._log import Logger
import logging

# 测试装饰器获取本地数据
def main():
    f_s = FumeSpider()

    # 装饰器请求本地网页
    fume_data = f_s.fetch(_my_request_local)

    print(f'遍历完毕：结果为：fume_data:{fume_data}')
    print(f'遍历完毕：长度为：{len(fume_data)}')

    # 去重
    removed_dup = RemoveDup.remove_duplicates_cls(fume_data)
    print(f'去重后,结果为：removed_dup：{removed_dup}')
    print(f'去重后：长度为：{len(removed_dup)}')


if __name__ == '__main__':
    Logger('my_log.log')

    # 本地环境
    # local_fume_page = LocalFumePage()
    # t0 = time.perf_counter()
    # f = FumeSpider()
    # r = f.fetch_many(config['development'].shop_name, local_fume_page)
    # time_sum = time.perf_counter()-t0
    # print('总用时：', time_sum)

    # 远程请求
    # request_update_cookie(config['development'].cookies)
    # t0 = time.perf_counter()
    # f = FumeSpider()
    # r = f.fetch_many(config['development'].shop_name, _my_request_remote)
    # print('数据总数为：', len(r))
    # time_sum = time.perf_counter() - t0
    # print('总用时：', time_sum)


    # 初始化日志工具类，并指定输出文件
    t0 = time.perf_counter()
    r = download_many(config['development'].shop_name)
    print(len(r))
    time_sum = time.perf_counter() - t0
    print('总用时：', time_sum)


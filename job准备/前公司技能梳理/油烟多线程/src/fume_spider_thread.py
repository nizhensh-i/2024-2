import logging
import time
from concurrent import futures

from requests import HTTPError, Timeout, ConnectionError, RequestException
from .get_web_page import FumeWebPage
from .config import config
from src.request_.request_test_data import LocalFumePage
from .util.generate_url import GenerateUrl
import tqdm
from .survey.extract import Extract


# def fetch(url: str, page: FumeWebPage):
#     try:
#         r = page.get_page(url)
#     except ConnectionError as e:
#         print('网络连接异常: ', e)
#     except Timeout as e:
#         print('连接超时: ', e)
#     except HTTPError as e:
#         print(f'HTTP错误, 状态码: {e.response.status_code}, {e}')
#     except RequestException as e:
#         print('请求异常: ', e)
#     except ValueError as e:
#         print('响应解析异常: ', e)
#     return r

def fetch(url: str, page: FumeWebPage):
    try:
        r = page.get_page(url)
        return r
    except (ConnectionError, Timeout, HTTPError, RequestException) as e:
        print(f'Error fetching {url}: {e}')
        return None
class FumeSpider:

    # 多线程
    def fetch_many_thread(self, shops, page):
        shop_url = GenerateUrl.generate_url(shops)
        print(f'url:{shop_url}')
        all_url = []
        for shop, urls in shop_url.items():
            all_url = all_url + urls
        print(all_url)
        print(f'url长度为:{len(all_url)}')

        # ThreadPoolExecutor.map 的实践
        # with futures.ThreadPoolExecutor() as executor:
        #     r = executor.map(fetch, all_url)
        # for i in r:
        #     print(i)

        # 进度条
        task_list = []

        # 爬取的html
        fume_data = []

        with futures.ThreadPoolExecutor() as executor:
            for url in all_url:
                res = executor.submit(fetch, url, page)
                task_list.append(res)

            done_iter = tqdm.tqdm(futures.as_completed(task_list), total=len(all_url))
            for future in done_iter:
                html = future.result()
                # 数据提取
                fume_sum = Extract.extract_from_html(html)
                fume_data += fume_sum
                # time.sleep(config['development'].delay_start)
        return fume_data

    # 顺序执行
    def fetch_many(self, shops, page):
        shop_url = GenerateUrl.generate_url(shops)
        print(f'url:{shop_url}')
        all_url = []
        for shop, urls in shop_url.items():
            all_url = all_url + urls
        print(all_url)
        print(f'url长度为:{len(all_url)}')

        # 爬取的html
        fume_data = []
        for url in all_url:
            html = fetch(url, page)
            # 数据提取
            fume_sum = Extract.extract_from_html(html)
            fume_data += fume_sum
        return fume_data


if __name__ == '__main__':
    f = FumeSpider()
    f.fetch_many(config['development'].shop_name)

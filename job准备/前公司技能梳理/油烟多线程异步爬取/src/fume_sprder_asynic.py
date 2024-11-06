import asyncio
import requests
from httpx import AsyncClient

from src.survey.extract import Extract
from src.util.generate_url import GenerateUrl
from src.config import config
import logging
from src.log._log import Logger
import time

con_req = 3

async def download_one(client: AsyncClient, cc: str, queue, semaphore):
    async with semaphore:
        html = await get_fume(client, cc)
    r = Extract.extract_from_html(html)
    queue += r


async def get_fume(client: AsyncClient, url: str) -> bytes:
    try:
        # 发起异步HTTP请求
        resp = await client.get(url, follow_redirects=True)
        # 确保响应状态码是200
        if resp.status_code == 200:
            return resp.text  # 返回响应的文本内容
        else:
            # 如果不是200状态码，可以在这里处理错误或重定向
            # 例如，可以记录日志或抛出异常
            raise Exception(f"Received non-200 status code: {resp.status_code}")
    except requests.exceptions.RequestException as e:
        # 捕获并处理请求异常，例如网络问题、连接问题等
        logging.error(f"Request failed: {e}")
        # 根据需要决定是否重新尝试或返回None或其他值
        return ''
    except Exception as e:
        # 捕获其他可能的异常
        logging.error(f"An unexpected error occurred: {e}")
        # 根据需要决定是否重新尝试或返回None或其他值
        return ''


def download_many(shops: list[str]) -> int:
    shop_url = GenerateUrl.generate_url(shops)
    print(f'url:{shop_url}')
    all_url = []
    for shop, urls in shop_url.items():
        all_url = all_url + urls
    print(all_url)
    print(f'url长度为:{len(all_url)}')
    return asyncio.run(supervisor(all_url))


async def supervisor(cc_list: list[str]) -> int:
    sem = asyncio.Semaphore(con_req)
    queue = []
    async with AsyncClient() as client:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
            "sec-ch-ua": "'Google Chrome';v='129', 'Not=A?Brand';v='8', 'Chromium';v='129'",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "'Windows'",
            "upgrade-insecure-requests": "1"}
        cookies_dict = dict(pair.split('=') for pair in config['development'].cookies.split('; '))
        client.cookies.update(cookies_dict)
        client.headers.update(headers)
        to_do = [download_one(client, cc, queue, sem) for cc in cc_list]
        await asyncio.gather(*to_do)
    print("队列长度", len(queue))
    return queue


if __name__ == '__main__':
    Logger('my_log.log')
    t0 = time.perf_counter()
    r = download_many(config['development'].shop_name)
    print(len(r))
    time_sum = time.perf_counter() - t0
    print('总用时：', time_sum)

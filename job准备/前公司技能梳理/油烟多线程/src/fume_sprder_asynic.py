import asyncio
import requests
from httpx import AsyncClient

from src.survey.extract import Extract
from src.util.generate_url import GenerateUrl
from src.config import config
import logging
from src.log._log import Logger
import time

async def download_one(client: AsyncClient, cc: str, queue):
    html = await get_fume(client, cc)
    await queue.put(html)


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
    finally:
        await asyncio.sleep(0.5)


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
    queue = asyncio.Queue()
    async with AsyncClient() as client:
        cookies_dict = dict(pair.split('=') for pair in config['development'].cookies.split('; '))
        client.cookies.update(cookies_dict)
        to_do = [download_one(client, cc, queue) for cc in cc_list]
        await asyncio.gather(*to_do)
    f = []
    while not queue.empty():
        item = await queue.get()
        # 处理数据
        r = Extract.extract_from_html(item)
        f += r
    return f

if __name__ == '__main__':
    Logger('my_log.log')
    t0 = time.perf_counter()
    r = download_many(config['development'].shop_name)
    print(len(r))
    time_sum = time.perf_counter() - t0
    print('总用时：', time_sum)


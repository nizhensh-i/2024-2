import asyncio
import requests
from httpx import AsyncClient
from src.survey.extract import Extract
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
    base_url = 'http://quotes.toscrape.com/page/'
    all_url = []
    for number in range(20):
        all_url.append(base_url + f'{number}/')
    print(all_url)
    print(f'url长度为:{len(all_url)}')
    return asyncio.run(supervisor(all_url))


async def supervisor(cc_list: list[str]) -> int:
    queue = asyncio.Queue()
    async with AsyncClient() as client:
        to_do = [download_one(client, cc, queue) for cc in cc_list]
        await asyncio.gather(*to_do)
    f = []
    while not queue.empty():
        html = await queue.get()
        quotes = Extract.extract_quotes(html)
        logging.info('%s',quotes)
        # 处理数据
        f.append(quotes)
    print(f)
    return f



if __name__ == '__main__':
    Logger('my_log.log')
    t0 = time.perf_counter()
    r = download_many('')
    print(len(r))
    time_sum = time.perf_counter() - t0
    print('总用时：', time_sum)


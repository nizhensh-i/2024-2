import asyncio
import time

import requests
from httpx import AsyncClient

import logging
from src.log._log import Logger
from pathlib import Path


POP20_CC = ('CN IN US ID BR PK NG BD RU JP '
            'MX PH VN ET EG DE IR TR CD FR').split()  # <2>

BASE_URL = 'http://localhost:8000/flags'
DEST_DIR = Path('downloaded')


async def download_one(client: AsyncClient, cc: str, queue):
    image = await get_fume(client, cc)
    await queue.put(image)
    return cc


def save_flag(img: bytes, filename: str) -> None:  # <5>
    (DEST_DIR / filename).write_bytes(img)


async def get_fume(client: AsyncClient, cc: str) -> bytes:
    try:
        url = f'{BASE_URL}/{cc}/{cc}.gif'.lower()
        # 发起异步HTTP请求
        resp = await client.get(url, follow_redirects=True)
        # 确保响应状态码是200
        if resp.status_code == 200:
            return resp.content  # 返回响应的文本内容
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


def download_many() -> int:
    return asyncio.run(supervisor(POP20_CC))


async def supervisor(cc_list: list[str]) -> int:
    queue = asyncio.Queue()
    async with AsyncClient() as client:
        to_do = [download_one(client, cc, queue) for cc in cc_list]
        res = await asyncio.gather(*to_do)
    i = 0
    while not queue.empty():
        image = await queue.get()
        # 保存图像
        save_flag(image, f'{i}.gif')
        i = i + 1
    return len(res)


if __name__ == '__main__':
    Logger('my_log.log')
    t0 = time.perf_counter()
    DEST_DIR.mkdir(exist_ok=True)
    r = download_many()
    print(r)
    time_sum = time.perf_counter() - t0
    print('总用时：', time_sum)


from .url.url_parser import Url
from .login import *
from requests import HTTPError,Timeout,ConnectionError,RequestException
from .get_web_page import FumeWebPage
from .decorator.loop import loop_get_data_by_shop
from .config import config
from .decorator.sleep import DelayedStart

class FumeSpider:
    # 第一个参数url 自动由装饰器@loop_get_data_by_shop 提供，无需传递
    @loop_get_data_by_shop(shops=config['development'].shop_name)
    @DelayedStart(seconds=config['development'].delay_start)
    def fetch(self, url: str, page: FumeWebPage):
        try:
            r = page.get_page(url)
        except ConnectionError as e:
            print('网络连接异常: ', e)
        except Timeout as e:
            print('连接超时: ', e)
        except HTTPError as e:
            print(f'HTTP错误, 状态码: {e.response.status_code}, {e}')
        except RequestException as e:
            print('请求异常: ', e)
        except ValueError as e:
            print('响应解析异常: ', e)
        return r



if __name__ == '__main__':
    # 登录
    login_fume_web()
    u = Url()
    urls = u.concatenate_url_with_condition('杨记齐齐哈尔烤肉','2023-10-01','2023-10-31',1)
    f_s = FumeSpider()
    for item in urls:
        f_s.fetch(item)
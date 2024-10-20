import requests
import urllib3


class RemoteFumePage:
    def __init__(self):
        urllib3.disable_warnings()
        self.session = requests.session()
        self.session.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
        }

    def post(self, url: str, params: dict):
        """post请求

        Args:
            url (str): 目标url
            params (dict): 请求参数

        Returns:
            _type_: 响应内容
        """
        r = self.session.post(url, data=params, verify=False, timeout=10)
        if r.status_code != 200:
            return False
        return r

    def get(self, url: str):
        """get请求

        Args:
            url (str): 目标url

        Returns:
            _type_: 响应内容
        """
        r = self.session.get(url, verify=False)
        if r.status_code != 200:
            return False
        return r

    def update_cookie(self, cookie_str: str):
        print('cookie为：', cookie_str)
        # 将Cookie字符串解析为字典
        cookies_dict = dict(pair.split('=') for pair in cookie_str.split('; '))

        # 将Cookie字典添加到会话中
        self.session.cookies.update(cookies_dict)


_my_request = RemoteFumePage()
request_post = _my_request.post
request_get = _my_request.get
request_update_cookie = _my_request.update_cookie

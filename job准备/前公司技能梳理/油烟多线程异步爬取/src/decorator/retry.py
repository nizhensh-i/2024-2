import wrapt
import time


class Retry:

    def __init__(self,retry_num: int):
        self.retry_num = retry_num

    @wrapt.decorator
    def __call__(self, wrapped, instance, args, kwargs):
        for i in range(self.retry_num):
            try:
                r = wrapped(*args, **kwargs)
                break
            except ConnectionError as c:
                if (i+1) == self.retry_num:
                    print('达到最大重试次数...稍后重试')
                    raise
                else:
                    print('请求失败..等待30s后重试')
                    time.sleep(30)
        return r


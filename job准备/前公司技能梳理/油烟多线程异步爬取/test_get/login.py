import time
import json
import base64
from src.config import config
from test_get.request_stable import request_get, request_post


def get_time():
    # 毫秒妙级时间戳 13位数字
    now_time = str(int(time.time() * 1000))
    return now_time


def get_photo_url(url):
    return url + get_time()


def base64_api(img):
    # 返回账号密码
    uname, pwd = config['development'].verification_code_account, config['development'].verification_code_password
    with open(img, 'rb') as f:
        base64_data = base64.b64encode(f.read())
        b64 = base64_data.decode()
    data = {"username": uname, "password": pwd, "typeid": 2, "image": b64}
    # result = json.loads(request_post("http://api.ttshitu.com/predict", data))
    result = json.loads(request_post("http://api.ttshitu.com/predict", data).text)
    if result['success']:
        return result["data"]["result"]
    else:
        # ！！！！！！！注意：返回 人工不足等 错误情况 请加逻辑处理防止脚本卡死 继续重新 识别
        return result["message"]
    return ""


# zk123 fyhb123
def login_fume_web():
    # 请求验证码地址
    # 构造时间戳
    # 拼接url
    # 识别验证码
    url_photo = get_photo_url('http://xhhb.senzly.cn/servlet/Vcode_new.serv?t=')
    response = request_get(url_photo)
    # response = request_get(url_photo)         # 图片为二进制数据
    image_data = response.content
    with open('Vcode.jpg', mode='wb') as f:
        f.write(image_data)
    # 验证码结果
    v_code_result = base64_api('Vcode.jpg')
    print(v_code_result)
    play_load = {
        "account": "9SUBjEeNy7nFMzk123",
        "password": "6SUBIyusanb170e13a221a4cb58c66876006488504",
        "vcode": v_code_result
    }

    url_jump = 'http://xhhb.senzly.cn/cusLogin.php'
    r = request_post(url_jump, play_load)
    print(r.text)
    print('登录成功')

    # return session
    # 个人验证
    tartget = 'https://xhhb.senzly.cn/sys/yyRealTimeValue_list.jsp'
    r = request_get(tartget)
    print(f'跳转地址为：{r.text}')

    shop_url = 'http://xhhb.senzly.cn/sys/yyRealTimeValue_list.jsp?key1=&shop=%25E5%2590%2589%25E5%2588%25BB%25E8%2581%2594%25E7%259B%259F&pagesize=100&key5=2024-7-18&key6=2024-7-19&page=1'
    r = request_get(shop_url)
    print(f'店铺数据为：{r.text}')

if __name__ == '__main__':
    login_fume_web()



class Config:
    # 爬取参数
    # shop_name = ['吉刻联盟','大成海鲜','大肆撸串','天钥小馆','弄堂咪道','杨记齐齐哈','棒约翰','狼来了','缘家','食其家','馨远美食小镇（哈尼美食广场）']
    shop_name = ['棒约翰']
    begin_date = '2024-7-1'
    end_date = '2024-7-20'
    page_size = 100
    page_num = 14

    # 请求间隔秒
    delay_start = 0.2

    # 数据库
    ip = 'localhost'
    user = 'root'
    password = '1234'
    port = 3306
    data_base_name = 're_conganize_fume'

    # 验证码平台
    verification_code_account = '191259'
    verification_code_password = 'zsc654321'

    cookies = 'SECKEY_ABVK=QmrbR1Q4HE8b9xfvCg0wED9BgSusZ2yUc2sM5YWr0XBNL3X2hXSUa5I4Tnr8vnATupGRdKLM5OuIXmL3mYFejA%3D%3D; BMAP_SECKEY=QmrbR1Q4HE8b9xfvCg0wED9BgSusZ2yUc2sM5YWr0XDOWhPHuC2UKWL9sFAEUA504L8hUEF_7KT7xJkx_xWByaH1db7w4nuiKyPNyXg_7axH5ROcoGW-LVw0U5vYh8kNA45L9ObKiMwQjGDtiVd9v2Ncxt1cXIESjclielz4KcNKWbRPi8IV82sfEFhb5ezyTHgxc0lDnB0gn0DWRDYHdA; JSESSIONID=35949E4856C77159767E74AF93926F0F'

    # 并发量
    con_req = 3
    def __init__(self):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URL = f"mysql+pymysql://{Config.user}:{Config.password}@{Config.ip}:{Config.port}/{Config.data_base_name}?charset=utf8"

class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URL = f"mysql+pymysql://{Config.user}:{Config.password}@{Config.ip}:{Config.port}/{Config.data_base_name}?charset=utf8"

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URL = None


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'product': ProductionConfig,
    'default': DevelopmentConfig
}

if __name__ == '__main__':
    print(DevelopmentConfig.SQLALCHEMY_DATABASE_URL)
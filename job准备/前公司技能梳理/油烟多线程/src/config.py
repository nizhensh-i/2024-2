

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

    cookies = 'BMAP_SECKEY=Tss_ySlqtuBjMMLAdWsXQkhvu_2DnvUXQ-Jj47ZJKMSHaClqJCESAHkwAuk5chLhERAON0bBDST7AzRmzL7BBHE4yK0Ftwfz0fDDoDcAxH9xfGdpkU3WhlqMiLXHDoMelx39L3iCYFWrq-gniiP74MX0Iyz2cusHfiEtHJP3z4DRT96KDJZ3wybHY_Chl33cI0Li_SQ4G3bef2GkPQU_Pw; SECKEY_ABVK=Tss/ySlqtuBjMMLAdWsXQkhvu/2DnvUXQ+Jj47ZJKMS7oA+oq+o/XVi/mdzJRWmaRkZD0a7+pSuZh56V56hVGw%3D%3D; JSESSIONID=0967A08DC75803C2FCB949A51A9C4B6F'


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
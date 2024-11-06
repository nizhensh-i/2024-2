from test_get.login import login_fume_web
from test_get.request_stable import request_get, request_post,request_update_cookie

if __name__ == '__main__':
    # login_fume_web()

    # url = ['http://xhhb.senzly.cn/sys/yyRealTimeValue_list.jsp?key1=&shop=%25E5%2590%2589%25E5%2588%25BB%25E8%2581%2594%25E7%259B%259F&pagesize=100&key5=2024-7-18&key6=2024-7-19&page=1', 'http://xhhb.senzly.cn/sys/yyRealTimeValue_list.jsp?key1=&shop=%25E5%2590%2589%25E5%2588%25BB%25E8%2581%2594%25E7%259B%259F&pagesize=100&key5=2024-7-18&key6=2024-7-19&page=2']
    cookies = 'SECKEY_ABVK=Tss/ySlqtuBjMMLAdWsXQkhvu/2DnvUXQ+Jj47ZJKMRCWAaYsgJdoxmeWn1G+jgzxrMCVqQm9Y7Aiw4L8DcjFA%3D%3D; BMAP_SECKEY=Tss_ySlqtuBjMMLAdWsXQkhvu_2DnvUXQ-Jj47ZJKMSHaClqJCESAHkwAuk5chLhYnXmONgAlYFuOfyHfz7-m_wRoVH0VFXT6DHYTwRpM5LvDQ6o5IXSEKDzaWr0cqr7qaHt55fy8oWgOEYdZIDX31TOxjz8P90Dk33NL_q2tDPI9WaGOi6zm1SruIuPyuLVhjoIaS2PJ71lFggFQLhcv_W5iPMlnn9VfBM9qkWXY6o; JSESSIONID=731B2139D24F5905A183FF62B70F8164'
    request_update_cookie(cookies)
    url = 'http://xhhb.senzly.cn/sys/yyRealTimeValue_list.jsp?key1=&shop=%25E5%2590%2589%25E5%2588%25BB%25E8%2581%2594%25E7%259B%259F&pagesize=100&key5=2024-7-18&key6=2024-7-19&page=1'
    r = request_get(url)
    print(r.text)



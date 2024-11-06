from ..model.fume import Fume
from bs4 import BeautifulSoup as bs
import logging


class Extract:
    # 从HTML中提取需要的数据

    # 日志详细记录
    @staticmethod
    def extract_from_html(html: str) -> list[Fume]:
        soup = bs(html, 'html.parser')
        logging.info('开始解析 HTML 内容')
        # 找到所有的 tr 标签
        rows = soup.find_all('tr')
        logging.info(f'找到 {len(rows)} 个 tr 标签')

        # 提取表格中的数据
        result = []
        for row in rows[1:]:  # 跳过标题行
            data = []
            cols = row.find_all('td')
            # logging.info(f'当前行有 {len(cols)} 个 td 标签')
            for col in cols:
                if col.find('div'):
                    div_content = col.find('div').text.strip()
                    # logging.info(f'在 td 中找到 div，内容为: {div_content}')
                    # 返回元素的文本内容 搜索tag的直接子节点
                    td_content = ''.join(col.find_all(text=True, recursive=False)).strip()
                    data.append(td_content)
                    data.append(div_content)
                else:
                    td_content = col.text.strip()
                    data.append(td_content)

            # 删除不必要的内容
            del (data[-2:])
            del (data[2])

            # 创建 Fume 对象并添加到结果列表中
            result.append(
                Fume(MV_Stat_Code=data[2], MV_Create_Time=data[-1], MV_Data_Time=data[-2], MV_Fan_Electricity=data[6],
                     MV_Purifier_Electricity=data[7], MV_Fume_Concentration=data[4], MV_Fume_Concentration2=data[5]))

        logging.info('完成解析 HTML 内容\n')
        return result

    @staticmethod
    def extract_quotes(html):
        # 使用BeautifulSoup解析HTML
        soup = bs(html, 'html.parser')

        # 查找所有的名言div
        quote_divs = soup.find_all('div', class_='quote')

        # 提取名言
        quotes = []
        for div in quote_divs:
            quote = div.find('span', class_='text').get_text(strip=True)
            quotes.append(quote)

        return quotes

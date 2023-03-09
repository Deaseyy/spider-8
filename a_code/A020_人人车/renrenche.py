import re
from io import BytesIO

import requests
from fontTools.ttLib import TTFont
from lxml import etree

from utils.ut import compile_js


class RRC:
    def __init__(self):
        self.headers = {
            "Host": "www.renrenche.com",
            "Pragma": "no-cache",
            "Referer": "https://www.renrenche.com/bj/ershouche/p2/?&plog_id=2c4ed6bbfb48e60ea77985f173880562",
            # "Referer": "https://www.renrenche.com/bj/ershouche/p3/?&plog_id=d229997704294afe87e8d8c2039b8d4d",
            "sec-ch-ua": "\"Google Chrome\";v=\"105\", \"Not)A;Brand\";v=\"8\", \"Chromium\";v=\"105\"",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "\"Windows\"",
            "Sec-Fetch-Dest": "document",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-Site": "same-origin",
            "Sec-Fetch-User": "?1",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"

            # 'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Mobile Safari/537.36'
        }
        self.url = 'https://www.renrenche.com/bj/ershouche/p2/?&plog_id=2c4ed6bbfb48e60ea77985f173880562'
        # self.url = 'https://www.renrenche.com/bj/ershouche/p3/?&plog_id=d229997704294afe87e8d8c2039b8d4d'

    def req1(self):
        """首次请求, 返回一段js,用于计算acw_sc__v2"""
        resp = requests.get(self.url, headers=self.headers)
        print('====================== 首次请求 ===================================')
        resp.encoding = 'utf-8' if resp.encoding == 'ISO-8859-1' else resp.encoding
        print(resp.text)
        acw_tc = resp.cookies.get('acw_tc')
        arg1 = re.findall("var arg1=\'(.*?)\';", resp.text)[0]
        # print(arg1)
        exe = compile_js('renrenche.js')
        acw_sc__v2 = exe.call('get_acw_sc__v2', arg1)
        cookies = {
            'acw_tc': acw_tc,
            'acw_sc__v2': acw_sc__v2
        }
        return cookies

    def req2(self, cookies):
        """再次请求，携带cookie: acw_tc, acw_sc__v2, 返回正常数据"""
        resp = requests.get(self.url, headers=self.headers, cookies=cookies)
        print('====================== 再次请求 ===================================')
        resp.encoding = 'utf-8' if resp.encoding == 'ISO-8859-1' else resp.encoding
        print(resp.text)
        # 老是出现滑块验证，先写入html文件再分析
        with open('req2_res.html', 'w', encoding='utf-8') as f:
            f.write(resp.text)
        return resp.text

    def get_font(self, html):
        """获取字体对应关系"""
        font_url = re.findall("url\('(.*\.woff)'\)", html)[0]
        resp = requests.get(font_url)
        # # 保存到文件，以便分析字体关系
        # with open('file.woff', 'wb') as f:
        #     f.write(resp.content)
        wff_data = BytesIO(resp.content)
        font = TTFont(wff_data)
        cmap = font.get("cmap").getBestCmap()
        print('cmap: ', cmap)
        value_list = font.getGlyphOrder()[1:]  # 多了个 '.notdef',
        print('value固定顺序：', value_list)
        new_cmap = {v: chr(k) for k, v in cmap.items()}
        print('k-v映射：', new_cmap)
        map_list = [new_cmap[v] for v in value_list]
        print('value翻译值顺序：', map_list)
        font_dict = dict(zip(new_cmap.values(), map_list))
        return font_dict

    def get_data(self, html, font_dict):
        html = etree.HTML(html)
        lis = html.xpath('//div[@id="search_list_wrapper"]//ul/li')
        # 网页40条，li元素得到43条，有数据的有42条
        n = 0
        for li in lis:
            n+=1
            try:
                # print(n)
                title = li.xpath('.//h3/text()')[0]  # 是个 E对象，可以使用str的所有方法，可以使用title() 取str，
                ok_title = ''.join([i if not i.isdigit() else font_dict[i] for i in title])
                price = li.xpath('.//div[@class="price"]/text()')[0].strip()
                price_unit = li.xpath('.//div[@class="price"]/span/text()')[0]
                year_mileage = li.xpath('.//div[@class="mileage"]/span/text()')
                ok_year = ''.join([i if not i.isdigit() else font_dict[i] for i in year_mileage[0]])
                ok_mileage = ''.join([i if not i.isdigit() else font_dict[i] for i in year_mileage[1].strip()])
                print(ok_title, price, price_unit, ok_year, ok_mileage)
            except Exception as e:
                print('错误：', e)  # 第43个li元素取不到数据


if __name__ == '__main__':
    rrc = RRC()
    cookies = rrc.req1()
    html = rrc.req2(cookies)

    # # 老是出验证码，先使用已返回的正常数据进行调试
    # with open('req2_res_OK.html', 'r', encoding='utf-8') as f:
    #     html = f.read()

    # 注意：字体文件隔一段时间貌似会更新，导致解析的数据还是错误的
    font_dict = rrc.get_font(html)
    rrc.get_data(html, font_dict)



    # print(chr(57))
    # print(ord())


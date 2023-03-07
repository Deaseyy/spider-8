import re

from fontTools.ttLib import TTFont
from lxml import etree

import requests


class Sxs():
    def __init__(self):
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36"
        }

    def get_html(self):
        # 第1步：获取html，且存为html文件以便后面研究使用
        # url = 'https://www.shixiseng.com/interns?keyword=%E4%BA%A7%E5%93%81&city=%E5%85%A8%E5%9B%BD&type=intern&from=menu'
        url = 'https://www.shixiseng.com/interns?keyword=python&city=%E5%85%A8%E5%9B%BD&type=intern'
        res = requests.get(url=url, headers=self.headers).text
        with open('interns.html', 'w', encoding='utf8') as f:
            f.write(res)
        return res

    def get_font(self, html):
        # 第2步：下载html配套的字体ttf文件
        font_url = re.findall('src: url\((.*?)\);', html)
        f_url = 'https://www.shixiseng.com' + font_url[0] if font_url else font_url
        resp = requests.get(f_url)
        font_content = resp.content
        with open('file.woff', 'wb') as f:
            f.write(font_content)

    def get_font_map(self, ttf):
        # 第3步：提取ttf中映射的数据
        font_dict = {}
        # font = TTFont("file.woff")
        font = TTFont(ttf)
        cmap = font.get("cmap").getBestCmap()
        for k, v in cmap.items():
            if v[3:]:  # 默认标记 uni   默认3位
                content = "\\u00" + v[3:] if len(v[3:]) == 2 else "\\u" + v[3:]  # uni51  \\u0051   uni4E00 \\u4E00
                real_content = content.encode('utf-8').decode('unicode_escape')
                k_hex = hex(k)
                # 网页返回的字体是以&#x开头  ，换成以这个开头，下面代码就是直接替换
                real_k = k_hex.replace("0x", "&#x")
                font_dict[real_k] = real_content
        return font_dict

    def put_html(self, html, ttf_dict):
        # 第4步：对下载（HTML内容）进行映射替换
        for k, v in ttf_dict.items():
            html = html.replace(k, v)
        return html

    def get_data(self, html):
        html = etree.HTML(html)
        li_list = html.xpath("//div[@class='intern-wrap intern-item']")
        for li in li_list:
            title = "".join(li.xpath(".//div[@class='f-l intern-detail__job']//a/text()")[0].split())
            price = "".join(
                li.xpath(".//div[@class='f-l intern-detail__job']//span[@class='day font']/text()")[0].split())
            name = li.xpath('.//a[@class="title ellipsis"]/text()')[0]
            print(title, price, name)

    def main(self):
        # 第1步：获取html，且存为html文件以便后面研究使用
        html = self.get_html()
        # 第2步：下载html配套的ttf文件
        self.get_font(html)
        # 第3步：提取ttf中映射的数据
        font_dict = self.get_font_map('file.woff')
        # 第4步：对下载（HTML内容）进行替换
        html = self.put_html(html, font_dict)
        # 第5步：使用xpath提取想要的数据
        self.get_data(html)


if __name__ == '__main__':
    Sxs().main()

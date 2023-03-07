import re

import requests

from utils.ut import compile_js


class RRC:
    def __init__(self):
        self.headers = {
            'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Mobile Safari/537.36'
        }
        self.url = 'https://www.renrenche.com/bj/ershouche/p3/?&plog_id=6a544c539cc2f6d011e8588b6fae941c'

    def req1(self):
        """首次请求, 返回一段js,用于计算acw_sc__v2"""
        resp = requests.get(self.url, headers=self.headers)
        print('====================== 首次请求 ===================================')
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
        print(resp.text)


if __name__ == '__main__':
    rrc = RRC()
    cookies = rrc.req1()
    rrc.req2(cookies)


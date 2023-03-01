import json
import re

import requests
import execjs


# 32e09969994b58ea31c79792d4e209bd
# 1676646032.282|0|sFT5ir6%2FLjP0ldIr3KVgK%2B%2B96%2Bk%3D


url = 'https://www.mps.gov.cn/n2254098/n4904352/index.html'

def first_get():
    """code 521"""
    headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Mobile Safari/537.36"
    }
    resp = requests.get(url, headers=headers)
    print('首次响应数据：', resp.text)
    __jsluid_s = resp.cookies.get('__jsluid_s')

    js_code = re.findall('document.cookie=(.*?);location.href', resp.text)[0]
    jsl_cle_text = execjs.eval(js_code).split(';')[0]
    __jsl_clearance_s = jsl_cle_text.split('=')[1]
    cookies = {
        '__jsluid_s': __jsluid_s,
        '__jsl_clearance_s': __jsl_clearance_s
    }
    print('首次返回cookie: ', cookies)
    return cookies


def second_get():
    """code 521"""
    cookies = first_get()
    headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Mobile Safari/537.36"
    }
    resp = requests.get(url, headers=headers, cookies=cookies)
    print('二次响应数据：', resp.text)
    _0x1fde2d_text = re.findall(';go\((.*?)\)</script>', resp.text, re.S)[0]
    _0x1fde2d = json.loads(_0x1fde2d_text)
    print(_0x1fde2d)
    with open('zh-2-dec.js', encoding='utf-8') as f:
        js_code = f.read()

    exe = execjs.compile(js_code)
    __jsl_clearance_s = exe.call('get_cookie', _0x1fde2d)
    # print(__jsl_clearance_s)
    cookies.update({'__jsl_clearance_s': __jsl_clearance_s})
    print('二次返回cookie: ', cookies)
    return cookies


def third_get():
    """code 200"""
    cookies = second_get()
    headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Mobile Safari/537.36"
    }
    resp = requests.get(url, headers=headers, cookies=cookies)
    resp.encoding = 'utf-8'  # 设置响应数据的编码格式，不然返回有乱码
    print('三次响应数据：', resp.text)
    print(resp.text)


# first_get()
# second_get()
third_get()
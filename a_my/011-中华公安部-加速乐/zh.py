import re

import requests
import execjs

url = 'https://www.mps.gov.cn/n2254098/n4904352/index.html'

def first_get():
    resp = requests.get(url)
    __jsluid_s = resp.cookies.get('__jsluid_s')

    js_code = re.findall('document.cookie=(.*?);location.href', resp.text)[0]
    jsl_cle_text = execjs.eval(js_code).split(';')[0]
    __jsl_clearance_s = jsl_cle_text.split('=')[1]

    cookies = {
        '__jsluid_s': __jsluid_s,
        '__jsl_clearance_s': __jsl_clearance_s
    }
    # print(cookies)
    return cookies

def second_get():
    cookies = first_get()
    resp = requests.get(url, cookies=cookies)
    print(resp.text)
    __jsluid_s = resp.cookies.get('__jsluid_s')
    print(__jsluid_s)


second_get()
"""有道词典 翻译接口响应密文破解
加密方式：AES cbc模式
"""

import subprocess
from functools import partial

# 修改编码方式，windows 默认编码是gbk，Mac 和 Linux 默认是utf-8
subprocess.Popen = partial(subprocess.Popen, encoding='utf-8')

import execjs
import requests


url = 'https://dict.youdao.com/webtranslate'

headers = {
    "Cookie": "_ntes_nnid=4573866719e6af38a634727027cbd8d8,1561992959994; OUTFOX_SEARCH_USER_ID=1838921021@183.17.59.60; OUTFOX_SEARCH_USER_ID_NCOO=1088876131.1063359; P_INFO=13875045745|1657533079|1|dict_logon|00&99|null&null&null#gud&440300#10#0|&0|null|13875045745; YOUDAO_MOBILE_ACCESS_TYPE=0; UM_distinctid=185b8bf07d8c9e-018b7b21cba791-26021051-144000-185b8bf07d99fa",
    # "Host": "dict.youdao.com",
    # "Origin": "https://fanyi.youdao.com",
    # "Pragma": "no-cache",
    "Referer": "https://fanyi.youdao.com/",
    # "sec-ch-ua": "\"Not_A Brand\";v=\"99\", \"Google Chrome\";v=\"109\", \"Chromium\";v=\"109\"",
    # "sec-ch-ua-mobile": "?1",
    # "sec-ch-ua-platform": "\"Android\"",
    # "Sec-Fetch-Dest": "empty",
    # "Sec-Fetch-Mode": "cors",
    # "Sec-Fetch-Site": "same-site",
    "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Mobile Safari/537.36"
}

data = {
    'i': 'my name is yyds',
    'from': 'auto',
    # to: null,
    'domain': 0,
    'dictResult': True,
    'keyid': 'webfanyi',
    'sign': 'e39339a6fb1e92aa046406d67f195951',
    'client': 'fanyideskweb',
    'product': 'webfanyi',
    'appVersion': '1.0.0',
    'vendor': 'web',
    'pointParam': 'client,mysticTime,product',
    'mysticTime': '1673842025620',
    'keyfrom': 'fanyi.web'
}

resp = requests.post(url=url, data=data, headers=headers)
print('响应密文：', resp.text)

with open('youdao.js', encoding='utf-8') as f:
    js_code = f.read()

# print(js_code)
exe = execjs.compile(js_code)
res = exe.call('decodeData', resp.text)
print('解密结果：', res)

# text = 'Z21kD9ZK1ke6ugku2ccWu-MeDWh3z252xRTQv-wZ6jddVo3tJLe7gIXz4PyxGl73nSfLAADyElSjjvrYdCvEP4pfohVVEX1DxoI0yhm36ytQNvu-WLU94qULZQ72aml6qaEgNoL9hpcSmEB6685K2g_6vKeCBoW_2onZCm9lcoW72YMQC6Jro7XuC0JjLRpW8YWrbe_H5Q-LIw1uO3YX2gUY1_6yqDNn4rvl2Tc-axk3N0u3pnPLnWWnQXdNTf61BnpEC0RyZRlOKXldTcAIJ_zhnJuizmcFry5IpEFFDLMeDwOKRpmDqGqT7WeFIdXybr-vkmjPGdsYfb6wG76MlwV2vc7bTM_AXswRKDFxoCexbmCGNtplR8OZQ0JFy0hlZvAMqtQ21g-CnSW7gDLEYvq5Ry4t0hF_ykgWBvNnruZDOQXolhsrcVbmpwvTDQQY81Wiw3bIEvjE_mgEcHvmqg1xeguHjDuFaYSnl9FXr_e2w47TpEa4AwoRT6-VnFVxGkiyfbPFtbTJRr21JoacqE9ecLzGUX1GJfTEdcnFjorCt1B4Gz7wXGZiyED4CPQrDfz8m7-WTzvaYXHF0jKFqAfW6oO9mU1q-5CsySBJ5F4cXivBwWaMWOrcgKZflKvR_Jt5dBokbn2N2sZsXur3BZWHEJ2sRiWwK-jE0_eXsXoL6rYr4niXNX4MtDZoBMFn1nzIZYUwMd9fg97hOPN8aza5nJvkYcRG4zEOZsHV1ZpO7iDJHDadi_NlQrQ7pyHVt9RewNj0MUAMmUfMiUExQXO2NT5_CK3daDsSC1FxWV264W4K_tfB-RE_yv_2ErGBEveR-ZrYe6EFq1gILxfMz36Lf-7U_Gtpbcwz9jtBs0Cyst4pPIi0dhkrTbrYEyok5kyj4-GY7GsQcSOGBL9SZCTql3i-MsjQIs-8JrVVKmU='
# res = exe.call('decodeData', text)


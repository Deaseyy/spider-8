import subprocess
from functools import partial

# 修改编码方式，windows 默认编码是gbk，Mac 和 Linux 默认是utf-8
subprocess.Popen = partial(subprocess.Popen, encoding='utf-8')

import requests
import execjs
# from gmssl import sm4

# 需要提取的页码，每页数量
pageNo = 1
pageSize = 10

with open('guojiayibao.js', encoding='utf-8') as f:
    js_code = f.read()

exe = execjs.compile(js_code)
x_tif_nonce = exe.call('i')
x_tif_signature = exe.call('x_tif_signature')
x_tif_timestamp = exe.call('x_tif_timestamp')

t = {
    'data': {
        "data": {
            "addr": "",
            "areaCode": "110000", # 地区区号，应该可以自行传入
            "optinsName": "",
            "pageNo": pageNo,
            "pageSize": pageSize
        },
        "appCode": "T98HPCGN5ZVVQBS8LZQNOAEXVI9GYHKQ",
        "version": "1.0.0",
        "encType": "SM4",
        "signType": "SM2",
        "timestamp": x_tif_timestamp
    }
}
sign_data = exe.call('sign_data', t)
enc_data = exe.call('enc_data', t)

url = 'https://fuwu.nhsa.gov.cn/ebus/fuwu/api/nthl/api/CommQuery/queryLocalOptins'
headers = {
    "Accept": "application/json",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
    "Cache-Control": "no-cache",
    "channel": "web",
    "Connection": "keep-alive",
    "Content-Length": "413",
    "Content-Type": "application/json",
    "contentType": "application/x-www-form-urlencoded",
    "Cookie": "__jsluid_s=f249f3536a616a2d2a67d6f42d472a54; amap_local=440300; yb_header_active=-1; yb_header_show=true",
    "Host": "fuwu.nhsa.gov.cn",
    "Origin": "https://fuwu.nhsa.gov.cn",
    "Pragma": "no-cache",
    "Referer": "https://fuwu.nhsa.gov.cn/nationalHallSt/",
    "sec-ch-ua": "\"Not_A Brand\";v=\"99\", \"Google Chrome\";v=\"109\", \"Chromium\";v=\"109\"",
    "sec-ch-ua-mobile": "?1",
    "sec-ch-ua-platform": "\"Android\"",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Mobile Safari/537.36",
    "x-tif-nonce": "c4KCqFA6",
    "x-tif-paasid": "undefined",
    "x-tif-signature": "4e3613f164c55b7b456128ee8534a6fe87ef7fb793beac17f47449df9e1f73d2",
    "x-tif-timestamp": "1675237317",
    "X-Tingyun": "c=B|4Nl_NnGbjwY;x=fa6ed3435b5f4fbb"
}

t['data'].update({
    'data': {'encData': enc_data},
    'signData': sign_data
})

# data = {
#     "data": {
#         "data": {
#             "encData": "DAC536D90758AB68AF4373A349F3BBDF4CE34C33DC32F1068E9E23CA546C9EA8E639B26A7D25A6C1B97CCC02DDB933E477A9AAE02ED054FCBFB6DEA99372702FE64D17BF28F141090CC5289421E593DD"
#         },
#         "appCode": "T98HPCGN5ZVVQBS8LZQNOAEXVI9GYHKQ",
#         "version": "1.0.0",
#         "encType": "SM4",
#         "signType": "SM2",
#         "timestamp": 1675237317,
#         "signData": "DitO6d6O8oyO8NiXQbeSA2bxX0Iw+fl76yT72empkT1SFHivjr7lmoNfLa6THo4ouzq0EG4HBoiPyp2ZU4K8TA=="
#     }
# }
resp = requests.post(url, json=t, headers=headers)
# print(resp.json())
enc_res = resp.json()
res = exe.call('dec_data', enc_res) # 调用js 解密加密响应
print(res)


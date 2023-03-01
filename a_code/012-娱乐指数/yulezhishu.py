import subprocess
from functools import partial

# 修改编码方式，windows 默认编码是gbk，Mac 和 Linux 默认是utf-8
subprocess.Popen = partial(subprocess.Popen, encoding='utf-8')

import requests
import execjs


with open('yulezhishu.js', encoding='utf-8') as f:
    js_code = f.read()

exe = execjs.compile(js_code)


# url = 'https://www.chinaindex.net/iIndexMobileServer/mobile/movie/objectFansRank?channel=movielist&sign=5f3cce6a40c09a221b21104cc98436a3'
# url = 'https://www.chinaindex.net/iIndexMobileServer/mobile/entertainment/objectFansRank?channel=varietylist&sign=6fb5ce5dd1fb90ed46df7b71cef028e3'
url_movie = 'https://www.chinaindex.net/iIndexMobileServer/mobile/movie/objectFansRank'  # 电影榜
url_entertainment = 'https://www.chinaindex.net/iIndexMobileServer/mobile/entertainment/objectFansRank'  # 综艺榜

# params = {
#     'channel': 'movielist',
#     # // 网页测试感觉 sign 是写死的，但每个菜单不一样, 但是不携带也能请求数据
#     'sign': '5f3cce6a40c09a221b21104cc98436a3'
#     # 'channel': 'varietylist',
#     # 'sign': '6fb5ce5dd1fb90ed46df7b71cef028e3'
#
# }

params = {
    'channel': 'movielist'
}
params['sign'] = exe.call('getSign', params)
print('params: ', params)
headers = {
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Mobile Safari/537.36'
}
resp = requests.get(url_movie, params=params, headers=headers)
# resp = requests.get(url_entertainment, headers=headers)
print(resp.json())


res = exe.call('dataFilter', resp.json())
print(res)
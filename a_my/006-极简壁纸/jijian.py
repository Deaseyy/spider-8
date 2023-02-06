# import subprocess
# from functools import partial
#
# # 修改编码方式，windows 默认编码是gbk，Mac 和 Linux 默认是utf-8
# subprocess.Popen = partial(subprocess.Popen, encoding='utf-8')

import requests
import execjs

url = 'https://api.zzzmh.cn/bz/v3/getData'
headers = {
    "accept": "application/json, text/plain, */*",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8",
    "cache-control": "no-cache",
    "chuck": "b675dce0e8924ea797ae80365b631699",
    "content-length": "95",
    "content-type": "application/json;charset=UTF-8",
    "origin": "https://bz.zzzmh.cn",
    "pragma": "no-cache",
    "referer": "https://bz.zzzmh.cn/",
    "sec-ch-ua": "\"Not_A Brand\";v=\"99\", \"Google Chrome\";v=\"109\", \"Chromium\";v=\"109\"",
    "sec-ch-ua-mobile": "?1",
    "sec-ch-ua-platform": "\"Android\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Mobile Safari/537.36"
}
params = {
    "size": 24,
    "current": 1,
    "sort": 0,
    "category": 0,
    "resolution": 0,
    "color": 0,
    "categoryId": 0,
    "ratio": 0
}
resp = requests.post(url, json=params, headers=headers)
data = resp.json()
print('加密响应：', data['result'])


with open('jijian.js', encoding='utf-8') as f:
    js_code = f.read()

exe = execjs.compile(js_code)
# rrr = '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'
result = exe.call('getData', data['result'])
print('解密响应：', result)

images = []
for img in result['list']:
    image_id = img['i']
    img_url = exe.call('get_image_url', image_id)
    print(img_url)
    images.append(img_url)

# print(images)  # 等全部执行完太慢
print(len(images))

# 剩下的就用requests库去下载每一张图片
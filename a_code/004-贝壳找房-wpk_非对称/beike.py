import subprocess
from functools import partial

# 修改编码方式，windows 默认编码是gbk，Mac 和 Linux 默认是utf-8
subprocess.Popen = partial(subprocess.Popen, encoding='utf-8')

import requests
import execjs

password = 'yds11111111'


def get_init_info():
    url = 'https://clogin.ke.com/authentication/initialize'
    headers = {
        # "Accept": "application/json, text/plain, */*",
        # "Accept-Encoding": "gzip, deflate, br",
        # "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
        # "Cache-Control": "no-cache",
        # "Connection": "keep-alive",
        # "Content-Length": "77",
        # "Content-Type": "application/json;charset=UTF-8",
        # "Cookie": "lianjia_uuid=709c9392-4aa5-4e33-8848-cb763863cc6c; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22185fd1d14c91-07a41904872b43-26021051-3686400-185fd1d14cac03%22%2C%22%24device_id%22%3A%22185fd1d14c91-07a41904872b43-26021051-3686400-185fd1d14cac03%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E4%BB%98%E8%B4%B9%E5%B9%BF%E5%91%8A%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fwww.baidu.com%2Fother.php%22%2C%22%24latest_referrer_host%22%3A%22www.baidu.com%22%2C%22%24latest_search_keyword%22%3A%22%E8%B4%9D%E5%A3%B3%22%2C%22%24latest_utm_source%22%3A%22baidu%22%2C%22%24latest_utm_medium%22%3A%22pinzhuan%22%2C%22%24latest_utm_campaign%22%3A%22wyshenzhen%22%2C%22%24latest_utm_content%22%3A%22biaotimiaoshu%22%2C%22%24latest_utm_term%22%3A%22biaoti%22%7D%7D; select_city=430100; ke_uuid=88e1f24aeb1a2fc7fa55f115c9850959; _ga=GA1.2.95255170.1674988853; _gid=GA1.2.534415233.1674988853; __xsptplus788=788.1.1674988948.1674988948.1%234%7C%7C%7C%7C%7C%23%23SZNQgB2PwGgV0jJKfWSEnuzX1RKjTDsl%23; crosSdkDT2019DeviceId=imk384-fcmjkf-2bprv00zdw0768s-kxtoprbjd; beikeBaseData=%7B%22parentSceneId%22%3A%22%22%7D; lianjia_ssid=af95c991-9baa-4d84-bfdf-4b80abb39212; digv_extends=%7B%22utmTrackId%22%3A%22%22%7D",
        # "Host": "clogin.ke.com",
        # "Origin": "https://cs.fang.ke.com",
        # "Pragma": "no-cache",
        # "Referer": "https://cs.fang.ke.com/",
        # "sec-ch-ua": "\"Not_A Brand\";v=\"99\", \"Google Chrome\";v=\"109\", \"Chromium\";v=\"109\"",
        # "sec-ch-ua-mobile": "?1",
        # "sec-ch-ua-platform": "\"Android\"",
        # "Sec-Fetch-Dest": "empty",
        # "Sec-Fetch-Mode": "cors",
        # "Sec-Fetch-Site": "same-site",
        "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Mobile Safari/537.36"
    }
    data = {"service":"https://ajax.api.ke.com/login/login/getuserinfo","version":"2.0"}
    resp = requests.post(url, json=data, headers=headers)
    res = resp.json()
    loginTicketId = res['loginTicketId']
    pubkey = res['publicKey']['key']
    encodeVersion = res['publicKey']['version']
    return loginTicketId, pubkey, encodeVersion


def get_encrypt_pwd(pwd):
    with open('beike.js', encoding='utf-8') as f:
        js_code = f.read()

    exe = execjs.compile(js_code)
    e_password = exe.call('f', password, pubkey)
    return e_password


loginTicketId, pubkey, encodeVersion = get_init_info()
# print('loginTicketId:', loginTicketId)
# print('pubkey:', pubkey)
# print('encodeVersion:', encodeVersion, '类型:', type(encodeVersion))
e_password = get_encrypt_pwd(password)
# print(e_password)

url = 'https://clogin.ke.com/authentication/authenticate'
headers = {
    # "Accept": "application/json, text/plain, */*",
    # "Accept-Encoding": "gzip, deflate, br",
    # "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
    # "Cache-Control": "no-cache",
    # "Connection": "keep-alive",
    # "Content-Length": "1322",
    # "Content-Type": "application/json;charset=UTF-8",
    # "Cookie": "lianjia_uuid=709c9392-4aa5-4e33-8848-cb763863cc6c; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22185fd1d14c91-07a41904872b43-26021051-3686400-185fd1d14cac03%22%2C%22%24device_id%22%3A%22185fd1d14c91-07a41904872b43-26021051-3686400-185fd1d14cac03%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E4%BB%98%E8%B4%B9%E5%B9%BF%E5%91%8A%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fwww.baidu.com%2Fother.php%22%2C%22%24latest_referrer_host%22%3A%22www.baidu.com%22%2C%22%24latest_search_keyword%22%3A%22%E8%B4%9D%E5%A3%B3%22%2C%22%24latest_utm_source%22%3A%22baidu%22%2C%22%24latest_utm_medium%22%3A%22pinzhuan%22%2C%22%24latest_utm_campaign%22%3A%22wyshenzhen%22%2C%22%24latest_utm_content%22%3A%22biaotimiaoshu%22%2C%22%24latest_utm_term%22%3A%22biaoti%22%7D%7D; select_city=430100; ke_uuid=88e1f24aeb1a2fc7fa55f115c9850959; _ga=GA1.2.95255170.1674988853; _gid=GA1.2.534415233.1674988853; __xsptplus788=788.1.1674988948.1674988948.1%234%7C%7C%7C%7C%7C%23%23SZNQgB2PwGgV0jJKfWSEnuzX1RKjTDsl%23; crosSdkDT2019DeviceId=imk384-fcmjkf-2bprv00zdw0768s-kxtoprbjd; digv_extends=%7B%22utmTrackId%22%3A%22%22%7D; lianjia_ssid=1cdc16ef-7d23-43b7-81e1-f1bdc1e291fc",
    # "Host": "clogin.ke.com",
    # "Origin": "https://cs.fang.ke.com",
    # "Pragma": "no-cache",
    # "Referer": "https://cs.fang.ke.com/",
    # "sec-ch-ua": "\"Not_A Brand\";v=\"99\", \"Google Chrome\";v=\"109\", \"Chromium\";v=\"109\"",
    # "sec-ch-ua-mobile": "?1",
    # "sec-ch-ua-platform": "\"Android\"",
    # "Sec-Fetch-Dest": "empty",
    # "Sec-Fetch-Mode": "cors",
    # "Sec-Fetch-Site": "same-site",
    "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Mobile Safari/537.36"
}

data = {
    "service": "https://ajax.api.ke.com/login/login/getuserinfo",
    "mainAuthMethodName": "username-password",
    "accountSystem": "customer",
    "credential": {
        "username": "13811111114",
        # "password": "HdIKsgk0jTc+gyPnw0FIW0ojlOZ0bNPZtAF2PxEolOucGP+ELJHZw0WvtfZj9j4xeid4g6dopIYsM4Y6NlOf7WdnZCFgTsltXiw2tPfLz7+70y4QApRYUdLRms8rglm9gqx4QmKzm6RGqWqlyuM8iddNOZbVcriVV3FXkzA09V8=",
        "password": e_password,
        # "encodeVersion": "2"
        "encodeVersion": encodeVersion
    },
    "context": {
        "ua": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Mobile Safari/537.36",
        "clientSource": "pc",
        "os": "Android",
        "osVersion": "6.0",
        "registerPosLx": 425,
        "registerPosLy": 791.453125,
        "registerPosRx": 725,
        "registerPosRy": 841.453125,
        "clickPosX": 578,
        "clickPosY": 816,
        "screen": "982_1244"
    },
    # "loginTicketId": "u9K18VdppPNpcTnzToqRErTxTm081ovV",
    # "loginTicketId": "6fZYXkqCIXsjUxUF5Nq3RoGa80rjQShF",
    # "loginTicketId": "vcIsy4iVEpZJoyoqBk9SozJq8WqAAo4S",
    "loginTicketId": loginTicketId,
    "version": "2.0",
    # "version": encodeVersion,
    "srcId": "eyJ0Ijoie1wiZGF0YVwiOlwiMGVjMWQ0MjY1NTcwNjcwODY2MTc1NmUwN2U3NjRlNjEzYTY4Y2Y1NTgwYmVmOGI0NTgzZmZkZjQzNWUyZGUwMGI3ZWNhYTg0ZTQwNjg0ODJhYTEwNzc2NTJjYWZhMmY3OGI2MDA4YTczYzAyOWNiYmM3YzEzMDFmNmZkZjgxZmVhNDhiMGI1Y2Q3MGQ1YjI1Yzk3MjMwMjI1MzliYTViZTdhMTY0NDEzODc0MGQxYmNjYzVkYTYyM2Y0OWE1YTlmNDM3MDA1YmYxZGY5MmZlNjYwYjhlOGUzNDhlOGM0OWI3MTAwMTc1ZjI4MjgwOGM4MzA1YjdhYTRhMGI3MzJlOVwiLFwia2V5X2lkXCI6XCIxXCIsXCJzaWduXCI6XCI2YTM5OWRjMVwifSIsInIiOiJodHRwczovL2NzLmZhbmcua2UuY29tLyIsIm9zIjoid2ViIiwidiI6IjAuMSJ9",
    "ticketMaxAge": 604800
}

resp = requests.post(url=url, json=data, headers=headers)
print(resp.json())


"""
说明：
1.若使用正确加密算法的加密串，则会提示：
    {'exception': {'code': 'auth.incorrect.credential', 'identities': {},
    'message': '用户名或密码不正确'}, 'message': '用户名或密码不正确', 'success': False}
    这才是正常的，所以需要破解密码js加密。

2.若密码随便填写，将解密失败，则会提示：
    {'message': '密码校验失败，请重试', 'success': False}
    这表示密码加密不对
    
3.若 loginTicketId 使用太久，会提示过期：
    {'message': '登录状态过期，请刷新', 'success': False}
    需要从另一个接口获取 loginTicketId
若 请求接口时，没有传入正确的请求头，返回的 loginTicketId 看似一样，实则不正确，提示：
    {'exception': {'code': 'context.mismatching', 'identities': {}, 'message': '登录状态无效，请刷新'}, 
    'message': '登录状态无效，请刷新', 'success': False}

破解后最终正常返回：
    {'exception': {'code': 'auth.incorrect.credential', 'identities': {}, 'message': '用户名或密码不正确'}, 
    'message': '用户名或密码不正确', 'success': False}

"""


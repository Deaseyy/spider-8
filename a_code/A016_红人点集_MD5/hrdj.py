import hashlib

import requests

from utils.ut import compile_js, ctime


def login(phone, pwd):
    url = 'https://user.hrdjyun.com/wechat/phonePwdLogin'
    headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Mobile Safari/537.36"
    }
    data = {
        "phoneNum": phone,
        "pwd": hashlib.md5(pwd.encode()).hexdigest(),
        "t": ctime(),
        "tenant": 1,
    }
    exe = compile_js('hrdj-模拟md5.js')
    sig_text = exe.call('get_sig_text', data)
    data['sig'] = hashlib.md5(sig_text.encode()).hexdigest()
    # print('params:', data)
    resp = requests.post(url, json=data, headers=headers)
    return resp.json()


if __name__ == '__main__':
    phone = '13875045745'
    pwd = 'yds12345'
    print(login(phone, pwd))


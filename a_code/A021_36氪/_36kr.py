import requests

from utils.ut import ctime, compile_js


def login(mobileNo, password):
    url = 'https://gateway.36kr.com/api/mus/login/byMobilePassword'
    headers = {
        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Mobile Safari/537.36'
    }
    exe = compile_js('_36kr.js')
    mobile = exe.call('encrypt_param', mobileNo)
    pwd = exe.call('encrypt_param', password)
    params = {
        "krtoken": "",
        "partner_id": "web",
        "timestamp": ctime(),
        "param": {
            "countryCode": "86",
            # "mobileNo": "UYhObWZ+5QJZ6VIlnRGtIpKgaDv5s0if2aeZEjuTuqB0elsiuO9dyt8kjvZPPajP/cZqSpgLuJgHdG7wIT4EvmEkWyL2zAt/+tIL5DW1EhB+NK0hhIMC1dr28bh6jTp5gsIclWV58ysZW1QgmgoPvI7ZO8pfE2fwA20DJ6jvzJI=",
            # "password": "B9rdZaZ4WLdow6ztFbS1p9ahFeulDRNIPBsuWTcjpj8HF8NuX7p0w3+fHQk1d2vXTGyrRe2scsn6PoL13f/OeHThTpZTibeyjnzIesd6JXZiX0xfsheZKdAGVFLA7+Eb/F8uatSsDNqCoNC1RwYHnv+2LDXwYGkSVeiBvbLlP1I="
            "mobileNo": mobile,
            "password": pwd,
        }
    }
    resp = requests.post(url, json=params, headers=headers)
    print(resp.json())


if __name__ == '__main__':
    mobileNo = '13811111111'
    password = '123456789'
    login(mobileNo, password)
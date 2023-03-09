import requests

from utils.ut import compile_js


def get_data():
    headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Mobile Safari/537.36"
    }
    # 获取公钥
    pubkey_url = 'https://ec.minmetals.com.cn/open/homepage/public'
    resp = requests.post(pubkey_url, headers=headers)
    pubkey = resp.text
    print('公钥：', pubkey)

    # 获取数据
    data_url = 'https://ec.minmetals.com.cn/open/homepage/zbs/by-lx-page'
    base_params = {
        "inviteMethod": "",
        "businessClassfication": "",
        "mc": "",
        # "lx": "ZBGG",  # 可修改，暂不知道啥含义
        "lx": "CQGG",
        "dwmc": "",
        "pageIndex": 1 # 可修改页码
    }
    exe = compile_js('wukuang.js')
    enc_params = exe.call('encrypt_params', base_params, pubkey)
    params = {'param': enc_params}
    resp = requests.post(data_url, json=params, headers=headers)
    print(resp.json())


if __name__ == '__main__':
    get_data()


import requests

from utils.ut import compile_js, format_query_params


"""分析：
请求头有一个 加密参数，key 和 value 都是加密参数,且：
- 每页的 k，v 是固定的，根据api和参数加密而来；

加密方式使用: HmacSHA512
"""

def get_data():
    url = 'https://www.qcc.com/api/datalist/touzilist'
    params = {
        'keyNo': '5dffb644394922f9073544a08f38be9f',  # 应该是公司id， 可从列表api取值
        'pageIndex': 5  # 页码
    }
    t = url.replace('https://www.qcc.com', '') + '?' + format_query_params(params).lower()
    exe = compile_js('qichacha.js')
    k, v = exe.call('get_k_v', t)

    headers = {
        # "accept": "application/json, text/plain, */*",
        # "accept-encoding": "gzip, deflate, br",
        # "accept-language": "zh-CN,zh;q=0.9,en;q=0.8",
        # "b26315bd778a64e24856": "1eeb21d5bebd3d098ecf6c2a58f3ba6e2aa4dc7bc479362ea9c63466ffd2fea0309f244ca655518aade29020d1b29ee9fbe893ad586087d59a3b42ab4d5f4584",
        k: v,
        # "cache-control": "no-cache",
        # TODO: 暂未分析是否会改变
        "cookie": "_uab_collina=162463350927257430988502; qcc_did=b79eac63-19b3-4d62-908e-4b18b3bb992c; UM_distinctid=1867c3f28ff4dd-017161df0bc1d9-26031951-384000-1867c3f2900ceb; MQCCSESSID=161f9b6a144fab76c04ea01480; QCCSESSID=841ab184084288c4d863b60287; CNZZDATA1254842228=1522912875-1677120519-https%253A%252F%252Fwww.baidu.com%252F%7C1677746971; acw_tc=3b2550a216777473291188009ea02abc239639e2c0cc183b6e0f8ab97c",
        # "pragma": "no-cache",
        # "referer": "https://www.qcc.com/firm/5dffb644394922f9073544a08f38be9f.html",
        # "sec-ch-ua": "\"Chromium\";v=\"110\", \"Not A(Brand\";v=\"24\", \"Google Chrome\";v=\"110\"",
        # "sec-ch-ua-mobile": "?1",
        # "sec-ch-ua-platform": "\"Android\"",
        # "sec-fetch-dest": "empty",
        # "sec-fetch-mode": "cors",
        # "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Mobile Safari/537.36",
        # "x-pid": "0f028790a20964f4f9d6ab5202253945",
        # "x-requested-with": "XMLHttpRequest"
    }

    resp = requests.get(url, params=params, headers=headers)
    res = resp.json()
    return res


if __name__ == '__main__':
    print(get_data())
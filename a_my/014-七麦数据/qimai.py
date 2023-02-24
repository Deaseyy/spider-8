import requests

from a_my.utils import ut


# 有些参数不用传， 换个分页参数就行
t = {
    # 'params': {'brand': 'free', 'device': 'iphone', 'country': 'cn', 'genre': '36'}, // ok
    # 'params': {'brand': 'free', 'device': 'iphone', 'country': 'cn', 'genre': '36',
    #            'date': '2023-02-24', 'page': 2, 'is_rank_index': 1, 'snapshot': '14:48:04'},  // ok
    'params': {'brand': 'free', 'device': 'iphone', 'country': 'cn', 'genre': '36', 'page': 3},  # ok
    'url': '/rank/index',
    'baseURL': 'https://api.qimai.cn'
}

exe = ut.compile_js('qimai.js')
analysis = exe.call('getAnalysis', t)
print(analysis)


url = 'https://api.qimai.cn/rank/index'
headers = {
    "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Mobile Safari/537.36"
}
# params = {
#     "analysis": "exs4CQYVIwNvZmETByZRQAMPNlk4WlVHUFkISwhXUgQaI0dJTEMNAg9aU1UBAyFBUA==",
#     "brand": "free",
#     "device": "iphone",
#     "country": "cn",
#     "genre": "36"
# }
params = t['params']
params['analysis'] = analysis

resp = requests.get(url, params=params, headers=headers)
print(resp.json())
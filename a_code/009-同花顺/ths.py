import requests

url = 'http://q.10jqka.com.cn/index/index/board/all/field/zdf/order/desc/page/1/ajax/1/'
headers = {
    "Accept": "text/html, */*; q=0.01",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Cookie": "log=; Hm_lvt_78c58f01938e4d85eaf619eae71b4ed1=1675763083,1676276698; Hm_lpvt_78c58f01938e4d85eaf619eae71b4ed1=1676276698; v=A6M9HZV4xGOQfIhXMRtYYV3LMuxImDdkcS97HNUB_T58Z82SXWjHKoH8C1Lm",
    "hexin-v": "A6M9HZV4xGOQfIhXMRtYYV3LMuxImDdkcS97HNUB_T58Z82SXWjHKoH8C1Lm",
    "Host": "q.10jqka.com.cn",
    "Pragma": "no-cache",
    "Referer": "http://q.10jqka.com.cn/",
    "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Mobile Safari/537.36",
    "X-Requested-With": "XMLHttpRequest"
}
resp = requests.get(url, headers=headers)

print(resp.text)


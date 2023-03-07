import requests

url = 'https://www.renrenche.com/bj/ershouche/p3/?&plog_id=6a544c539cc2f6d011e8588b6fae941c'
headers = {
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Mobile Safari/537.36'
}
resp = requests.get(url, headers=headers)
print(resp.text)
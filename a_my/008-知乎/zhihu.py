import requests

url = 'https://www.zhihu.com/api/v4/comment_v5/answers/2875983182/root_comment?order_by=score&limit=30&offset='
resp = requests.get(url)
print(resp.json())  # 貌似不需要破解啥参数， 直接可以返回结果


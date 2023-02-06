import requests

res = requests.get('http://127.0.0.1:5001')
print(res.text)

res = requests.get('http://127.0.0.1:5001/params?name=lisi')
print(res.text)
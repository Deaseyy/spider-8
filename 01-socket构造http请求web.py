"""socket 构造http请求 下载图片"""
import re
import socket

# url = 'https://pic.netbian.com/uploads/allimg/220211/004115-1644511275bc26.jpg'
url = 'https://static.nuvision.com.cn/frames/605775613/2d/0A.png?x-oss-process=style/gallery'

socket = socket.socket()
# socket.connect(('pic.netbian.com', 80)) # 443 https 需要配置ssl证书，这里采用80端口，前提是网站开放了80端口的访问
socket.connect(('static.nuvision.com.cn', 80)) # 443 https 需要配置ssl证书，这里采用80端口，前提是网站开放了80端口的访问

# http/1.1 不加 Connection: close\r\n 会很慢
# http_req = 'GET ' + url + ' HTTP/1.1\r\nhost: pic.netbian.com\r\nuser-agent: Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1\r\n\r\n'
http_req = 'GET ' + url + ' HTTP/1.1\r\nhost: static.nuvision.com.cn\r\nuser-agent: Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1\r\nConnection: close\r\n\r\n'

socket.send(http_req.encode())
data = socket.recv(1024)
result = b''
while data:
    result += data
    data = socket.recv(1024)

print(result)

img = re.findall(b'\r\n\r\n(.*)', result, re.S)[0]
# print(img)

with open('1-socket-2.jpg', 'wb') as f:
    f.write(img)


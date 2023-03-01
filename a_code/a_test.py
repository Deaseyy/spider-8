import re
import time

a = 'eyJ0Ijoie1wiZGF0YVwiOlwiMGVjMWQ0MjY1NTcwNjcwODY2MTc1NmUwN2U3NjRlNjEzYTY4Y2Y1NTgwYmVmOGI0NTgzZmZkZjQzNWUyZGUwMGI3ZWNhYTg0ZTQwNjg0ODJhYTEwNzc2NTJjYWZhMmY3OGI2MDA4YTczYzAyOWNiYmM3YzEzMDFmNmZkZjgxZmVhNDhiMGI1Y2Q3MGQ1YjI1Yzk3MjMwMjI1MzliYTViZWNlZjFjMTkzZTQ3N2QxY2RkZTgwY2FkN2EwNDkxZTU4YjRjOTVmNWQ2Y2M5ZDM2N2QzMGFkOGU0NWMxYzU5YTE1MzkyMTY0Y2U4MGNlYzM4MzM0MzQ1ZjA3YjMxZmNiOFwiLFwia2V5X2lkXCI6XCIxXCIsXCJzaWduXCI6XCI2OTY3YzA0OVwifSIsInIiOiJodHRwczovL2NzLmZhbmcua2UuY29tLyIsIm9zIjoid2ViIiwidiI6IjAuMSJ9'
b = 'eyJ0Ijoie1wiZGF0YVwiOlwiMGVjMWQ0MjY1NTcwNjcwODY2MTc1NmUwN2U3NjRlNjEzYTY4Y2Y1NTgwYmVmOGI0NTgzZmZkZjQzNWUyZGUwMGI3ZWNhYTg0ZTQwNjg0ODJhYTEwNzc2NTJjYWZhMmY3OGI2MDA4YTczYzAyOWNiYmM3YzEzMDFmNmZkZjgxZmVhNDhiMGI1Y2Q3MGQ1YjI1Yzk3MjMwMjI1MzliYTViZTM0NjAzNDk3NmE4YWEwMmEwZGUzOGRiMTE4YmE0ZjMyZmYwNWZkMzFmNTYwZGI4ZGYzNWMxZmUzN2VlYWJmOWNlYWU3YTQ4Njc0OTIyYzk4Y2QzZmI0MmJiZWNiMmRjY1wiLFwia2V5X2lkXCI6XCIxXCIsXCJzaWduXCI6XCI2ZGM5MDQzZlwifSIsInIiOiJodHRwczovL2NzLmZhbmcua2UuY29tLyIsIm9zIjoid2ViIiwidiI6IjAuMSJ9'

print(time.time())
t = 1678809600
loc = time.localtime(t)
print(loc)
print(time.strftime('%Y-%m-%d %X',loc))

text = 'geetest_1677592020704({"gt": "019924a82c70bb123aae90d483087f94", "challenge": "d9ae1c3423682154e8bcad355df07f3fe1", "id": "ad9ae1c3423682154e8bcad355df07f3f", "bg": "pictures/gt/cd0bbb6fe/bg/45cf39266.jpg", "fullbg": "pictures/gt/cd0bbb6fe/cd0bbb6fe.jpg", "link": "", "ypos": 20, "xpos": 0, "height": 160, "slice": "pictures/gt/cd0bbb6fe/slice/45cf39266.png", "api_server": "https://api.geetest.com", "static_servers": ["static.geetest.com/", "dn-staticdown.qbox.me/"], "mobile": true, "theme": "ant", "theme_version": "1.2.6", "template": "", "logo": true, "clean": false, "type": "multilink", "fullpage": false, "feedback": "https://www.geetest.com/contact#report", "show_delay": 250, "hide_delay": 800, "benchmark": false, "version": "6.0.9", "product": "embed", "https": true, "width": "100%", "show_voice": true, "c": [12, 58, 98, 36, 43, 95, 62, 15, 12], "s": "70664e72", "so": 0, "i18n_labels": {"cancel": "\u53d6\u6d88", "close": "\u5173\u95ed\u9a8c\u8bc1", "error": "\u8bf7\u91cd\u8bd5", "fail": "\u8bf7\u6b63\u786e\u62fc\u5408\u56fe\u50cf", "feedback": "\u5e2e\u52a9\u53cd\u9988", "forbidden": "\u602a\u7269\u5403\u4e86\u62fc\u56fe\uff0c\u8bf7\u91cd\u8bd5", "loading": "\u52a0\u8f7d\u4e2d...", "logo": "\u7531\u6781\u9a8c\u63d0\u4f9b\u6280\u672f\u652f\u6301", "read_reversed": false, "refresh": "\u5237\u65b0\u9a8c\u8bc1", "slide": "\u62d6\u52a8\u6ed1\u5757\u5b8c\u6210\u62fc\u56fe", "success": "sec \u79d2\u7684\u901f\u5ea6\u8d85\u8fc7 score% \u7684\u7528\u6237", "tip": "\u8bf7\u5b8c\u6210\u4e0b\u65b9\u9a8c\u8bc1", "voice": "\u89c6\u89c9\u969c\u788d"}, "gct_path": "/static/js/gct.b71a9027509bc6bcfef9fc6a196424f5.js"})'
r = re.findall('geetest_\d+\((.*?)\)', text)[0]
print(r)

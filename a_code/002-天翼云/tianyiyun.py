import execjs
import requests


url = 'https://m.ctyun.cn/account/login'

headers = {
    # "Cookie": "mvid=900f64f1-1b51-4872-83ff-4d99a8662c5b; Hm_lvt_4b4ce93f1c92033213556e55cb65769f=1673924430,1674179676; sid1=1674179677075-44459E937A4991095EFA0C2FEA002567; sid2=1674179677075-44459E937A4991095EFA0C2FEA002567; Hm_lpvt_4b4ce93f1c92033213556e55cb65769f=1674179736; pvid=3",
    # "Host": "m.ctyun.cn",
    # "Pragma": "no-cache",
    # "Referer": "https://m.ctyun.cn/wap/main/auth/login",
    # "sec-ch-ua": "\"Not_A Brand\";v=\"99\", \"Google Chrome\";v=\"109\", \"Chromium\";v=\"109\"",
    # "sec-ch-ua-mobile": "?1",
    # "sec-ch-ua-platform": "\"Android\"",
    # "Sec-Fetch-Dest": "empty",
    # "Sec-Fetch-Mode": "cors",
    # "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Mobile Safari/537.36",
    # "x-riskdevicesign": "5a389862331406f7b744fee485d23a61"
}

userName = '123456789@163.com'
pwd = '123456789'

with open('tianyiyun.js', encoding='utf-8') as f:
    js_code = f.read()

exe = execjs.compile(js_code)
DES_pwd = exe.call('T', pwd, userName)
print('加密结果：', DES_pwd)

params = {
    "userName": userName,
    # "password": "skAvSv1k+9NyY5s7FY79Lg==",
    # "password": pwd,   # 明文好像也没啥区别，都返回：{"resultCode":"-1","resultMsg":"账户或密码不正确","code":"","success":false}
    "password": DES_pwd,
    "referrer": "wap",
    "mainVersion": "300031500",
    "comParam_curTime": "1674179698671",
    "comParam_seqCode": "CDA683496F3CCB594E41DBED5F937ED2",
    "comParam_signature": "db713bcad907174aef07e5b433e9ab80",
    "isCheck": "true",
    "locale": "zh-cn"
}

resp = requests.get(url=url, params=params, headers=headers)
# print(resp.json())
print(resp.text)


"""
问题：
1.密码明文好像也没啥区别，都返回：
    {"resultCode":"-1","resultMsg":"账户或密码不正确","code":"","success":false}

2.请求响应返回比较久
"""


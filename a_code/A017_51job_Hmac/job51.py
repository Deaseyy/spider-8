import hmac

import requests

from utils.ut import format_query_params, ctime


def get_data():
    url = 'https://cupid.51job.com/open/noauth/search-pc'
    params = {
        "api_key": "51job",
        "timestamp": ctime(ms=False),
        "keyword": "Java",
        "searchType": "2",
        "function": "",
        "industry": "",
        "jobArea": "000000",
        "jobArea2": "",
        "landmark": "",
        "metro": "",
        "salary": "",
        "workYear": "",
        "degree": "",
        "companyType": "",
        "companySize": "",
        "jobType": "",
        "issueDate": "",
        "sortType": "0",
        "pageNum": "5",
        "requestId": "d10b2f8b3db7dcc6e084c09f7137a604",
        "pageSize": "50",
        "source": "1",
        "accountId": "",
        "pageCode": "sou|sou|soulb"
    }
    t = url.replace('https://cupid.51job.com', '') + '?' + format_query_params(params, sort=False, urlencode=True)
    cupid_sign_key = "abfc8f9dcf8c3f3d8aa294ac5f2cf2cc7767e5592590f39c3f503271dd68562b" # js写死的key
    sign = hmac.new(cupid_sign_key.encode(), msg=t.encode(), digestmod='sha256').hexdigest()
    headers = {
        # "Accept": "application/json, text/plain, */*",
        # "Accept-Encoding": "gzip, deflate, br",
        # "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
        # "account-id": "",
        # "Cache-Control": "no-cache",
        # "Connection": "keep-alive",
        # "From-Domain": "51job_web",
        # "Host": "cupid.51job.com",
        # "Origin": "https://we.51job.com",
        # "partner": "www_baidu_com",
        # "Pragma": "no-cache",
        # "property": "%7B%22partner%22%3A%22www_baidu_com%22%2C%22webId%22%3A2%2C%22fromdomain%22%3A%2251job_web%22%2C%22frompageUrl%22%3A%22https%3A%2F%2Fwe.51job.com%2F%22%2C%22pageUrl%22%3A%22https%3A%2F%2Fwe.51job.com%2Fpc%2Fsearch%3Fkeyword%3DPython%26searchType%3D2%26sortType%3D0%26metro%3D%22%2C%22identityType%22%3A%22%22%2C%22userType%22%3A%22%22%2C%22isLogin%22%3A%22%E5%90%A6%22%2C%22accountid%22%3A%22%22%7D",
        # "Referer": "https://we.51job.com/",
        # "sec-ch-ua": "\"Chromium\";v=\"110\", \"Not A(Brand\";v=\"24\", \"Google Chrome\";v=\"110\"",
        # "sec-ch-ua-mobile": "?1",
        # "sec-ch-ua-platform": "\"Android\"",
        # "Sec-Fetch-Dest": "empty",
        # "Sec-Fetch-Mode": "cors",
        # "Sec-Fetch-Site": "same-site",
        # "sign": "048b96ec9b71233f0594255bf8a7dafe17af95be39b0655825bc05ea886c81f3",
        "sign": sign,
        "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Mobile Safari/537.36",
        # "user-token": "",
        # "uuid": "000422719de166142b90db33ba6c198f"
    }
    resp = requests.get(url, params=params, headers=headers)
    return resp.json()




if __name__ == '__main__':
    print(get_data())


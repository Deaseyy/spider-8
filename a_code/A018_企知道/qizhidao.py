import requests

from a_code.utils.ut import compile_js


def get_data():
    url = 'https://app.qizhidao.com/qzd-bff-enterprise/qzd/v1/enterprise/zhichan/enterpriseListV2'
    headers = {
    # "accept": "application/json, text/plain, */*",
    # # "accept-encoding": "gzip, deflate, br",  // 要去掉，不然返回压缩后的乱码结果
    # "accept-language": "zh-CN,zh;q=0.9",
    "accesstoken": "eyJhbGciOiJIUzUxMiJ9.ZXlKNmFYQWlPaUpFUlVZaUxDSmhiR2NpT2lKa2FYSWlMQ0psYm1NaU9pSkJNVEk0UTBKRExVaFRNalUySW4wLi5KLXFDNnFnVXQxanFWdHNmTU1yUGxBLkFwVkR1UUF5dnRsWk1vVHRmYXlpMzI4ZGdYcHE0U3NsOFozcDFLZF9JbHBWa1pGVmhUZW8xbmk1VjVhQVJIakpLVURmZWNWNUo0am1vM0k1RTJXMGV6UC1RWWw3VE1oS0UtVmZmZ2RmVGFqM3UzLWZ3LUo2Qm92VHR6OXdUcUFLeHdwLTg3ZHNmMDlRNEhpNmxobzNWVGc2ZzBvU0luMWRpY2xkVnktQ3NJcm1ZYkFiMzA2QXlBaFJ6bFF6TnpOS01tcExHTzBBSWV5QWtaN0NBUnJIN3FpOVhMQTB4b0VKbC16S0QtbVoxbG8uS183UWRGQU5YS2FQb29PRUhUWlZPZw.TUyp187ngFDzaV-3IsQVmoZNUVFfZ1xqYfWS50gUCW-TZIWbXiZcTfNHlHDIYohX0XL4mVoTVZGa-Mqq515lkA",
    # "content-length": "114",
    # "content-type": "application/json; charset=UTF-8",
    # "cookie": "token=eyJhbGciOiJIUzUxMiJ9.ZXlKNmFYQWlPaUpFUlVZaUxDSmhiR2NpT2lKa2FYSWlMQ0psYm1NaU9pSkJNVEk0UTBKRExVaFRNalUySW4wLi5KLXFDNnFnVXQxanFWdHNmTU1yUGxBLkFwVkR1UUF5dnRsWk1vVHRmYXlpMzI4ZGdYcHE0U3NsOFozcDFLZF9JbHBWa1pGVmhUZW8xbmk1VjVhQVJIakpLVURmZWNWNUo0am1vM0k1RTJXMGV6UC1RWWw3VE1oS0UtVmZmZ2RmVGFqM3UzLWZ3LUo2Qm92VHR6OXdUcUFLeHdwLTg3ZHNmMDlRNEhpNmxobzNWVGc2ZzBvU0luMWRpY2xkVnktQ3NJcm1ZYkFiMzA2QXlBaFJ6bFF6TnpOS01tcExHTzBBSWV5QWtaN0NBUnJIN3FpOVhMQTB4b0VKbC16S0QtbVoxbG8uS183UWRGQU5YS2FQb29PRUhUWlZPZw.TUyp187ngFDzaV-3IsQVmoZNUVFfZ1xqYfWS50gUCW-TZIWbXiZcTfNHlHDIYohX0XL4mVoTVZGa-Mqq515lkA; ticket=eyJhbGciOiJIUzUxMiJ9.ZXlKNmFYQWlPaUpFUlVZaUxDSmhiR2NpT2lKa2FYSWlMQ0psYm1NaU9pSkJNVEk0UTBKRExVaFRNalUySW4wLi5KLXFDNnFnVXQxanFWdHNmTU1yUGxBLkFwVkR1UUF5dnRsWk1vVHRmYXlpMzI4ZGdYcHE0U3NsOFozcDFLZF9JbHBWa1pGVmhUZW8xbmk1VjVhQVJIakpLVURmZWNWNUo0am1vM0k1RTJXMGV6UC1RWWw3VE1oS0UtVmZmZ2RmVGFqM3UzLWZ3LUo2Qm92VHR6OXdUcUFLeHdwLTg3ZHNmMDlRNEhpNmxobzNWVGc2ZzBvU0luMWRpY2xkVnktQ3NJcm1ZYkFiMzA2QXlBaFJ6bFF6TnpOS01tcExHTzBBSWV5QWtaN0NBUnJIN3FpOVhMQTB4b0VKbC16S0QtbVoxbG8uS183UWRGQU5YS2FQb29PRUhUWlZPZw.TUyp187ngFDzaV-3IsQVmoZNUVFfZ1xqYfWS50gUCW-TZIWbXiZcTfNHlHDIYohX0XL4mVoTVZGa-Mqq515lkA; accessToken=eyJhbGciOiJIUzUxMiJ9.ZXlKNmFYQWlPaUpFUlVZaUxDSmhiR2NpT2lKa2FYSWlMQ0psYm1NaU9pSkJNVEk0UTBKRExVaFRNalUySW4wLi5KLXFDNnFnVXQxanFWdHNmTU1yUGxBLkFwVkR1UUF5dnRsWk1vVHRmYXlpMzI4ZGdYcHE0U3NsOFozcDFLZF9JbHBWa1pGVmhUZW8xbmk1VjVhQVJIakpLVURmZWNWNUo0am1vM0k1RTJXMGV6UC1RWWw3VE1oS0UtVmZmZ2RmVGFqM3UzLWZ3LUo2Qm92VHR6OXdUcUFLeHdwLTg3ZHNmMDlRNEhpNmxobzNWVGc2ZzBvU0luMWRpY2xkVnktQ3NJcm1ZYkFiMzA2QXlBaFJ6bFF6TnpOS01tcExHTzBBSWV5QWtaN0NBUnJIN3FpOVhMQTB4b0VKbC16S0QtbVoxbG8uS183UWRGQU5YS2FQb29PRUhUWlZPZw.TUyp187ngFDzaV-3IsQVmoZNUVFfZ1xqYfWS50gUCW-TZIWbXiZcTfNHlHDIYohX0XL4mVoTVZGa-Mqq515lkA; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22eff1e4c329974936b42769323ab0fef0%22%2C%22first_id%22%3A%22186aca8515c454-0008b57b8a4a069a-57b1a33-1327104-186aca8515d804%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfbG9naW5faWQiOiJlZmYxZTRjMzI5OTc0OTM2YjQyNzY5MzIzYWIwZmVmMCIsIiRpZGVudGl0eV9jb29raWVfaWQiOiIxODZhY2E4NTE1YzQ1NC0wMDA4YjU3YjhhNGEwNjlhLTU3YjFhMzMtMTMyNzEwNC0xODZhY2E4NTE1ZDgwNCJ9%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%24identity_login_id%22%2C%22value%22%3A%22eff1e4c329974936b42769323ab0fef0%22%7D%2C%22%24device_id%22%3A%22186aca8515c454-0008b57b8a4a069a-57b1a33-1327104-186aca8515d804%22%7D; wz_uuid=X%2F8a829b07859b0d5972027080c091a295; x-web-ip=14.154.29.167, 119.23.123.175, 120.78.44.143, 100.121.99.188; sensorsdata2015jssdkchannel=%7B%22prop%22%3A%7B%22_sa_channel_landing_url%22%3A%22%22%7D%7D; creditNo=%22%22; Hm_lvt_9ea3e7293b7c088e0d2c88874b63e7dd=1677933961,1678002943; Hm_lpvt_9ea3e7293b7c088e0d2c88874b63e7dd=1678002943; acw_tc=784e2c9516780028862918216e6114e2ba64a2adb26fd54b8713e4b42ae271; SERVERID=b14e139c6c11571a3f0b0522ee275399|1678004105|1678002886; SERVERCORSID=b14e139c6c11571a3f0b0522ee275399|1678004105|1678002886",
    "device-id": "BQEsfmyR5bs5NNPnTES5IiNxYdI9CzPqgS8Py8z/6mHoTUfTQORIfv8DqNSwJD3tLAgpKnbYrOtcyBPNKdUwOCA==",  # 不给会提示行为异常
    # "h5version": "v1.0.0",
    # "origin": "https://www.qizhidao.com",
    # "referer": "https://www.qizhidao.com/",
    # "sec-ch-ua": "\"Chromium\";v=\"21\", \" Not;A Brand\";v=\"99\"",
    # "sec-ch-ua-mobile": "?0",
    # "sec-ch-ua-platform": "\"Windows\"",
    # "sec-fetch-dest": "empty",
    # "sec-fetch-mode": "cors",
    # "sec-fetch-site": "same-site",
    # "sensordeviceid": "186aca8515c454-0008b57b8a4a069a-57b1a33-1327104-186aca8515d804",
    # "sensorsdistinctid": "eff1e4c329974936b42769323ab0fef0",
    # "signature": "c92125e46f6e78083771cfbde469fc8a.5rggkm",  # 测试感觉好像不用破解，白费几小时去破解了
    # "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36", # 360极速的
    "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Mobile Safari/537.36",  # 谷歌的
    # "user-agent-web": "X/8a829b07859b0d5972027080c091a295",
    # "x-web-ip": "14.154.29.167, 119.23.123.175, 120.78.44.143, 100.121.99.188"
}
    params = {
        "content": "人工智能",
        "current": 10,
        "found_years": [],
        "pageSize": 20,
        "platform": 1,
        "isDefinedYears": 0,
        "isSwitch": 0
    }
    resp = requests.post(url, json=params, headers=headers)
    print(resp.text)
    data = resp.json()
    enc_data = data['data1']
    hasUse = data['hasUse']
    exe = compile_js('qizhidao.js')
    res = exe.call('decrypt_data', enc_data, hasUse)
    return res


if __name__ == '__main__':
    print(get_data())

import requests

url = 'https://sh.esfxiaoqu.zhuge.com/page2/'
headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Cookie": "SECKEY_ABVK=mNOIlrH0nmVmG6sGf/tpCUuxsTEP7PpXe0nNRn/xR98%3D; BMAP_SECKEY=rhyNdVZZFlIgN90qjlnBAb1hA1Ln6G2vk7jNZP__I8fCLEyKAWkfBkp6Zb0px3de3-nT-UVffpXTPsgX_UxJ28buL7U485pCTxB87-ilCJkH0_6vRn9uFs3pMkO4hToJILqAKTuZusY5UHYOIq1561wAV9Ar5Z2dksoNjM29kOr4MDvl2rt2P-ZLKda5IsQEDamg2HE2LvzOmJVoKBeipQ; acw_tc=2760823716765173831796145edef31e14add41787970ae57679f0fea6217f; _WEB_page_type=web; _WEB_city_code=sh; _WEB_token=Um7EACW-c8jdx5L600lNC8GVcgPIx8HdTX5NIj_K4lFeM5cTHDt13AEeuPfDqMqUcgU6A6cqHrybDrOPvHU9VQ==; _WEB_USER_ID=1676517475503330; _WEB_city_name=%E4%B8%8A%E6%B5%B7; _WEB_cityid=2; _WEB_ip_cityCode=sz; _WEB_ip_cityName=%E6%B7%B1%E5%9C%B3; sajssdk_2015_cross_new_user=1; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22186583b5fbb20a-01e5cd9293a1537-26031951-3686400-186583b5fbcbd3%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22%24device_id%22%3A%22186583b5fbb20a-01e5cd9293a1537-26031951-3686400-186583b5fbcbd3%22%7D; _ga=GA1.2.1042398828.1676517532; _gid=GA1.2.1253605210.1676517532; Hm_lvt_8d409b931bc5e2ac53a0cea966f06d99=1676515757,1676517348,1676517532; acw_sc__v2=63eda0ab7d4f217eb1b4cc9ffa1d6225ee356292; _WAP_page_type=wap; _WAP_city_code=sh; _WAP_token=OWClLsSjtswommkpvyNp7mqlJOqw5abwxxeqnCK-awvHsszxZKC0R9LMolAyALeQ1lfmCFle-STed9ksOX7olA==; _WAP_USER_ID=1676517547767722; _WAP_city_name=%E4%B8%8A%E6%B5%B7; _WAP_cityid=2; _WAP_ip_cityCode=sz; _WAP_ip_cityName=%E6%B7%B1%E5%9C%B3; gr_user_id=64f2a238-f172-44e8-b833-1e4b812e79be; 9d1fd90035f1c8a9_gr_session_id=190e94dc-1d54-4a0d-8d0e-52597343ac60; 9d1fd90035f1c8a9_gr_session_id_190e94dc-1d54-4a0d-8d0e-52597343ac60=true; Hm_lpvt_8d409b931bc5e2ac53a0cea966f06d99=1676518044",
    "Host": "m.zhuge.com",
    "Pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"110\", \"Not A(Brand\";v=\"24\", \"Google Chrome\";v=\"110\"",
    "sec-ch-ua-mobile": "?1",
    "sec-ch-ua-platform": "\"Android\"",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Mobile Safari/537.36"
}
resp = requests.get(url)
# resp = requests.get(url,headers=headers)
print(resp.text)

print(ord('p'))
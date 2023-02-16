"""
目标接口：https://www.toutiao.com/api/pc/list/feed?channel_id=0&max_behot_time=1675742074&category=pc_profile_recommend&aid=24&app_name=toutiao_web&_signature=_02B4Z6wo001011x6ISwAAIDBvs9RuTCeqjtcTiWAALUK0oIe83dxBNYmNE5JMv24LKn8oyPhSZJTjy-bQuXI.GxowOhg34oxwEuEYMZx.kuX7H5ZRIYqUQr4asUFjArqw1Ii0jeljvoH4PVH7e

逆向参数：
- _signature

逆向方式：rpc转发
"""

import requests
data = {
    "group": "toutiao",
    "action": "signature",
}
resp = requests.get("http://127.0.0.1:5620/business-demo/invoke", params=data)
res = resp.json()
print(res)
print(res['data'])



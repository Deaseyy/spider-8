"""
国家医疗保障局-医保机构查询，网址:
    https://fuwu.nhsa.gov.cn/nationalHallSt/#/search/agency-inquiry

可疑加密参数
头部：
x-tif-nonce: D3hHkgZH
    - 随机串
x-tif-signature: 66c06d602b12b80e48656e417e8b99029296e8e49efe31908b7bafac76446a57
    - 国际标准 SHA256 加密
x-tif-timestamp: 1675235840
    - 时间戳
X-Tingyun: c=B|4Nl_NnGbjwY;x=5d354f546a7b4221
载荷：
appCode："T98HPCGN5ZVVQBS8LZQNOAEXVI9GYHKQ"
    - 固定值
encData:"DAC536D90758AB68AF4373A349F3BBDF4CE34C33DC32F1068E9E23CA546C9EA8E639B26A7D25A6C1B97CCC02DDB933E4DDE5E61C1F66ECE05044FE3A9B2AFB45E64D17BF28F141090CC5289421E593DD"
    - 加密类型：SM4
signData:"yCdzS8LYKYqKwdSQIabjXnTByCTznQdy1ufa+MujtGnTAlQDhZWGLkBCpn19NyLzV5KOpeKnnInbU6l5WuI+hw=="
    - 加密类型：SM2
响应：
    encData  SM4 加密，需要找到对应js解密函数
"""

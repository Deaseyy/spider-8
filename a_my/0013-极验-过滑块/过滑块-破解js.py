import time

import requests

# ==============================初次进入极验网址， 有以下请求========================================================
def get_1():
    """
    register-slide
    :return:
        - challenge
        - gt
    """
    url = 'https://www.geetest.com/demo/gt/register-slide'
    headers = {
        "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Mobile Safari/537.36"
    }
    # params = {'t': '1677050511202'}  # 必须写活，不然返回的challenge不变，导致后面请求提示 "old challenge"
    params = {'t': str(int(time.time() * 1000))}
    resp = requests.get(url, params=params, headers=headers)
    print('req1: ', resp.json())
    # {'success': 1, 'challenge': 'f3c968c1da2e448be62ef951ff4b67f9', 'gt': '019924a82c70bb123aae90d483087f94', 'new_captcha': True}
    return resp.json()


def get_2(res1):
    """gettype.php
    返回一堆 js 文件
    """
    url = 'https://apiv6.geetest.com/gettype.php'
    headers = {
        "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Mobile Safari/537.36"
    }
    params = {
        # 'gt': '019924a82c70bb123aae90d483087f94', # 不写活，也能返回success
        # 'callback': 'geetest_1677050515844'
        "gt": res1['gt'],
        "challenge": res1['challenge'],
    }
    resp = requests.get(url=url, params=params, headers=headers)
    print('req2: ', resp.text)



def get_3(res1):
    """get.php"""
    url = 'https://apiv6.geetest.com/get.php'
    headers = {
        "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Mobile Safari/537.36"
    }
    params = {
        # "gt": "019924a82c70bb123aae90d483087f94",
        # "challenge": "10c647b38b39e0b7f439979439744931",
        "gt": res1['gt'],
        "challenge": res1['challenge'],
        "lang": "zh-cn",
        "pt": "3",
        "client_type": "web_mobile",
        "w": "cx5PhynwYxqS2KYDFbPW1xz7vgy(4PknC4ov3MoOnLLlOLcLV4qm5SNHyn6IYz2T8mW4rsk9XdB45wpDCVm070eO5gFwFuraYq0eIw9b0rS2JOoqCQpm5jye1ORvBS4q1Wr1ias0iO2Un7ZvrMUQD4j)slZ1TvgD6N6BP)0)yzlX73l(VtxTmOkVwlWHYGLO0qVmf9MmuWiDFgka5cj2BW0lbW(UiHB9YlQEwxAZQuwyCs6fEngRUMbIxrn0c1Vunu3vvq9fiRsSw2wf8kOrB75oRcUmwOWaQLsE4LTYnnyj7vfE8DFNyQZFIdjRut4wsFA(eKvCR2aNoW4AQUUBVIvkqOQmFcDHhFKwXTp6yRGyqwkcMXbCgW3DO5CopySIFUdTR17(FjFAHZJ6B7JzNH5JttFhOWH6rfiowH8LOfvuQwxYriGyKuwS5QwSeXucWU(7Cu50RPBzeeNtL2s)OfdSItUJXwEj(u23Xga1L16Vy8z43Na3h0BEh0mYYHop8XiOGaWUS5Dac(eMZSqkn2L2BD1wVO)MMiffTJleBN3W89n(n(X2CQmte9OP5x6MQ)7(GHU5czwlpAJjO5l3d)FtkehE8(uRcuaT0cuA)CEV0qqDpwO8I6(ooQOl0TuH(HXpDgtkfAncyB7cfIRQSOb580SoYXDIkw3YUVEkan5S)BmbDzDGP76zEqUAzM6uiIiQ81yS9zdF11OXok6K1Cjv1hyIBHVx1fb5ZbsMOQyI8DDXD4eSVKEk8eB6C9LZtze1OzDOG9fwN9BSm5)ppBWOLGwr1u31nRJAoxlMQOygHaLMu(OYOrGtgUzvEs8JfkU)HZdic7f1OREWXterEqh8Z)gQxd1t1yLfGjC915LR3vq6ZZhzy)J5XrEZ0M4xTfBD3BaRI3ntQuXW9cvCzekOYMWFnUUJs0ACTgg6e1NSTCH416(ZWX7O4JXl7gdXgptGe(EBM437pQOnGKrWk8IKtzujqya2kFpbL5Yj6(8JEpmsvnwTBtM9jaP9pW3lbOLR7mLEtctbTqzv)MIdpJ7)0T5qJfoccfaVqTT2emvkWbiTBO9PS7k0PyGJK9VQZJDYMdO(KhbEQAUEXBwZWMZxeJsGZ)PLAVC2AAXKuTNPUMW77IcVyE7zmgey)8tlwAHfjD48)rGafdUJJZyU85fWR540Xq8DVSSNMm3sIjhCNFPjpt3tov7LX2l88j(U3whYX)EoecEigRcKvCr9XpAfeD13SsF1iDGpNU2ARESWeNFq0rKnsfDIw55N0Qw66FwggkHkPVcEK1BW)exAp(eT4X(cW5lfM3otGvy0TwKiKnUD5cVQE0pcCn3Efu1z4b)rm23z)UjAcFFqtVQxa4AHYBeNyaHT8KeQ5iA9cqlEuk0hTyoaIOZV7Skd5Eg0Uq2NTRG5q8W(32V2bPDpfQRApbXk(bbMSHNsVt4Sk5LsFwO3term(3k5Z3m22CyelqtWDY8VwQFmkG5yoRTmGftQkW9KX1GMPA4pd(eYe7vn)F)AMedgTnAKI9Qh3YYqGJ1DMmMEBKt31dLFENPHHQTzpI)fYGkKrhL0pFfDzK)ZtCVz6MclGk0(6dc27rRcry86imi5ml0XaP7ml8X(jYZvmyjxyagr1Vdt0twUTnaOzwFwRr83XZ(KMKIV1nDHPB3bqlDcXd(euYSPvq5D77(gfyskia36fqIr3DQtvBEvvDBW37XNkOWTHb)qURjz5O9(ZadsQtymjfIcS6GLFVb6r8VOLLgrl)(dYZpCBYQx5tantvSIovwomG77Z3bSqQwQG5iHdk1lnqvvxaDCAFJ(nby2vkHY6lSb(Z)FfXGGM2ZKTLiaLvkw8Z4NxbZLpzxGtQX7enjTUFPcLnEtZ)NnTPpdgx6uBh10K4KnkLZmli1yWvkctLhbPgqZMXTSkge(iRiz4QwXfqNd2Be6)HEXzm)3YmUFmEFYBiRs5XBHBOv(o9oKW0RrDLfN91dDS8FUuW58bQSLe4L72y)EC8v(ROXksRjqeZJuGKLkFuGEMbNH3Xmw26eHKjJZUgoYGTSq0NGnP)lnV7FlQOC)hgNyFwkko(SSBA0e)YmyzGKo6IVmqACmYybknNGvZ8RH9FoSCup1T2iyDNvW9Qh2ehANq5nl3IKtJwfrwEmJtz9Cqd93OGxV55NQG6HMM2OrbR0KPK(Ncuu3vDxskg2x8XZGe8f9FJmBQwg2l39q(k94Kx7iDO2fkkdecpeMhxYizkBTcqYlTqkepF8Sj3(Nlw..76bb99f5a064c53ccb8224e76d94cecd2e937e393c95715bd910a16347b6e3bfbeb276e8d9ff8c79edbbb7fd0209dca815564f51b7edd6e5527230c71e8cb4ef737e8d9097bf3b84e5c34c8b23225dbd89a62e184ba6d0b4a9010651388b1470a88a6ab7cc926726daafbcee58448cb97d4004a9705e42b58bb4a74fd849cf2c",
        # "callback": "geetest_1677054485814"
        "callback": f"geetest_{int(time.time() * 1000)}"
    }
    resp = requests.get(url=url, params=params, headers=headers)
    # resp.encoding = 'utf-8'
    print('req31: ', resp.encoding)
    print('req3: ', resp.text)


# ==============================点击验证，有以下请求========================================================
def get_4(res1):
    """ajax.php"""
    url = 'https://api.geetest.com/ajax.php'
    headers = {
        "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Mobile Safari/537.36"
    }
    params = {
        # "gt": "019924a82c70bb123aae90d483087f94",
        # "challenge": "1a4f67a5dcf8342e7cd7b735e92e69e5",
        "gt": res1['gt'],
        "challenge": res1['challenge'],
        "lang": "zh-cn",
        "pt": "3",
        "client_type": "web_mobile",
        "w": "g4LhvDNS2LBR5GV0)pps2bpe82UFTTNqfYN82eIyDjjbTHAefaBqkDQ7KMv10Zdd8vX0jykIW5RsChPYLR3)UVz1q4Y7damDez5wxZHcAYyNC2B)uoESm3SoGZDT5vMgocB1LD)r9NZSAB4W4aJjTmUtYWZmOgMkXGctnp)LW8QVZK7(2wX0M(VLLRDxRFRcks5WAnSdOcIZNDCBmZg1(m1FrvEuD343RG3qQ9b0mp2BthrxGTq0MUGFvGj32B(NZOJ0sEcHAUsoXSpqu5OkDSuGwmxCjm7IvI4lt9n1HLKTnG5jGZt4gdBzfAH(RFA9k4AKfmjUVgqvGeLQcpyL24W8Q2W0Wi6U5iKP2UCvWdBao1MT1omcnPhyUpVKpfKiNIk1WluM)QHRLfKxPTUU4qqwnM)cvBPKfyyfvUVB1Ma3tTjyhgfhAplyfW6sY1SYRL3MMeUCmeSzACsZXAAy749wRNWtNw)7neAcKYTqLKS8odb4RjP4dQrZj3kxa)t7BEeqt6Ptrb767Dsd7WDqAeyQFwpiLEfmkzZDv3cIVXGhykUhcY9HL3cHFahHLMosH)RPMpN8j8EQTxZeaXldW(pcrfConXNlbwEoVqhqJlcVGFLI1J1SAIb1MBheNORv7dkh1qCj2s(OqQ4zKwoLrZ1(k3SzJa)lDbFgwTpUGkQT3(n(WkK3O55FGiCAujnYfBDnjN9LIj)tFLTmbHQDUcH5mKHpFft2814oH6bFxbBtScHSzq8xWCDdopJcAl8sNWxP8WBsZo5CEbonWV2K4)Yd0ZBkdMOnBR0C3Ju7DzD9kVdOoWDY4uM8t5rRwjcSFk(ADosh6gVZYWqj3eVqNVIezm7ij3)ergTMs5zjcihejRxdEzVpABffxpqc2Rr4X972dmM)iN06MNyySpW8ugAvkw20Nk1zbvwAGiASpH1J4K5A9BwJM)vfe44cwW567yYVoChiny5cFmXMC788SLcM3tx8PgKNsTxvXcweWfhTWPs3dQUMM1gamQqyW(OcncOMvgWXwmN8YBxLtHc6ydbWwvX2yW)s2rIoYh6Bq3I34nSKuPB8fIp0hTwIWNHz028e1(K6N6ojN37FgCR9lGWK6dZR4z3WAxh0BnZDMUeOm)Dhruh(Mi5zQ2nTxuhuf(XOMhcLn9WEuhKnepuYeYPrIFg5M2jCK6l1yAvru3Y)f(0SYxPlCf8tJwjFf4fnwltK7MN3VCVIVyU1)jmvMUvcWOKHfEfSA0dpS3o(0Zkzfh8SarBJuA7HShwzjo5u",
        "callback": "geetest_1677052125471",
        "JSON.parse": ""
    }
    resp = requests.get(url=url, params=params, headers=headers)
    print(resp.text)


def get_5(res1):
    """get.php
    获取验证码相关的图片：滑块图，缺口图，背景原图
    """
    url = 'https://api.geetest.com/get.php'
    params = {
        "is_next": "true",
        "type": "slide3", # 表示三代产品
        # "gt": "019924a82c70bb123aae90d483087f94",
        # "challenge": "1a4f67a5dcf8342e7cd7b735e92e69e5",
        "gt": res1['gt'],
        "challenge": res1['challenge'],
        "lang": "zh-cn",
        "https": "true",
        "protocol": "https://",
        "offline": "false",
        "product": "popup",
        "api_server": "api.geetest.com",
        "isPC": "true",
        "autoReset": "true",
        "width": "100%",
        "callback": "geetest_1677052119932"
    }
    headers = {
        "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Mobile Safari/537.36"
    }
    resp = requests.get(url=url, params=params, headers=headers)
    print(resp.text)


# =====================
def restore_img():
    """还原后台返回的乱序验证码图
    - 可通过监听canvas 绘图事件，找到对应还原图片的js代码
    """
    pass


def get_validate():
    """获取滑块验证成功返回的 validate """
    url = 'https://api.geetest.com/ajax.php'
    headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Mobile Safari/537.36"
    }
    params = {
        "gt": "019924a82c70bb123aae90d483087f94",
        "challenge": "e778330cd54877beac432673d841eac5dp",
        "lang": "zh-cn",
        "$_BCw": "3",
        "client_type": "web_mobile",
        "w": "lv4NEf2D0pezssjBTCIzjP(WJt7(xt1Y4fGfHXl4xWjzso7lD3GEapj5mvfUzLW)c1UvRl5SFDVdfD1JayYqI4Pqw7deqpkbGHLrQyUyhyKF5bBnhzf)OGlox95ZkVEQpwjSY1XPx6AbDD76ibGweLWSyzXTfTOiw9sfNOfjjNe0Pnn)Sa3WYHV8Boy5QZzeNJPiAk(q85)RQ)2snYNPpFAG2jsT)25TN00wt1Lt482)HbaKKBVq5h8GXFlWAGXucXOOvX(wsL9XGcKuoMUOE8RrpBCMwvDUglKP13PpI3XKhsOdIBGvbn(MWBlk)DKBIaI2en1RvVvSckxZou3QOADdvHhPy85i9Sl38aycpGvAJiBWc5v8K0NQ5wbUpzbjBWU2qUPyOTp8ogYmvR5nXPvkyUALgFg5AomzzLYveQTFPOXWZuzNkDzBUccSYgS140t)P7TaniZEl)w8ooUoNIbz6eclGHShdYfxoqsnb2vlY7ZuaPZZUayrbPh2mHAmARqGQ(jDYbLFM4Shal6JrCeRlWgfpSnJyAaQYQzx5emr37089oOueNc01lPhYac9rKj(8a9CiGoj8IIyP7e)a4x1ruFUcwBIU2i02ibmUH56yfZYf)DIFVsh1hjUlpGutmoUtZnRpgqoELyHUtXNGzMaQQjv)DXYmUlagJj6zo)v8yiLkKUUtw5ZoXoGnXRhguAsrcW09)vr0tbfYYEROLps46a9BNIqwtLA9qby5TZYP(PgXMVsxYdYFqNNtr2NwgtW762KY)XchzPybIa0ddRmmInW1(YsAQ3PBDUl2jzTxuI4MHaZvsJUPXULYjqLw)wLb2G7n7324UWIjbG0kCTMOjXknECDe0FXRHKFhfX8i884itvKDB3NYjjJLOpa9957d9e6c163121948cdf2fc04e52161912c5a116ae03cd9194a204c9b4be9afcfab4a12098a9af931640d61121f93868f2b3d65dd8b95e0c588c04f9b9e2c342724c57e77c3aabcd54f08f48132fc284d8728bfb59d4385071d7e193c45ea3546163fc1f60050c17439993570c6b8a52af361000dfd3bbc2704b76666ef9938",
        "callback": "geetest_1677144493094"
    }


if __name__ == '__main__':
    res1 = get_1()
    res2 = get_2(res1)
    res3 = get_3(res1)
    # res4 = get_4(res1)
    # res5 = get_5(res1)

""" 通过破解js来过滑块验证码 """

import json
import re
import time

import execjs
import requests
import ddddocr

from a_code.A013_极验_过滑块.handle import restore_img, slide_track
from a_code.utils.ut import compile_js

# import subprocess
# from functools import partial
# # 修改编码方式，windows 默认编码是gbk，Mac 和 Linux 默认是utf-8
# subprocess.Popen = partial(subprocess.Popen, encoding='utf-8')
# TODO: 备注问题：这里需要修改 c:\python38\lib\subprocess.py 文件 __init__方法参数： encoding='utf-8'


# ======================== 1. 初次进入极验滑动网址， 有以下请求 ================================================
def req1():
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


def req2(res1):
    """gettype.php
    返回一堆 js 文件
    """
    url = 'https://apiv6.geetest.com/gettype.php'
    headers = {
        "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Mobile Safari/537.36"
    }
    params = {
        "gt": res1['gt'],
        'callback': 'geetest_1677050515844'
    }
    resp = requests.get(url=url, params=params, headers=headers)
    print('req2: ', resp.text)


def req3(res1):
    """get.php"""
    url = 'https://apiv6.geetest.com/get.php'
    headers = {
        "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Mobile Safari/537.36"
    }
    params = {
        "gt": res1['gt'],
        "challenge": res1['challenge'],
        "lang": "zh-cn",
        "pt": "3",
        "client_type": "web_mobile",
        "w": "cx5PhynwYxqS2KYDFbPW1xz7vgy(4PknC4ov3MoOnLLlOLcLV4qm5SNHyn6IYz2T8mW4rsk9XdB45wpDCVm070eO5gFwFuraYq0eIw9b0rS2JOoqCQpm5jye1ORvBS4q1Wr1ias0iO2Un7ZvrMUQD4j)slZ1TvgD6N6BP)0)yzlX73l(VtxTmOkVwlWHYGLO0qVmf9MmuWiDFgka5cj2BW0lbW(UiHB9YlQEwxAZQuwyCs6fEngRUMbIxrn0c1Vunu3vvq9fiRsSw2wf8kOrB75oRcUmwOWaQLsE4LTYnnyj7vfE8DFNyQZFIdjRut4wsFA(eKvCR2aNoW4AQUUBVIvkqOQmFcDHhFKwXTp6yRGyqwkcMXbCgW3DO5CopySIFUdTR17(FjFAHZJ6B7JzNH5JttFhOWH6rfiowH8LOfvuQwxYriGyKuwS5QwSeXucWU(7Cu50RPBzeeNtL2s)OfdSItUJXwEj(u23Xga1L16Vy8z43Na3h0BEh0mYYHop8XiOGaWUS5Dac(eMZSqkn2L2BD1wVO)MMiffTJleBN3W89n(n(X2CQmte9OP5x6MQ)7(GHU5czwlpAJjO5l3d)FtkehE8(uRcuaT0cuA)CEV0qqDpwO8I6(ooQOl0TuH(HXpDgtkfAncyB7cfIRQSOb580SoYXDIkw3YUVEkan5S)BmbDzDGP76zEqUAzM6uiIiQ81yS9zdF11OXok6K1Cjv1hyIBHVx1fb5ZbsMOQyI8DDXD4eSVKEk8eB6C9LZtze1OzDOG9fwN9BSm5)ppBWOLGwr1u31nRJAoxlMQOygHaLMu(OYOrGtgUzvEs8JfkU)HZdic7f1OREWXterEqh8Z)gQxd1t1yLfGjC915LR3vq6ZZhzy)J5XrEZ0M4xTfBD3BaRI3ntQuXW9cvCzekOYMWFnUUJs0ACTgg6e1NSTCH416(ZWX7O4JXl7gdXgptGe(EBM437pQOnGKrWk8IKtzujqya2kFpbL5Yj6(8JEpmsvnwTBtM9jaP9pW3lbOLR7mLEtctbTqzv)MIdpJ7)0T5qJfoccfaVqTT2emvkWbiTBO9PS7k0PyGJK9VQZJDYMdO(KhbEQAUEXBwZWMZxeJsGZ)PLAVC2AAXKuTNPUMW77IcVyE7zmgey)8tlwAHfjD48)rGafdUJJZyU85fWR540Xq8DVSSNMm3sIjhCNFPjpt3tov7LX2l88j(U3whYX)EoecEigRcKvCr9XpAfeD13SsF1iDGpNU2ARESWeNFq0rKnsfDIw55N0Qw66FwggkHkPVcEK1BW)exAp(eT4X(cW5lfM3otGvy0TwKiKnUD5cVQE0pcCn3Efu1z4b)rm23z)UjAcFFqtVQxa4AHYBeNyaHT8KeQ5iA9cqlEuk0hTyoaIOZV7Skd5Eg0Uq2NTRG5q8W(32V2bPDpfQRApbXk(bbMSHNsVt4Sk5LsFwO3term(3k5Z3m22CyelqtWDY8VwQFmkG5yoRTmGftQkW9KX1GMPA4pd(eYe7vn)F)AMedgTnAKI9Qh3YYqGJ1DMmMEBKt31dLFENPHHQTzpI)fYGkKrhL0pFfDzK)ZtCVz6MclGk0(6dc27rRcry86imi5ml0XaP7ml8X(jYZvmyjxyagr1Vdt0twUTnaOzwFwRr83XZ(KMKIV1nDHPB3bqlDcXd(euYSPvq5D77(gfyskia36fqIr3DQtvBEvvDBW37XNkOWTHb)qURjz5O9(ZadsQtymjfIcS6GLFVb6r8VOLLgrl)(dYZpCBYQx5tantvSIovwomG77Z3bSqQwQG5iHdk1lnqvvxaDCAFJ(nby2vkHY6lSb(Z)FfXGGM2ZKTLiaLvkw8Z4NxbZLpzxGtQX7enjTUFPcLnEtZ)NnTPpdgx6uBh10K4KnkLZmli1yWvkctLhbPgqZMXTSkge(iRiz4QwXfqNd2Be6)HEXzm)3YmUFmEFYBiRs5XBHBOv(o9oKW0RrDLfN91dDS8FUuW58bQSLe4L72y)EC8v(ROXksRjqeZJuGKLkFuGEMbNH3Xmw26eHKjJZUgoYGTSq0NGnP)lnV7FlQOC)hgNyFwkko(SSBA0e)YmyzGKo6IVmqACmYybknNGvZ8RH9FoSCup1T2iyDNvW9Qh2ehANq5nl3IKtJwfrwEmJtz9Cqd93OGxV55NQG6HMM2OrbR0KPK(Ncuu3vDxskg2x8XZGe8f9FJmBQwg2l39q(k94Kx7iDO2fkkdecpeMhxYizkBTcqYlTqkepF8Sj3(Nlw..76bb99f5a064c53ccb8224e76d94cecd2e937e393c95715bd910a16347b6e3bfbeb276e8d9ff8c79edbbb7fd0209dca815564f51b7edd6e5527230c71e8cb4ef737e8d9097bf3b84e5c34c8b23225dbd89a62e184ba6d0b4a9010651388b1470a88a6ab7cc926726daafbcee58448cb97d4004a9705e42b58bb4a74fd849cf2c",
        # "callback": "geetest_1677054485814" // 貌似写死就行
        "callback": f"geetest_{int(time.time() * 1000)}"
    }
    resp = requests.get(url=url, params=params, headers=headers)
    # print('req31: ', resp.encoding) # 本身就是utf-8
    print('req3: ', resp.text)


# =========================== 2. 点击验证，有以下请求 =======================================================
def req4(res1):
    """ajax.php"""
    url = 'https://api.geetest.com/ajax.php'
    headers = {
        "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Mobile Safari/537.36"
    }
    params = {
        "gt": res1['gt'],
        "challenge": res1['challenge'],
        "lang": "zh-cn",
        "pt": "3",
        "client_type": "web_mobile",
        # pt 和 client_type 有时会是下面的值,但不影响
        # "pt": 0,
        # "client_type": "web",
        # 不能给 w 参数, 给了会请求失败, 提示 "param decrypt error"
        # "w": "z2UnFOByzXLEMxzejuLobBLu5AWhN0i4yKuCYakBPBiBhT8BEqlujT16UfBAvOFD6yqmK13x2(PKUPqD0Qs8tJJPl0XYaQxoH7dO2XIliuaKH4XahP0A4CUDU6EibpAyfV4r4wQumqHOD8UIx8LDv2)MUAMIuNdVEiTpZIG9iH7LL6ckSh8saWuLX3J8FXUMhgVN(JZcrA1ue)DvpdivMxY6I20xDpnLCxOiwll(Yf9CMb6N8tFKVvbdp4kh1gf8FW7h3Kq54yaL2Nq3UqopJeu7O9O92GI0Vy(0MWR0zuAjXa(NeoMZPx5BQzVu9xdffRFSqUWN1nYyxHLzj7m7CBNEK9Lev)FvKdAwTBvKb2fgOJnidS)6f9Q68KLK0x5uO(KgnS5)PccBF9eGkYTEPqdlaqHXE)Vcq(sD0a)mq4a0es)sKHinauHIGAqekxHG98jVSKuURQQ2kwpr6QST98)M)Iy4dreOAcNOIY4ij4AyNRfk71fY5I4LnfihHbCHkLxitZ9L5V49Xx)lwewKxtQqPEO)5S(FvV8vx0K2qG5LnByl(r81nmmNdFFDNd7JmSUN(o3Ga6dgGrKqXFnvg06kUT4oNUupSEvna1iR5hcWsAAvCJCQo6MOo07W2UsTRz2r)7q6ze1qtNd6r6luYXqb)B)3oswcGIq3aIXk9Xox5wO7wMhwHz8daY1WXhU99MqY)kG(4xP1L51kaIdY1)DKAXtar)HIqGswNPe5qR2NB)GvOvMrh35gn5lziXWLPucU3IAmJZdCbWSkwvRF9TRdXHIkHkl7n48m4DUt3KqbeRCzPDLSWGDpZAzno7LqhTG2pqNb)DJOyMQ0)XZIparO1jsCqMoZ0aIsM3owqXzS7UJ0EGPO(A72xaSjuh6zEWy5Sd)z4jXp(TAx5ybR6QyWpRLmaLKzZG(HrO7CctiyMPKy5KgFOMmHmTBB(ZPZzK1fJAlnnlp17Ib5Tx8A1o7CEK0P7XXuPzTWg4N50wtKleSpmczDszFjQmkk7fdhfA6L4TWac)BVWNDjRR5(GTFtiBlosNeOeK(ZX7fRoB01ZA9lvWzoNM6WbLA)LGOGYfXMIzP27Qpz3xgjtwiwZMolTMkiYQlHRthYmGPRhJ0PqMGdns)rmP(gCmuw0jgpAhFphStWlxtfmcVtDKeotlCpOrVWejc)zCs5edFcqZP2GzqZ5vemoLOfHNif7qHKGHPOQY(zDGfCkDLWMKzVyvDBKHuvHearVz7va)46iaTfdAdkfadaDqPBZR4b2vt3DkUbxNo20YxtlHaA8TWpGHukvXruJg8DZLMrAuTxzK1NSnkmiwoaiDWOOy9SCQCzJcOROtoRAGXC5DLJaBn40BUxdo(4EfyAPkpw8ZDQe2wCCp6SOx8jxpH7ITS4tMKmXY8LhYTis(lj1LivNVRrYTfSoO4CHK3SWOpwocR4J4DDo)KwMqGXOSXFL2ENe3tYv6F6Iz7puB(YAB)Xf5PSQxtUTi8PyaDZSdri7s7viuEdaxd2H4p)lHm1o5Aqpbxz2ALuJiaaozqGID60BWUCB7w45nUjhsZM0wf3l81NtWVXEU6J)(tTrz5NC7f(6dYrpN0RzHMNqnXCsNbkeqevzvqiv1M5t49Sf8)y)cx(OoS2ZG0cR7tR4Lhgms5zfirW1(IFBLeBp31j7(FMdFyMsAuhqIpaRXOwrpFzdSpd3EQIxhFUQ(yP7ewM2tjc(TRNHmYPOfVuVDdnFVFqAcu1hcHGZrVvRygO2wSaYjEqeJuTwzlgQ0PlB51dfWlvoVwCrHqMqqttYr(rp7rkl8WdWw..",
        "callback": f"geetest_{int(time.time() * 1000)}"
    }
    resp = requests.get(url=url, params=params, headers=headers)
    print('req4: ', resp.text)


def req5(res1):
    """get.php
    获取验证码相关的图片：滑块图，缺口图，背景原图
    """
    url = 'https://api.geetest.com/get.php'
    headers = {
        "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Mobile Safari/537.36"
    }
    params = {
        "is_next": "true",
        "type": "slide3", # 表示三代产品
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
    resp = requests.get(url=url, params=params, headers=headers)
    print('req5: ', resp.text)
    res = json.loads(re.findall('geetest_\d+\((.*?)\)', resp.text)[0])
    return res


# =========================== 3. 手动还原验证码图片 =======================================================
def parse_bg_captcha(res5):
    """还原后台返回的乱序验证码图
    - 可通过监听canvas 绘图事件，找到对应还原图片的js代码
    """
    base_url =  'https://'+ res5['static_servers'][0]
    full_bg_url = base_url + res5['fullbg']
    bg_url = base_url + res5['bg']
    resp1 = requests.get(full_bg_url)
    resp2 = requests.get(bg_url)
    full_bg = restore_img.parse_bg_captcha(resp1.content)
    bg = restore_img.parse_bg_captcha(resp2.content)
    return full_bg, bg


# =========================== 4. 识别缺口坐标位置 =======================================================
def read_img(bg, full_bg):
    """进行缺口识别"""
    slide = ddddocr.DdddOcr(det=False, ocr=False)
    # with open('bg.jpg', 'rb') as f:
    #     target_bytes = f.read()
    # with open('full.jpg', 'rb') as f:
    #     background_bytes = f.read()
    # res = slide.slide_comparison(target_bytes, background_bytes)

    res = slide.slide_comparison(bg, full_bg)
    print('==缺口坐标：', res)
    return res.get('target')[0]  # x坐标, 即滑动距离


# =========================== 5. 模拟生成滑动轨迹 =======================================================
def get_slide_track(distance):
    return slide_track.get_slide_track(distance)


# =========================== 6. 模拟滑动行为,请求获取 validate 响应参数 =======================================================
def get_validate(guiji, res5):
    """获取滑块验证成功返回的 validate """
    exe = compile_js('slide-js全扣.js')
    w = exe.call('get_w', guiji, res5)
    url = 'https://api.geetest.com/ajax.php'
    headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Mobile Safari/537.36"
    }
    params = {
        "gt": res5['gt'],
        "challenge": res5['challenge'],
        "lang": "zh-cn",
        "$_BCw": "3",
        "client_type": "web_mobile",
        # "w": "lv4NEf2D0pezssjBTCIzjP(WJt7(xt1Y4fGfHXl4xWjzso7lD3GEapj5mvfUzLW)c1UvRl5SFDVdfD1JayYqI4Pqw7deqpkbGHLrQyUyhyKF5bBnhzf)OGlox95ZkVEQpwjSY1XPx6AbDD76ibGweLWSyzXTfTOiw9sfNOfjjNe0Pnn)Sa3WYHV8Boy5QZzeNJPiAk(q85)RQ)2snYNPpFAG2jsT)25TN00wt1Lt482)HbaKKBVq5h8GXFlWAGXucXOOvX(wsL9XGcKuoMUOE8RrpBCMwvDUglKP13PpI3XKhsOdIBGvbn(MWBlk)DKBIaI2en1RvVvSckxZou3QOADdvHhPy85i9Sl38aycpGvAJiBWc5v8K0NQ5wbUpzbjBWU2qUPyOTp8ogYmvR5nXPvkyUALgFg5AomzzLYveQTFPOXWZuzNkDzBUccSYgS140t)P7TaniZEl)w8ooUoNIbz6eclGHShdYfxoqsnb2vlY7ZuaPZZUayrbPh2mHAmARqGQ(jDYbLFM4Shal6JrCeRlWgfpSnJyAaQYQzx5emr37089oOueNc01lPhYac9rKj(8a9CiGoj8IIyP7e)a4x1ruFUcwBIU2i02ibmUH56yfZYf)DIFVsh1hjUlpGutmoUtZnRpgqoELyHUtXNGzMaQQjv)DXYmUlagJj6zo)v8yiLkKUUtw5ZoXoGnXRhguAsrcW09)vr0tbfYYEROLps46a9BNIqwtLA9qby5TZYP(PgXMVsxYdYFqNNtr2NwgtW762KY)XchzPybIa0ddRmmInW1(YsAQ3PBDUl2jzTxuI4MHaZvsJUPXULYjqLw)wLb2G7n7324UWIjbG0kCTMOjXknECDe0FXRHKFhfX8i884itvKDB3NYjjJLOpa9957d9e6c163121948cdf2fc04e52161912c5a116ae03cd9194a204c9b4be9afcfab4a12098a9af931640d61121f93868f2b3d65dd8b95e0c588c04f9b9e2c342724c57e77c3aabcd54f08f48132fc284d8728bfb59d4385071d7e193c45ea3546163fc1f60050c17439993570c6b8a52af361000dfd3bbc2704b76666ef9938",
        "w": w,
        "callback": "geetest_1677144493094"
    }
    resp = requests.get(url, params=params, headers=headers)
    return resp.text


if __name__ == '__main__':
    res1 = req1()
    res2 = req2(res1)
    res3 = req3(res1)
    res4 = req4(res1)
    res5 = req5(res1)
    full_bg, bg = parse_bg_captcha(res5)
    pos_x = read_img(bg, full_bg)
    track = get_slide_track(pos_x)
    print(track)
    # track = []
    # res5 = {'a': 1}
    res6 = get_validate(track, res5)
    print(res6)


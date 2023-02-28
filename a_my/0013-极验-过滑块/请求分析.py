"""请求分析
============ 进入极验demo地址，有以下三个请求（https://www.geetest.com/demo/slide-float.html）=========
1, https://www.geetest.com/demo/gt/register-slide
载荷：
    - t: 1677144355848
响应：
    challenge: "e778330cd54877beac432673d841eac5"
    gt: "019924a82c70bb123aae90d483087f94"

2，https://apiv6.geetest.com/gettype.php
载荷：
    - gt: 019924a82c70bb123aae90d483087f94
    - callback: geetest_1677144357843
响应：
    - 一堆js文件地址，包含了重要js文件 slide.js

3，https://apiv6.geetest.com/get.php
载荷：
    - gt: 019924a82c70bb123aae90d483087f94
    - challenge: e778330cd54877beac432673d841eac5
    - lang: zh-cn
    - pt: 3
    - client_type: web_mobile
    - w: m7HnCD5ziwUYIxSq8W)hZiT0vo(bxv(ILy5JAdmXhvlqmdF0KWB1XTdxStWxg(BJHJgn13OxeeYxnn10Ar(KsajG)KcZ13rHxIk6S8EBar2F1AJJhV36MVDFzPdsFC6yiYuVHFlxq0D90kX86MEQzb8sBGlBw5iz5SaeS1nGuak19V9pVo8zka7HEyM6ik29xiQOzvuwchFflldwTSU)y6bFkaw0CU1ge(e2sK)giqyadeoxLWH3PTI8I2SqwQTKMVGl2o(jRgOOK56Ax4CdArZoSw5Or73Q77lOlWOP9PWEKWZrThCW4DgP7)BY(6dFgRr9)kSq7YxGvPGokWyN1JpZeDSZRoN7h0kiT5Ku4b(VZumDaK(O1RYeIJEh91OHBhilbsVW6uwRiEG(7OTiOs)WlGSSL9bUxeQ1xgNnkjfa6ViofU19KSBGCdTInzWsi5hr(Omw)CAj(rTzO4JEsp(SM8pAsdwnmJ9wsbR8MLrZyORjzeElO66KL5O(kSy1td6M29RYzs(jlstMyIOMEytNqiZ()pDerymtJsdE8A)CJ5Xu5kU9GozdFEMUMjuiF0cXxj5EfeRcvpLXdxHEFMe0RU)Elrgx3w8v(QHRjqg(rfeZ9u3V61Ij2AIssJ3wl)YMM81e4oWxwNGo4NcMUcNjLancPkuJ34Rs6emhSm8KEEhatJrPB6G(NssOkPdcNdJM0RMfH2cmemuqbXuG7qC6SJlyp225sdb8NyWL)aI1Lon7Zaf63kv31OH(0lUZC11(bnyGIuuTQ9O)NsydzZ7LdMW14tqT2fodEPMlTgDxqXMwWilf7bNJpH2mNXK99hxUrY1lJzqTqXw6PrDlqnERKdFMrpnJ4kczo2Ww5qdC4ATrdmwVyyzAHMAvoondYJEIoXXMNy3NgScgMY6Q))(mq6SXszmIhByjdGwDYHIyakfgrtLWRtRkvikm4vSux0FbExppZEl9teUqJwpy3TiwmR2Yc)WDsapRxNLxQIMeTkQm)pGjm0BNcrVfOsTNH6Z(9kb9CHW9Mrg9MfzRFiNubgredxQqPr5mp8k(Xf52UC)N4G3PCzkU6lzE5XHW0v(qmY(kB7c1L)m3EhTbO3Uc30soJ1gt752HMpRZzax9iKMl4CAaycuvNoMTqI)QSOgThRojRWwZ3f2JLxTlVRfR2UIVsTNsCCXZjv(YDNRKrJpgl2tWRx8f7yK65yY3qakGOplL6YvtlvmsMirHprQJMicsvvDy0fxnVNINAcBqteqEBm4JCmAsRj6zmRGCk9pMqkXJQEKxm2pacVWmPR3qNS0qKwfpaSXJHs)6B57G0XX74SEnMSS0h1s(RG1Jl)5kcKf9xHcUDuHJ9X6sgTqHel9y9VBYUPX59mMumG1wDXNcYeEr8(d0G9xWjq2T)9WlRFxDryhgUbeyuegZpe7WeyHtETu41TLCXAP5zJsQlijRov0)mpiJE1AJOI6pVul)GR87HIFc8ZAFuWyteeUtv0kc4jJomlToroB1ahFpWyDdwc2ju1l9J9k(qn2qxdGeOPXHLYxvldRUil6qSRo14(BBQ(2ShggsdzSGbO4eFzGJPD0L0X5TaALyhduMMT97fm2TP62A68hXeZSl1KkExYKQxYxv4mkrVJznAVA8J24t63Z6CdM08yESGpbu0m57yBKUPltwziCOdaRtNTEtfAO1f69fKID))4R69tddkBCWsixVBjfWqp1xGxioxD9UGYYsIaWBn6eGp)ZczBiNV65OXjhTqS0G8ww77qoAsCUAKzEvuiCcd3HYA9dS0foRiS0Bbh9st55pGtgszIQpVD8SpUACnXxdHFGs3J78q9c0r6riCP9JRsTH07p)3vSm4Rr(pMn02jKLMhnuxzEjj41Qd422dr5Fq3eASrlzIXV64WBEzn0OAjU0cPh63bECvVRvmXr26WkgQ5qvsWvq0EnVAAMQa4W9RukHMOhtFrw(ZwJPC47x678an3gjtUO(zdkpzDOqjLotCBmwgZ1fjtoa81De521cgQOJxw6IbxhvDKtVGBSeYciFZ71Bqo1XHNaIWcpg()0uruQ4owQFICKnPYWbsHEQRjs8oP5BpfKvh2Vm9I5CZq25HxESFmee610m8DX2TuFb978VgDALjLxacY8kWSsRCKyth4uhRIB1Tsh52HCECvjfNZAV7xy(XigTOP3voLi(zEbaq1rZFMmlLRloL9WdQTBXz9CYMBuuKGkvj5Rz1aQNXFURQX9PlEQKhtZQXo7Ccl6qGg..76c08ec51c964e2dcc2401da7a11140dd157309893b93abf65d326576bdbc3ea418c999777865aa55f92bbeb94bea4672f70c581b67593b38974339780efe834ce7fd7c68da528e0c4489668e3a758b842ac12ddb2bef1a7fe9a805c83412c7be4f106165a1e92d72cde8f689b39a5d5d2df4614595900a93033becc97b6018a
    - callback: geetest_1677144364405
响应：
    - 返回一堆数据，js破解需要用到
    - 有图片域名："static.geetest.com"

============ 点击验证，弹出验证码，有以下两个请求 ==================
4，https://api.geetest.com/ajax.php
- 用于请求生成验证码；
- 这步之后会加载 前面请求返回的slide.js文件
载荷：
    - gt: 019924a82c70bb123aae90d483087f94
    - challenge: e778330cd54877beac432673d841eac5
    - lang: zh-cn
    - pt: 3
    - client_type: web_mobile
    - w: 6)OyAOQBSzItmdcDYlaAspxKARtjuBiOYW8OijkVZy7Kke4KojZB3CoMBUXvFs4yUZLIsa1JGFZU6WaWahdNjfRO(Af)lOg6ViExrMjAzpktUBAbeRpf8VJqXh120CseGyDXmslEAeyogj3Qb7kE9QcQ2KKrYSW11c4UruO2svggTGVkoHFctijikwJh3VT1ivWI4iIJqDVcff1j7Yaxf(grgY77kos7mf6rYciDnBzfWcWLxuvhrz6u3DjrkJ8q0cl6R)hojFD0MNccxTvzH6Xi5Oh8OcKR4r4YyVtciq3L2yFYgDRWMb9vEB01TMvPcq3SJiQFdPov1ofe0p75xP8oRPLAYLLgiAjtmC1)g4rM7L2mqPcjb7gbioRji22g8zMilFeLtYrji)nNqj)XFh58JC0Un3jUNPt6HoSbxO)aiRFAsVxDIdCq6bC7vzSEQCoyTZ3E0fA9l8IMbmRSh2rbfSdNYDhWWgYpwUJcFgf5Q59tz2EIpqBUDRL94SRtR8iV3MZaZ71CQdGmF1TauqO2F74QDgBP4zFLg8JbjkdBYVuGQXprlytg55Hl5958WhSIr6IvP)RQI)HICH)H6BFvUBFi79BLubAZfoYPdiNGJ1HQw71QaGBr7HJe8Bxzd7eKUmeaxGQZlBR3GpsQCSxWM1U91KSwSjuk8d2xN6NDMivqTREn0Y39YgYWk1FVG3PYvKL2oamH7T8YUgkBUOvK3C9YRW31KDgZn5(h8RGk9b8ZBazuCoHxuLbTua0(GM9CXWYjxYxHEn8krM1d)o17GLe)0RbGtv9K2tam2zCZfjs9(HaCD8hFEsu4DuNDVBUeQ(x4hc4)7KvcCM3q5MR0R4hyM1YfL5814LmqoKW1WeaiKp6fE)1QSYr8EEQjnfeSD3p7ck4HTVWo)AIm)5wzfDTAY6DJ8Wnmu1zUXCnI0u4p5TPNtQ6iBlecIYH03kY5DgmeoXlDhhdF(lwirwNmQEe3Chx15ZPH(ATslBLqVYZTbJUt5py4AI7pIq1rR(qnaRdfIXwxwtqOkshW)SE4zi5xAcHBJVTC(Y0ms4O(KAX1H6r)7Z)UHb)5jszwQBB6QFUGj5dmo6Q(USYmCTwX1Qu18GkK(MqYdrwqrc5lft27xRBYVAZGCIEvMrljtSShG(IoR1MbiycAtUCOxYci8nfNpbN3KZv2u4RXKNAYBLwoXrn(FcNcEZJIKdvascF2S2Da3blyZqE(CXK0K0VIPYrbkF)P1rbOYvFVZDIxwW31kvkhGjrJOrF)8ovf
    - callback: geetest_1677144464514
响应：result: "slide"

5，https://api.geetest.com/get.php
载荷：
    - is_next: true
    - type: slide3
    - gt: 019924a82c70bb123aae90d483087f94
    - challenge: e778330cd54877beac432673d841eac5
    - lang: zh-cn
    - https: true
    - protocol: https://
    - offline: false
    - product: popup
    - api_server: api.geetest.com
    - isPC: true
    - autoReset: true
    - width: 100%
    - callback: geetest_1677144465538
响应：一堆地址
    - 包含验证码图片地址，包括 背景原图，缺口图，滑块图
    - 返回一个新的 challenge，在原challenge后加了两个字符


============== 拖动滑块验证 ==================================
6，https://api.geetest.com/ajax.php
- 获取验证成功的凭证信息
载荷：
    - gt: 019924a82c70bb123aae90d483087f94
    - challenge: e778330cd54877beac432673d841eac5dp
    - lang: zh-cn
    - $_BCw: 3
    - client_type: web_mobile
    - w: lv4NEf2D0pezssjBTCIzjP(WJt7(xt1Y4fGfHXl4xWjzso7lD3GEapj5mvfUzLW)c1UvRl5SFDVdfD1JayYqI4Pqw7deqpkbGHLrQyUyhyKF5bBnhzf)OGlox95ZkVEQpwjSY1XPx6AbDD76ibGweLWSyzXTfTOiw9sfNOfjjNe0Pnn)Sa3WYHV8Boy5QZzeNJPiAk(q85)RQ)2snYNPpFAG2jsT)25TN00wt1Lt482)HbaKKBVq5h8GXFlWAGXucXOOvX(wsL9XGcKuoMUOE8RrpBCMwvDUglKP13PpI3XKhsOdIBGvbn(MWBlk)DKBIaI2en1RvVvSckxZou3QOADdvHhPy85i9Sl38aycpGvAJiBWc5v8K0NQ5wbUpzbjBWU2qUPyOTp8ogYmvR5nXPvkyUALgFg5AomzzLYveQTFPOXWZuzNkDzBUccSYgS140t)P7TaniZEl)w8ooUoNIbz6eclGHShdYfxoqsnb2vlY7ZuaPZZUayrbPh2mHAmARqGQ(jDYbLFM4Shal6JrCeRlWgfpSnJyAaQYQzx5emr37089oOueNc01lPhYac9rKj(8a9CiGoj8IIyP7e)a4x1ruFUcwBIU2i02ibmUH56yfZYf)DIFVsh1hjUlpGutmoUtZnRpgqoELyHUtXNGzMaQQjv)DXYmUlagJj6zo)v8yiLkKUUtw5ZoXoGnXRhguAsrcW09)vr0tbfYYEROLps46a9BNIqwtLA9qby5TZYP(PgXMVsxYdYFqNNtr2NwgtW762KY)XchzPybIa0ddRmmInW1(YsAQ3PBDUl2jzTxuI4MHaZvsJUPXULYjqLw)wLb2G7n7324UWIjbG0kCTMOjXknECDe0FXRHKFhfX8i884itvKDB3NYjjJLOpa9957d9e6c163121948cdf2fc04e52161912c5a116ae03cd9194a204c9b4be9afcfab4a12098a9af931640d61121f93868f2b3d65dd8b95e0c588c04f9b9e2c342724c57e77c3aabcd54f08f48132fc284d8728bfb59d4385071d7e193c45ea3546163fc1f60050c17439993570c6b8a52af361000dfd3bbc2704b76666ef9938
    - callback: geetest_1677144493094
响应：
    - validate: "16f609f4af675be5300da3a7bc9adc00"    // 最终就是要获取它，用它去请求目标数据


===============================================================================================================
重点分析 请求6：
破解 w 参数：w = h + u;
w被unicode编码了，可以搜索 "\u0077"




================================ js 分析 =======================================================================
var u = r[$_CAIAt(754)]()
  , l = V[$_CAIAt(353)](gt[$_CAIAt(218)](o), r[$_CAIAt(756)]())
  , h = m[$_CAIAt(782)](l)
  , f = {
    "\u0067\u0074": i[$_CAIAt(104)],
    "\u0063\u0068\u0061\u006c\u006c\u0065\u006e\u0067\u0065": i[$_CAHJd(182)],
    "\u006c\u0061\u006e\u0067": o[$_CAIAt(116)],
    "\u0024\u005f\u0042\u0043\u0077": r[$_CAHJd(665)],
    "\u0063\u006c\u0069\u0065\u006e\u0074\u005f\u0074\u0079\u0070\u0065": r[$_CAIAt(667)],
    "\u0077": h + u
};

目标位置： h + u
需要破解：u, l, h
"""

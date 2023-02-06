# 分析 JS

"""
# 需要逆向的函数 decodeData 函数名 A
const o = mn["a"].decodeData(n, gn["a"].state.text.decodeKey, gn["a"].state.text.decodeIv), a = o ? JSON.parse(o) : {};

# A 函数 ==> 解密函数，AES解密
A = (t,o,n)=>{
    if (!t)
        return null;
    const a = e.alloc(16, m(o))
      , r = e.alloc(16, m(n))
      , i = c.a.createDecipheriv("aes-128-cbc", a, r);
    let s = i.update(t, "base64", "utf-8");
    return s += i.final("utf-8"),
    s
}

# gn["a"].state.text.decodeKey:
'ydsecret://query/key/B*RGygVywfNBwpmBaZg*WT7SIOUP2T0C9WHMZN39j^DAdaZhAnxvGcCY6VYFwnHl'

# gn["a"].state.text.decodeIv
'ydsecret://query/iv/C@lZe2YzHtZ2CYgaXKSVfsb7Y4QWHjITPPZ0nQp87fBeJ!Iv6v^6fvi2WN@bYpJ4'

"""


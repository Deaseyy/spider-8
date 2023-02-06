// t.headers["x-tif-signature"] = r(f),
// t.headers["x-tif-timestamp"] = s,
// t.headers["x-tif-nonce"] = h,

function i() {
    var e, t, n, i = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ", r = "0123456789";
    return e = o(6, "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"),
    t = o(1, i),
    n = o(1, r),
    t + n + e;
    function o(e, t) {
        e = e || 32;
        for (var n = "", i = 0; i < e; i++)
            n += t.charAt(Math.ceil(1e3 * Math.random()) % t.length);
        return n
    }
}
console.log(i())


// // 载荷参数
// body = {
//     "data": {
//         "data": {
//             "encData": "DAC536D90758AB68AF4373A349F3BBDF4CE34C33DC32F1068E9E23CA546C9EA8E639B26A7D25A6C1B97CCC02DDB933E477A9AAE02ED054FCBFB6DEA99372702FE64D17BF28F141090CC5289421E593DD"
//         },
//         "appCode": "T98HPCGN5ZVVQBS8LZQNOAEXVI9GYHKQ",
//         "version": "1.0.0",
//         "encType": "SM4",
//         "signType": "SM2",
//         "timestamp": 1675237317,
//         "signData": "DitO6d6O8oyO8NiXQbeSA2bxX0Iw+fl76yT72empkT1SFHivjr7lmoNfLa6THo4ouzq0EG4HBoiPyp2ZU4K8TA=="
//     }
// }

// // 代码中写死的一些值
// l = (n("94f8"), {
//     appCode: "T98HPCGN5ZVVQBS8LZQNOAEXVI9GYHKQ",
//     version: "1.0.0",
//     appSecret: "NMVFVILMKT13GEMD3BKPKCTBOQBPZR2P",
//     publicKey: "BEKaw3Qtc31LG/hTPHFPlriKuAn/nzTWl8LiRxLw4iQiSUIyuglptFxNkdCiNXcXvkqTH79Rh/A2sEFU6hjeK3k=",
//     privateKey: "AJxKNdmspMaPGj+onJNoQ0cgWk2E3CYFWKBJhpcJrAtC",
//     publicKeyType: "base64",
//     privateKeyType: "base64"
// })
t={}
t.data = {
    "data": {
        "addr": "",
        "areaCode": "110000",
        "optinsName": "",
        "pageNo": 2,
        "pageSize": 10
    },
    "appCode": "T98HPCGN5ZVVQBS8LZQNOAEXVI9GYHKQ",
    "version": "1.0.0",
    "encType": "SM4",
    "signType": "SM2",
    "timestamp": 1675237544
}

function m(e) {
    var t = {}
      , n = ["signData", "encData", "extra"];
    for (var i in e)
        e.hasOwnProperty(i) && !n.includes(i) && null != e[i] && (t[i] = e[i]);
    return t
}
console.log(m(t.data))

function p(e) {
    var t = new Array
      , n = 0;
    for (var i in e)
        t[n] = i,
        n++;
    var r = [].concat(t).sort()
      , o = {};
    for (var a in r)
        o[r[a]] = e[r[a]];
    return o
}
console.log(p(m(t.data)));

var u = "NMVFVILMKT13GEMD3BKPKCTBOQBPZR2P" // 代码中写死的，赋给u
function v(e) {
    var t = [];
    for (var n in e)
        if (e.hasOwnProperty(n) && (e[n] || "".concat(e[n])))
            if ("data" === n) {
                var i = Object.assign({}, e[n]);
                for (var r in i) {
                    if ("number" != typeof i[r] && "boolean" != typeof i[r] || (i[r] = "" + i[r]),
                    Array.isArray(i[r]) && !i[r].length && delete i[r],
                    Array.isArray(i[r]) && i[r].length > 0)
                        for (var o = 0; o < i[r].length; o++)
                            i[r][o] = p(i[r][o]);
                    null != i[r] && i[r] || delete i[r]
                }
                var a = p(i);
                t.push("".concat(n, "=").concat(JSON.stringify(a)))
            } else
                t.push("".concat(n, "=").concat(e[n]));
    return t.push("key=".concat(u)),
    t.join("&")
}

i = p(m(t.data));
i.data = p(i.data)
console.log(v(i));

r = v(i);

function A(e) {
    var t, n, i = new Array;
    t = e.length;
    for (var r = 0; r < t; r++)
        (n = e.charCodeAt(r)) >= 65536 && n <= 1114111 ? (i.push(n >> 18 & 7 | 240),
        i.push(n >> 12 & 63 | 128),
        i.push(n >> 6 & 63 | 128),
        i.push(63 & n | 128)) : n >= 2048 && n <= 65535 ? (i.push(n >> 12 & 15 | 224),
        i.push(n >> 6 & 63 | 128),
        i.push(63 & n | 128)) : n >= 128 && n <= 2047 ? (i.push(n >> 6 & 31 | 192),
        i.push(63 & n | 128)) : i.push(255 & n);
    return i
}

console.log(A('{"addr":"","areaCode":"110000","optinsName":"","pageNo":1,"pageSize":10}'))
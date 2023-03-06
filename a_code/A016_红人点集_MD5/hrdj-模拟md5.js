/*
* 密码和签名都是标准 md5 加密，在python端使用算法包模拟；
* 这里 js 只获取 sig 签名文本的生成，得到文本后在python加密；
*
* */

e = {
    "phoneNum": "13875045745",
    "pwd": "ea8077345fc072003edbcf8bd4f39c4f",
    "t": 1677835120762,
    "tenant": 1
};

function S(n) {
    for (var e = Object.keys(n).sort(), t = {}, a = 0; a < e.length; a++)
        t[e[a]] = n[e[a]];
    return t
}

function P(n) {
    var e = []
      , t = "";
    for (var a in n)
        e.push(n[a]);
    for (var i = 0; i < e.length; i++)
        t += e[i] + "";
    return t += "JzyqgcoojMiQNuQoTlbR5EBT8TsqzJ",
t
}


// 入口
function get_sig_text(e){
    return P(S(e))
}

console.log(get_sig_text(e));
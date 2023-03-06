/*
js位置
var u = function(e) {
    var t = e.url.replace(e.baseURL, "")
      , n = o.default.stringify(e.params || {});
    n && (t += (-1 === t.indexOf("?") ? "?" : o.default.options.delimiter || "&") + n),
    t = t.toLowerCase();
    var i = (0,
    a.default)(t, e.data)
      , l = (0,
    r.default)(t, e.data, (0,
    s.default)());
    e.headers[i] = l
};
* */

// t = t.toLowerCase();
// var i = a.default(t, e.data),
//     l = r.default(t, e.data, s.default());

var CryptoJS = require('crypto-js');

// ===================== 分析 t ========================================
// api + 参数 拼接， 转小写而来
t = '/api/datalist/touzilist?keyno=5dffb644394922f9073544a08f38be9f&pageindex=2';


// ================== 分析 i ============================================
// var i = a.default(t, e.data)

// r函数中 o.default 是写死的
r_o = {};  // 这里指代r函数中的o
r_o.default = {
    "n": 20,
    "codes": {
        "0": "W",
        "1": "l",
        "2": "k",
        "3": "B",
        "4": "Q",
        "5": "g",
        "6": "f",
        "7": "i",
        "8": "i",
        "9": "r",
        "10": "v",
        "11": "6",
        "12": "A",
        "13": "K",
        "14": "N",
        "15": "k",
        "16": "4",
        "17": "L",
        "18": "1",
        "19": "8"
    }
};

// s中: a.default(t)
var r = function() {
    for (var e = (arguments.length > 0 && void 0 !== arguments[0] ? arguments[0] : "/").toLowerCase(), t = e + e, n = "", i = 0; i < t.length; ++i) {
        var a = t[i].charCodeAt() % r_o.default.n;
        n += r_o.default.codes[a]
    }
    return n
};

function get_i(t) {
    // i = a.default(t, e.data) // e.data为 undefined
    var s = function() {
        var e = arguments.length > 1 && void 0 !== arguments[1] ? arguments[1] : {}
          , t = (arguments.length > 0 && void 0 !== arguments[0] ? arguments[0] : "/").toLowerCase()
          , n = JSON.stringify(e).toLowerCase();
        // return o.default(t + n, a.default(t)).toLowerCase().substr(8, 20)
        // o.default， 是一个标准 HmacSHA512 加密,可用算法包模拟
        return CryptoJS.HmacSHA512(t + n, r(t)).toString().toLowerCase().substr(8, 20)
    };

    // headers的key
    i = s(t, undefined);
    return i;
}

console.log('i:', get_i(t));


// ======================= 分析 l =============================
// l = r.default(t, e.data, s.default());

// s.default(), 就是window.tid， 是一个定值；
// var _default = function _default() {
//     var list = ["w", "i", "n", "d", "o", "w", ".", "t", "i", "d"];
//     return eval(list.join(""))
// };

function get_l(t){
    // s.default()
    tid = 'd8e943c06de83114b7927251b675b4a1';

    // r.default
    var s2 = function() {
        var e = arguments.length > 1 && void 0 !== arguments[1] ? arguments[1] : {}
          , t = arguments.length > 2 && void 0 !== arguments[2] ? arguments[2] : ""
          , n = (arguments.length > 0 && void 0 !== arguments[0] ? arguments[0] : "/").toLowerCase()
          , i = JSON.stringify(e).toLowerCase();
        // return o.default(n + "pathString" + i + t, a.default(n))
        return CryptoJS.HmacSHA512(n + "pathString" + i + t, r(n)).toString()
    };

    l = s2(t, undefined, tid);
    return l;
}

console.log('l:', get_l(t));


// 封装入口
function get_k_v(t) {
    key = get_i(t);
    value = get_l(t);
    return [key, value]
}

// console.log(get_k_v(t));
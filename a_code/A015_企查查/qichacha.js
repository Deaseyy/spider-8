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


// api + 参数 拼接而来
t = '/api/datalist/touzilist?keyno=5dffb644394922f9073544a08f38be9f&pageindex=2';


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


// i = a.default(t, e.data) // e.data为 undefined
var s = function() {
    var e = arguments.length > 1 && void 0 !== arguments[1] ? arguments[1] : {}
      , t = (arguments.length > 0 && void 0 !== arguments[0] ? arguments[0] : "/").toLowerCase()
      , n = JSON.stringify(e).toLowerCase();
    // return o.default(t + n, a.default(t)).toLowerCase().substr(8, 20)
    // o.default， 是一个标准 HmacSHA512 加密,可用算法包模拟
    return CryptoJS.HmacSHA512(t + n, r(t)).toString().toLowerCase().substr(8, 20)
};

i = s(t, undefined);
console.log('i:', i);
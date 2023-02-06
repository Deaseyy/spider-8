var CryptoJS = require('crypto-js');


function Q() {
    // console.log(arguments[0]);
    var e = arguments.length > 0 && void 0 !== arguments[0] ? arguments[0] : "";
    return e.replace(/\s+/g, "")
}

function F(e) {
    var n = arguments.length > 1 && void 0 !== arguments[1] ? arguments[1] : {};
    if (e && "string" === typeof e) {
        var t = n.text || "0"
          , a = n.length || 24;
        if (e.length < a)
            for (var r = e.length; r < a; r++)
                e += t;
        else
            e = e.substring(0, a);
        return e
    }
}

//function T(e) {  // e: pwd
function T(e, userName) {
    console.log(arguments[0]) // pwd
    console.log(arguments[1])  // userName

    arguments[1] = F(Q(userName))
    console.log(arguments[1])

    //
    var n = arguments.length > 1 && void 0 !== arguments[1] ? arguments[1] : ""
      , t = arguments.length > 2 && void 0 !== arguments[2] ? arguments[2] : {}
      , a = t.enc
      , r = void 0 === a ? "Utf8" : a
      , c = t.mode
      , i = void 0 === c ? "ECB" : c
      , o = t.padding
      , u = void 0 === o ? "Pkcs7" : o
      , d = CryptoJS.enc[r].parse(n)
      , l = {
        mode: CryptoJS.mode[i],
        padding: CryptoJS.pad[u]
    }
      , s = CryptoJS.TripleDES.encrypt(e, d, l);
    return s.toString()
}

userName = '123456789@163.com';  // '1234444444@163.com';
pwd = '123456789';  // '12344444'
// console.log(T(pwd, F(Q(userName))));
console.log(T(pwd, userName));


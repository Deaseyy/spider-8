/*
e = (0,
i[jt])((0,
i[qt])(a, d))
即需要破解：e = i[jt](i[qt](a, d))
* */


// ======================= 开始分析 ================================
// 以下变量测试多次，为定值
var H = 0;
var s = 55812;
var d = 'xyz517cda96abcd';
var k2 = '861831832863830866861836861862839831831839862863839830865834861863837837830830837839836861835833';


// cv
function yds_v(t) {
    t = encodeURIComponent(t)["replace"](/%([0-9A-F]{2})/g, function(n, t) {
        return o("0x" + t)
    });
    try {
        return btoa(t)
    } catch (n) {
        return Buffer['from'](t)['toString']('base64') // 和btoa 一样效果
    }
}

function o(n) {
    t = '',
    // [f2, s2, d2, m2, l2, v2, p2, s2, l2, d2, h2, y2][M](function(n) {
    ['66', '72', '6f', '6d', '43', '68', '61', '72', '43', '6f', '64', '65']['forEach'](function(n) {
        t += unescape("%u00" + n)
    });
    var t, e = t; // 拼了个 'fromCharCode'
    return String[e](n)
}

// oZ
function yds_h(n, t) {
    t = t || u();
    for (var e = (n = n['split'](''))['length'], r = t['length'], a = 'charCodeAt', i = H; i < e; i++)
        n[i] = o(n[i][a](H) ^ t[(i + 10) % r][a](H));
    return n['join']('')
}

function u() {
    return unescape(k2["replace"](/8/g, '%u00'))
}

// =========================================================================
// 测试入参：
var t = {
    'params': {brand: 'free', device: 'iphone', country: 'cn', genre: '36'},
    'url': '/rank/index',
    'baseURL': 'https://api.qimai.cn'
};
var i = {
    'cv': yds_v,
    'oZ': yds_h
};

// 入口函数
function getAnalysis (t) {
    var n;
    false || null != s || (n = i['ej']("synct"),
    s = c['default']['prototype']['difftime'] = -(0,
    i['ej'])('syncd') || +new Date - a2 * n);
    var e, r = +new Date - (s || 0) - 1661224081041, a = [];
    return void 0 === t['params'] && (t['params'] = {}),
    Object['keys'](t['params'])['forEach'](function(n) {
        if (n == 'analysis')
            return !1;
        t['params']["hasOwnProperty"](n) && a["push"](t['params'][n])
    }),
    a = a['sort']()['join'](''),
    a = i['cv'](a),
    a = (a += '@#' + t['url']['replace'](t['baseURL'], '')) + ('@#' + r) + ('@#' + 3),
    e = i['cv'](i['oZ'](a, d)),
    // -B == t[Jt][j](p) && (t[Jt] += (-B != t[Jt][j](Rn) ? Hn : Rn) + p + B1 + z[V1](e)),
    // t
    e
}

// test
analysis = getAnalysis(t);
console.log(analysis);
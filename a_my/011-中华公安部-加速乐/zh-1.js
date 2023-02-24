/*
* 不解混淆，直接盲扣js
*
* */

// 逆向代码
// res = _0x1d2cf1[_0x4bf4('0xc5', 'vUx@') + 'z'](_0x1d2cf1[_0x4bf4('0xb6', 'Pp)E') + 'L'](_0x1fde2d['tn'] + '=', _0x2e4692[0x0]) + _0x1d2cf1[_0x4bf4('0xa', 'znd@') + 'y'], _0x1fde2d['vt']) + (_0x4bf4('0xdb', 'sdNH') + _0x4bf4('0x100', 'Lz4$') + '\x20/');
// 其中的 _0x1fde2d['tn'] + '='  //  __jsl_clearance_s
// _0x2e4692[0x0] // 就是 value

var CryptoJS = require('crypto-js');

// 需要写活，在js中提取
_0x1fde2d = {
    "bts": [
        "1676556631.148|0|y16",
        "M1Qp2KLF%2FAr%2FR8KCf1XhTI%3D"
    ],
    "chars": "tLeYWRqxPqUJmdhRcQEgJQ",
    "ct": "c89061e34ef72b3f4f75d692506af2dcbe2e466d4795789abca51191c94437b9",
    "ha": "sha256",
    "tn": "__jsl_clearance_s",
    "vt": "3600",
    "wt": "1500"
};

// 经多次测试：返回的js中，hash算法(_0x1fde2d['ha']的值)，仅包括 md5，sha1，sha256，且均为标准算法；
hashs = {
'md5': function (v){return CryptoJS.MD5(v).toString()},
'sha1': function (v){return CryptoJS.SHA1(v).toString()},
'sha256': function (v){return CryptoJS.SHA256(v).toString()},
};
hash = hashs[_0x1fde2d['ha']]; // 使用标准算法包来模拟js中原本的 hash 函数


_0x29f2e3 = {};
_0x29f2e3['OqWtz'] = function (_0x595b92, _0x4c350c) {
        return _0x595b92 + _0x4c350c;
    };
_0x29f2e3['mdwbn'] = function (a, b) {
    return a - b;
};
var _0x1d2cf1 = _0x29f2e3;

var _0x3a0164 = new Date();
function _0xc54626(_0x2f0186, _0x3d4864) {
    var _0x2ab139 = _0x1fde2d['chars']['length'];
    for (var _0x2ecdfd = 0x0; _0x2ecdfd < _0x2ab139; _0x2ecdfd++) {
        for (var _0x35f007 = 0x0; _0x35f007 < _0x2ab139; _0x35f007++) {
            var _0x29d9f1 = _0x1d2cf1['OqWtz'](_0x3d4864[0x0] + _0x1fde2d['chars']['substr'](_0x2ecdfd, 0x1) + _0x1fde2d['chars']['substr'](_0x35f007, 0x1), _0x3d4864[0x1]);
            if (hash(_0x29d9f1) == _0x2f0186) {
                // return [_0x29d9f1, _0x1d2cf1['mdwbn'](new Date(), _0x3a0164)];
                return [_0x29d9f1, new Date() - _0x3a0164];
            }
        }
    }
};
var _0x2e4692 = _0xc54626(_0x1fde2d['ct'], _0x1fde2d['bts']);
res = _0x1fde2d['tn'] + '=' + _0x2e4692[0x0]
console.log(res);
/*
* 先使用 decodeObfuscator 工具解混淆，再扣js
*
* 逆向代码
* document["cookie"] = _0x1fde2d['tn'] + '=' + _0x2e4692[0] + ";Max-age=" + _0x1fde2d['vt'] + "; path = /";
* */

// 该对象写死在返回的js中，每次会变动，可用正则提取
// _0x1fde2d = {
//     "bts": [
//         "1676556631.148|0|y16",
//         "M1Qp2KLF%2FAr%2FR8KCf1XhTI%3D"
//     ],
//     "chars": "tLeYWRqxPqUJmdhRcQEgJQ",
//     "ct": "c89061e34ef72b3f4f75d692506af2dcbe2e466d4795789abca51191c94437b9",
//     "ha": "sha256",
//     "tn": "__jsl_clearance_s",
//     "vt": "3600",
//     "wt": "1500"
// };

// 每次请求返回的js中的这个hash函数，会根据 _0x1fde2d['ha'] 的值而改变，该文件的 ha='sha256'
// 所以不能直接使用，经测试该hash函数为标准算法，可使用标准算法包模拟
// function hash(_0xc9cc72) {
//   var _0x4a2874 = 8;
//
//   function _0x2a2c7e(_0x1e3c43, _0x387023) {
//     var _0x3aa411 = (_0x1e3c43 & 65535) + (_0x387023 & 65535);
//
//     var _0x849436 = (_0x1e3c43 >> 16) + (_0x387023 >> 16) + (_0x3aa411 >> 16);
//
//     return _0x849436 << 16 | _0x3aa411 & 65535;
//   }
//
//   function _0x42c86b(_0x43e512, _0xd11ec6) {
//     return _0x43e512 >>> _0xd11ec6 | _0x43e512 << 32 - _0xd11ec6;
//   }
//
//   function _0x336f4b(_0x4a0784, _0xce54d8) {
//     return _0x4a0784 >>> _0xce54d8;
//   }
//
//   function _0x2c7e05(_0x5c330c, _0x3fecb4, _0x18487d) {
//     return _0x5c330c & _0x3fecb4 ^ ~_0x5c330c & _0x18487d;
//   }
//
//   function _0x35905e(_0x3d21c2, _0x27a31c, _0x1ca39e) {
//     return _0x3d21c2 & _0x27a31c ^ _0x3d21c2 & _0x1ca39e ^ _0x27a31c & _0x1ca39e;
//   }
//
//   function _0x544a0d(_0x4f4bf6) {
//     return _0x42c86b(_0x4f4bf6, 2) ^ _0x42c86b(_0x4f4bf6, 13) ^ _0x42c86b(_0x4f4bf6, 22);
//   }
//
//   function _0xac426(_0x43cc52) {
//     return _0x42c86b(_0x43cc52, 6) ^ _0x42c86b(_0x43cc52, 11) ^ _0x42c86b(_0x43cc52, 25);
//   }
//
//   function _0x5b677d(_0x34353f) {
//     return _0x42c86b(_0x34353f, 7) ^ _0x42c86b(_0x34353f, 18) ^ _0x336f4b(_0x34353f, 3);
//   }
//
//   function _0x5f5418(_0x4f6f41) {
//     return _0x42c86b(_0x4f6f41, 17) ^ _0x42c86b(_0x4f6f41, 19) ^ _0x336f4b(_0x4f6f41, 10);
//   }
//
//   function _0x124623(_0x542058, _0x4461e7) {
//     var _0x697790 = new Array(1116352408, 1899447441, 3049323471, 3921009573, 961987163, 1508970993, 2453635748, 2870763221, 3624381080, 310598401, 607225278, 1426881987, 1925078388, 2162078206, 2614888103, 3248222580, 3835390401, 4022224774, 264347078, 604807628, 770255983, 1249150122, 1555081692, 1996064986, 2554220882, 2821834349, 2952996808, 3210313671, 3336571891, 3584528711, 113926993, 338241895, 666307205, 773529912, 1294757372, 1396182291, 1695183700, 1986661051, 2177026350, 2456956037, 2730485921, 2820302411, 3259730800, 3345764771, 3516065817, 3600352804, 4094571909, 275423344, 430227734, 506948616, 659060556, 883997877, 958139571, 1322822218, 1537002063, 1747873779, 1955562222, 2024104815, 2227730452, 2361852424, 2428436474, 2756734187, 3204031479, 3329325298);
//
//     var _0x550f05 = new Array(1779033703, 3144134277, 1013904242, 2773480762, 1359893119, 2600822924, 528734635, 1541459225);
//
//     var _0x35966f = new Array(64);
//
//     var _0x1622b8, _0x36019f, _0x546c44, _0x2cbb1e, _0xf83c09, _0x59a436, _0x36c27e, _0x5b265d, _0x5628e0, _0x1864da;
//
//     var _0x51f546, _0x27549e;
//
//     _0x542058[_0x4461e7 >> 5] |= 128 << 24 - _0x4461e7 % 32;
//     _0x542058[(_0x4461e7 + 64 >> 9 << 4) + 15] = _0x4461e7;
//
//     for (var _0x5628e0 = 0; _0x5628e0 < _0x542058["length"]; _0x5628e0 += 16) {
//       _0x1622b8 = _0x550f05[0];
//       _0x36019f = _0x550f05[1];
//       _0x546c44 = _0x550f05[2];
//       _0x2cbb1e = _0x550f05[3];
//       _0xf83c09 = _0x550f05[4];
//       _0x59a436 = _0x550f05[5];
//       _0x36c27e = _0x550f05[6];
//       _0x5b265d = _0x550f05[7];
//
//       for (var _0x1864da = 0; _0x1864da < 64; _0x1864da++) {
//         if (_0x1864da < 16) {
//           _0x35966f[_0x1864da] = _0x542058[_0x1864da + _0x5628e0];
//         } else {
//           _0x35966f[_0x1864da] = _0x2a2c7e(_0x2a2c7e(_0x2a2c7e(_0x5f5418(_0x35966f[_0x1864da - 2]), _0x35966f[_0x1864da - 7]), _0x5b677d(_0x35966f[_0x1864da - 15])), _0x35966f[_0x1864da - 16]);
//         }
//
//         _0x51f546 = _0x2a2c7e(_0x2a2c7e(_0x2a2c7e(_0x2a2c7e(_0x5b265d, _0xac426(_0xf83c09)), _0x2c7e05(_0xf83c09, _0x59a436, _0x36c27e)), _0x697790[_0x1864da]), _0x35966f[_0x1864da]);
//         _0x27549e = _0x2a2c7e(_0x544a0d(_0x1622b8), _0x35905e(_0x1622b8, _0x36019f, _0x546c44));
//         _0x5b265d = _0x36c27e;
//         _0x36c27e = _0x59a436;
//         _0x59a436 = _0xf83c09;
//         _0xf83c09 = _0x2a2c7e(_0x2cbb1e, _0x51f546);
//         _0x2cbb1e = _0x546c44;
//         _0x546c44 = _0x36019f;
//         _0x36019f = _0x1622b8;
//         _0x1622b8 = _0x2a2c7e(_0x51f546, _0x27549e);
//       }
//
//       _0x550f05[0] = _0x2a2c7e(_0x1622b8, _0x550f05[0]);
//       _0x550f05[1] = _0x2a2c7e(_0x36019f, _0x550f05[1]);
//       _0x550f05[2] = _0x2a2c7e(_0x546c44, _0x550f05[2]);
//       _0x550f05[3] = _0x2a2c7e(_0x2cbb1e, _0x550f05[3]);
//       _0x550f05[4] = _0x2a2c7e(_0xf83c09, _0x550f05[4]);
//       _0x550f05[5] = _0x2a2c7e(_0x59a436, _0x550f05[5]);
//       _0x550f05[6] = _0x2a2c7e(_0x36c27e, _0x550f05[6]);
//       _0x550f05[7] = _0x2a2c7e(_0x5b265d, _0x550f05[7]);
//     }
//
//     return _0x550f05;
//   }
//
//   function _0x5a0ec4(_0x1a3da9) {
//     var _0x39cc02 = Array();
//
//     var _0x436bfa = 255;
//
//     for (var _0x26b314 = 0; _0x26b314 < _0x1a3da9["length"] * _0x4a2874; _0x26b314 += _0x4a2874) {
//       _0x39cc02[_0x26b314 >> 5] |= (_0x1a3da9["charCodeAt"](_0x26b314 / _0x4a2874) & _0x436bfa) << 24 - _0x26b314 % 32;
//     }
//
//     return _0x39cc02;
//   }
//
//   function _0x309c2b(_0x244a73) {
//     var _0x1d93ce = new RegExp("\n", 'g');
//
//     _0x244a73 = _0x244a73["replace"](_0x1d93ce, "\n");
//     var _0x275bd6 = '';
//
//     for (var _0x356119 = 0; _0x356119 < _0x244a73["length"]; _0x356119++) {
//       var _0x586bb7 = _0x244a73["charCodeAt"](_0x356119);
//
//       if (_0x586bb7 < 128) {
//         _0x275bd6 += String["fromCharCode"](_0x586bb7);
//       } else {
//         if (_0x586bb7 > 127 && _0x586bb7 < 2048) {
//           _0x275bd6 += String["fromCharCode"](_0x586bb7 >> 6 | 192);
//           _0x275bd6 += String["fromCharCode"](_0x586bb7 & 63 | 128);
//         } else {
//           _0x275bd6 += String["fromCharCode"](_0x586bb7 >> 12 | 224);
//           _0x275bd6 += String["fromCharCode"](_0x586bb7 >> 6 & 63 | 128);
//           _0x275bd6 += String["fromCharCode"](_0x586bb7 & 63 | 128);
//         }
//       }
//     }
//
//     return _0x275bd6;
//   }
//
//   function _0x2850a1(_0x7561a0) {
//     var _0x3abdec = "0123456789abcdef";
//     var _0x2e48e4 = '';
//
//     for (var _0x153a0f = 0; _0x153a0f < _0x7561a0["length"] * 4; _0x153a0f++) {
//       _0x2e48e4 += _0x3abdec["charAt"](_0x7561a0[_0x153a0f >> 2] >> (3 - _0x153a0f % 4) * 8 + 4 & 15) + _0x3abdec["charAt"](_0x7561a0[_0x153a0f >> 2] >> (3 - _0x153a0f % 4) * 8 & 15);
//     }
//
//     return _0x2e48e4;
//   }
//
//   _0xc9cc72 = _0x309c2b(_0xc9cc72);
//   return _0x2850a1(_0x124623(_0x5a0ec4(_0xc9cc72), _0xc9cc72["length"] * _0x4a2874));
// }


// 我们最终的结果
// var _0x2e4692 = _0xc54626(_0x1fde2d['ct'], _0x1fde2d["bts"]);
// console.log(_0x2e4692[0]);


var CryptoJS = require('crypto-js');

// 封装函数，获取 cookie
function get_cookie(_0x1fde2d){
  // 经多次测试：返回的js中，hash算法(_0x1fde2d['ha']的值)，仅包括 md5，sha1，sha256，且均为标准算法；
  hashs = {
    'md5': function (v){return CryptoJS.MD5(v).toString()},
    'sha1': function (v){return CryptoJS.SHA1(v).toString()},
    'sha256': function (v){return CryptoJS.SHA256(v).toString()},
  };
  hash = hashs[_0x1fde2d['ha']]; // 使用标准算法包来模拟js中原本的 hash 函数

  var _0x3a0164 = new Date();

  function _0xc54626(_0x2f0186, _0x3d4864) {
    var _0x2ab139 = _0x1fde2d["chars"]["length"];

    for (var _0x2ecdfd = 0; _0x2ecdfd < _0x2ab139; _0x2ecdfd++) {
      for (var _0x35f007 = 0; _0x35f007 < _0x2ab139; _0x35f007++) {
        var _0x29d9f1 = _0x3d4864[0] + _0x1fde2d["chars"]["substr"](_0x2ecdfd, 1) + _0x1fde2d["chars"]["substr"](_0x35f007, 1) + _0x3d4864[1];
        // _0x2f0186 为 _0x1fde2d['ct']的值，该js中为 sha256 加密的结果
        // 当 hash(_0x29d9f1) == _0x2f0186 才能返回结果。可知该hash函数肯定也是 sha256加密，可以使用算法包来模拟；
        if (hash(_0x29d9f1) == _0x2f0186) {
          return [_0x29d9f1, new Date() - _0x3a0164];
        }
      }
    }
  }

  var _0x2e4692 = _0xc54626(_0x1fde2d['ct'], _0x1fde2d["bts"]); // ['1676556631.148|0|y16RhM1Qp2KLF%2FAr%2FR8KCf1XhTI%3D', 21]
  // res = _0x1fde2d['tn'] + '=' + _0x2e4692[0]; // __jsl_clearance_s=value
  // console.log(_0x2e4692[0]);  // value
  return _0x2e4692[0]
}

// ================先写死调试，_0x1fde2d写活：需要从js文件中正则提取 =============================
// // sha256  当前文件js的hash函数 只支持sha256  （每次返回的js的hash函数使用的算法不一样）
// _0x1fde2d = {
//     "bts": [
//         "1676556631.148|0|y16",
//         "M1Qp2KLF%2FAr%2FR8KCf1XhTI%3D"
//     ],
//     "chars": "tLeYWRqxPqUJmdhRcQEgJQ",
//     "ct": "c89061e34ef72b3f4f75d692506af2dcbe2e466d4795789abca51191c94437b9",
//     "ha": "sha256",
//     "tn": "__jsl_clearance_s",
//     "vt": "3600",
//     "wt": "1500"
// };
//MD5
_0x1fde2d = {
    "bts": ["1676646032.282|0|sFT", "r6%2FLjP0ldIr3KVgK%2B%2B96%2Bk%3D"],
    "chars": "fiGMKM5vsYjPiUipGugxtP",
    "ct": "b4571041498fa655df6e276c052e0eaf",
    "ha": "md5",
    "tn": "__jsl_clearance_s",
    "vt": "3600",
    "wt": "1500"
};
//sha1
// _0x1fde2d = {'bts': ['1676627362.34|0|VMz6', 'EYm0qHWR1ohKDiZ2k6Wus%3D'], 'chars': 'matZhDUHuQMQAapDjsgoBd', 'ct': '2202c80eae1adf72faa68dd687c27c972d012fe0', 'ha': 'sha1', 'tn': '__jsl_clearance_s', 'vt': '3600', 'wt': '1500'}
console.log(get_cookie(_0x1fde2d));
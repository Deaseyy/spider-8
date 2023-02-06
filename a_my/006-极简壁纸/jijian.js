/*
1，逆向数据接口
    https://api.zzzmh.cn/bz/v3/getData
    逆向参数：响应参数 result
2，逆向下载图片接口
    https://cdn2.zzzmh.cn/wallpaper/origin/c89083824f074c0bad71a976de306a83.jpg/thumbs?auth_key=1678809600-dd5af35dea6482ec398b8d3ef3e1b19d-0-4ce27d8cd7cc0f4d95766b96d73130e3
    逆向参数：载荷参数 auth_key
*/

var CryptoJS = require('crypto-js');


result = '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'
// result = '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'
/* 逆向数据接口 */

function _0x43f8fa(_0x4f03f6) {
    // Buffer.from(res1, 'base64').toString('binary');  //atob  base64解码
    for (var _0xa1047e = Buffer.from(_0x4f03f6, 'base64').toString('binary'), _0x186e94 = new Int8Array(_0xa1047e['length']), _0x5806a5 = 0x0; _0x5806a5 < _0xa1047e['length']; _0x5806a5++)
        _0x186e94[_0x5806a5] = _0xa1047e['charCodeAt'](_0x5806a5);
    return _0x186e94;
}
// console.log(_0x43f8fa(res));

function _0x230351(_0x583989) {
    for (var _0x4d2087 = [-0x6f, 0x34, 0x5b, 0x41, -0x41, 0x74, 0x77, 0x6a, -0x79, -0x52, -0x5, 0x50, 0x33, 0x61, 0x44, -0x53, -0x70, -0x33, 0x17, -0x2e, -0x22, -0x72, -0x37, -0xb, -0x7f, 0x5a, 0x21, 0x16, -0x1f, 0x32, -0x11, 0x14, -0x2c, 0xf, -0x5e, -0x7b, 0x76, -0x17, -0x3d, 0x72, 0x47, -0x68, -0x7e, -0x75, -0x51, -0x36, -0x12, -0x6e, -0x4, -0x5f, -0x5b, 0x5e, -0x50, -0xe, 0x78, 0x69, 0x55, 0x68, -0x56, -0x6c, 0x43, 0x19, 0x65, 0x6c, 0x10, -0x69, 0x6f, -0xa, 0x75, -0x49, 0x4d, 0x59, -0x1d, -0x62, -0x44, 0x70, 0x6b, -0x1, 0x56, 0x79, 0x58, -0x65, -0x7c, 0x45, -0x1e, -0x8, -0x71, -0x4a, -0x76, 0x39, -0x19, 0xc, -0x73, -0x6a, 0x5f, 0x7f, 0x54, 0x7c, -0x66, -0x1c, 0x49, 0x2b, -0x3c, 0x1c, 0x2e, 0x73, 0x1e, 0x7a, -0x4b, 0x7d, -0x43, -0x4d, 0x3, -0x7, -0x35, -0xd, 0x35, 0x4e, -0x48, 0x1, 0xb, -0x47, -0x27, -0x4f, -0x3, 0x13, 0x29, 0x7e, -0x2b, -0x7d, -0x1b, 0x22, 0x3f, 0x8, 0x48, -0x23, -0x29, -0x3f, 0x3c, -0x18, 0x66, 0x2f, -0x77, -0x67, -0x16, 0x2d, 0x3b, 0x40, -0x60, 0x31, 0x53, -0x6b, -0x78, -0x39, -0x46, 0x0, -0x26, -0x54, -0x28, 0x18, 0xe, 0x30, 0x1d, 0x2c, -0x24, -0x2f, 0x38, -0x5c, 0x26, 0x25, 0x4, -0x32, 0x67, 0xa, -0x59, 0x37, 0x71, -0x1a, 0x6e, 0x36, 0x24, -0x14, -0x4e, -0xc, -0x74, 0x46, -0x25, 0x5, -0x3e, -0x4c, -0x30, -0x40, 0x4f, 0x64, 0x28, 0x6, -0x3a, -0x5a, -0x13, -0x9, 0x27, 0x5d, -0x63, 0x15, 0x7, 0x1a, -0x2, 0x1b, -0x2d, 0x51, 0x3a, -0x7a, 0x4c, -0x42, 0x2, 0x5c, -0x2a, 0x62, -0x10, 0x9, 0x3d, 0x3e, -0xf, 0x63, -0x15, 0x1f, -0x38, 0x57, 0x11, -0x34, -0x45, -0x21, -0x3b, -0x55, 0x42, 0x4a, 0x12, -0x5d, -0x80, -0x57, -0x20, 0x2a, 0x20, -0x58, 0x6d, 0x60, 0xd, -0x6, 0x4b, -0x64, -0x31, 0x23, -0x61, 0x52, -0x6d, 0x7b], _0x525612 = 0x0, _0xfdd5b7 = 0x0, _0x3f51a8 = 0x0, _0x41bbf1 = new Array(), _0x572991 = 0x0; _0x572991 < _0x583989['length']; _0x572991++) {
        _0x525612 = _0x525612 + 0x1 & 0xff,
        _0xfdd5b7 = (0xff & _0x4d2087[_0x525612]) + _0xfdd5b7 & 0xff;
        var _0xc16be2 = _0x4d2087[_0x525612];
        _0x4d2087[_0x525612] = _0x4d2087[_0xfdd5b7],
        _0x4d2087[_0xfdd5b7] = _0xc16be2,
        _0x3f51a8 = (0xff & _0x4d2087[_0x525612]) + (0xff & _0x4d2087[_0xfdd5b7]) & 0xff,
        _0x41bbf1['push'](_0x583989[_0x572991] ^ _0x4d2087[_0x3f51a8]);
    }
    return _0x41bbf1;
}

// console.log(_0x230351(_0x43f8fa(res)));

function _0x1372a9(_0x5c4f9d) {
    // var _0x5b118e = _0x5c81;  // 没必要kou，下面用来求方法字符串，直接还原
    for (var _0xf6e638, _0x2f95a8, _0x17f332 = '', _0x46372e = 0x0; _0x46372e < _0x5c4f9d['length']; )
        _0xf6e638 = _0x5c4f9d[_0x46372e],
        _0x2f95a8 = 0x0,
        _0xf6e638 >>> 0x7 === 0x0 ? (_0x17f332 += String['fromCharCode'](_0x5c4f9d[_0x46372e]),
        _0x46372e += 0x1) : 0xfc === (0xfc & _0xf6e638) ? (_0x2f95a8 = (0x3 & _0x5c4f9d[_0x46372e]) << 0x1e,
        _0x2f95a8 |= (0x3f & _0x5c4f9d[_0x46372e + 0x1]) << 0x18,
        _0x2f95a8 |= (0x3f & _0x5c4f9d[_0x46372e + 0x2]) << 0x12,
        _0x2f95a8 |= (0x3f & _0x5c4f9d[_0x46372e + 0x3]) << 0xc,
        _0x2f95a8 |= (0x3f & _0x5c4f9d[_0x46372e + 0x4]) << 0x6,
        _0x2f95a8 |= 0x3f & _0x5c4f9d[_0x46372e + 0x5],
        _0x17f332 += String['fromCharCode'](_0x2f95a8),
        _0x46372e += 0x6) : 0xf8 === (0xf8 & _0xf6e638) ? (_0x2f95a8 = (0x7 & _0x5c4f9d[_0x46372e]) << 0x18,
        _0x2f95a8 |= (0x3f & _0x5c4f9d[_0x46372e + 0x1]) << 0x12,
        _0x2f95a8 |= (0x3f & _0x5c4f9d[_0x46372e + 0x2]) << 0xc,
        _0x2f95a8 |= (0x3f & _0x5c4f9d[_0x46372e + 0x3]) << 0x6,
        _0x2f95a8 |= 0x3f & _0x5c4f9d[_0x46372e + 0x4],
        _0x17f332 += String['fromCharCode'](_0x2f95a8),
        _0x46372e += 0x5) : 0xf0 === (0xf0 & _0xf6e638) ? (_0x2f95a8 = (0xf & _0x5c4f9d[_0x46372e]) << 0x12,
        _0x2f95a8 |= (0x3f & _0x5c4f9d[_0x46372e + 0x1]) << 0xc,
        _0x2f95a8 |= (0x3f & _0x5c4f9d[_0x46372e + 0x2]) << 0x6,
        _0x2f95a8 |= 0x3f & _0x5c4f9d[_0x46372e + 0x3],
        _0x17f332 += String['fromCharCode'](_0x2f95a8),
        _0x46372e += 0x4) : 0xe0 === (0xe0 & _0xf6e638) ? (_0x2f95a8 = (0x1f & _0x5c4f9d[_0x46372e]) << 0xc,
        _0x2f95a8 |= (0x3f & _0x5c4f9d[_0x46372e + 0x1]) << 0x6,
        _0x2f95a8 |= 0x3f & _0x5c4f9d[_0x46372e + 0x2],
        _0x17f332 += String['fromCharCode'](_0x2f95a8),
        _0x46372e += 0x3) : 0xc0 === (0xc0 & _0xf6e638) ? (_0x2f95a8 = (0x3f & _0x5c4f9d[_0x46372e]) << 0x6,
        _0x2f95a8 |= 0x3f & _0x5c4f9d[_0x46372e + 0x1],
        _0x17f332 += String['fromCharCode'](_0x2f95a8),
        _0x46372e += 0x2) : (_0x17f332 += String['fromCharCode'](_0x5c4f9d[_0x46372e]),
        _0x46372e += 0x1);
    return _0x17f332;
}
// console.log(_0x1372a9(_0x230351(_0x43f8fa(result))));

function getData(result) {
    return JSON.parse(_0x1372a9(_0x230351(_0x43f8fa(result))))
}
console.log(getData(result));




/* ========== 逆向下载图片接口 ========== */
// image_id = 'bbc58c3d998d4f389fdae649334873f7';

// function _0x4c930e() {
//     var _0x2da29c = new Date();
//     _0x2da29c['setMonth'](_0x2da29c['getMonth']() + 0x1),
//     _0x2da29c['setDate'](0xf),
//     _0x2da29c['setHours'](0x0),
//     _0x2da29c['setMinutes'](0x0),
//     _0x2da29c['setSeconds'](0x0),
//     _0x2da29c['setMilliseconds'](0x0);
//     var _0x5b7cf6 = Math['ceil'](_0x2da29c['getTime']() / 0x3e8);
//     return _0x3d8cd4('number', _0x5b7cf6, _0x5b7cf6),
//     _0x5b7cf6;
// }

// function _0x5d4bf1(_0x391d4b) {
//     var _0x4039df = _0x391d4b + '='
//       , _0x3c7dab = document['cookie']['split'](';');  // cookie 不知道怎么获取？
//     for (var _0x219de3 in _0x3c7dab) {
//         if ('WliRg' === 'WliRg') {
//             var _0xa5796c = _0x3c7dab[_0x219de3]['trim']();
//             if (0x0 == _0xa5796c['indexOf'](_0x4039df))
//                 return _0xa5796c['substring'](_0x4039df['length'], _0xa5796c['length']);
//         } else {
//             var _0x116a62 = _0x5e3f7e('number') || _0x26ee88()
//               , _0x34802f = _0x177cda(_0x116a62)
//               , _0xc3228d = _0x98c771['substring'](0x15, -0x1 == _0x57d53e['lastIndexOf']('?') ? _0x129efd['length'] : _0x5f1a14['lastIndexOf']('?'))
//               , _0x2922ae = _0x116a62 + '-' + _0x34802f + '-0-' + _0x567756(_0xc3228d + '-' + _0x116a62 + '-' + _0x34802f + '-0-TPV4hi7wIeM7DPv35457O8poVyUJRX0o');
//             return _0x3e9c62 + (_0x74e669['indexOf']('?') < 0x0 ? '?' : '&') + 'auth_key=' + _0x2922ae;
//         }
//     }
//     return null;
// }

image_id = 'bbc58c3d998d4f389fdae649334873f7';
// function _0x49750c(_0x434c5e) { // _0x434c5e: https://cdn2.zzzmh.cn/wallpaper/origin/c071cdc46f0c4867a1d52d0cb51fc6d6.jpg/thumbs
function get_image_url(image_id) {
    // _0xb0716d = '/wallpaper/origin/c071cdc46f0c4867a1d52d0cb51fc6d6.jpg/thumbs'
    _0xb0716d = '/wallpaper/origin/' + image_id + '.jpg/thumbs'
    _0x434c5e = 'https://cdn2.zzzmh.cn' + _0xb0716d  // image url

    // var _0x258685 = _0x5d4bf1('number') || _0x4c930e()  // 需要从cookie获取，待破解，暂时写死
    var _0x258685 = '1678809600'  // 2023-03-15, 当前时间为 2023-02-04
      , _0x26a23c = CryptoJS.MD5(_0x258685) //.toString()
      , _0xb0716d = _0x434c5e['substring'](0x15, -0x1 == _0x434c5e['lastIndexOf']('?') ? _0x434c5e['length'] : _0x434c5e['lastIndexOf']('?'))
      , _0xfeeed2 = _0x258685 + '-' + _0x26a23c + '-0-' + CryptoJS.MD5(_0xb0716d + '-' + _0x258685 + '-' + _0x26a23c + '-0-TPV4hi7wIeM7DPv35457O8poVyUJRX0o');
    return _0x434c5e + (_0x434c5e['indexOf']('?') < 0x0 ? '?' : '&') + 'auth_key=' + _0xfeeed2;
}
console.log(get_image_url(image_id))

// 遗留问题：逆向获取图片接口时，时间戳需要从cookie中获取，暂时不会获取
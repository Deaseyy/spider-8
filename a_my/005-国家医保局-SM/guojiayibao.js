var CryptoJS = require('crypto-js');
var wpk = require('./wpk.js');

window = global;


// t.headers["x-tif-signature"] = r(f),
// t.headers["x-tif-timestamp"] = s,
// t.headers["x-tif-nonce"] = h,

/* x-tif-nonce：h=Object(i.a) */
function i() {
    // 直接可以用，无需扣
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

h = i();
// console.log(h)


/* x-tif-timestamp：s = Math.ceil((new Date).getTime() */
// s = Math.ceil((new Date).getTime());
function x_tif_timestamp(){
    return Math.ceil((new Date).getTime())
}
s = x_tif_timestamp();

/* x-tif-signature: r(f)*/
function x_tif_signature(){
    f = s + h + s;
    return CryptoJS.SHA256(f).toString();
}
sign = x_tif_signature();
console.log('x_tif_signature:', sign);


/* signData: signData*/
t = {};
t.data = {
    "data": {
        "addr": "",
        "areaCode": "110000",
        "optinsName": "",
        "pageNo": 2,  // 页码，可由调用端传入
        "pageSize": 10  // 每页数据，可由调用端传入
    },
    "appCode": "T98HPCGN5ZVVQBS8LZQNOAEXVI9GYHKQ",  // 代码中写死
    "version": "1.0.0", // 代码中写死
    "encType": "SM4",
    "signType": "SM2",
    "timestamp": s
};


function sign_data(t) {
    // 变量d：多次请求尝试，发现是一个常量
    var d = '009c4a35d9aca4c68f1a3fa89c93684347205a4d84dc260558a049869709ac0b42'
    var n = m(t.data)
      , i = p(n);
    i.data = p(i.data);
     // 加载扣出的模块
    var o = wpk._yds("4d09");
    var e = wpk._yds("b639").Buffer;
    var r = v(i)
      , a = o.doSignature(r, d, {
        hash: !0
    });
    return e.from(a, "hex").toString("base64")
}

function m(e) {
    var t = {}
      , n = ["signData", "encData", "extra"];
    for (var i in e)
        e.hasOwnProperty(i) && !n.includes(i) && null != e[i] && (t[i] = e[i]);
    return t
}
// console.log(m(t.data));

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
// console.log(p(m(t.data)));

var u = "NMVFVILMKT13GEMD3BKPKCTBOQBPZR2P" // 代码中写死的(可搜索查看)，赋给u
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

signData = sign_data(t);
console.log('signData:', signData);

/* encData: encData */
function enc_data(e) {
    // 常量，代码中写死的(可搜索查看)
    var c = '009c4a35d9aca4c68f1a3fa89c93684347205a4d84dc260558a049869709ac0b42';
    var u = "NMVFVILMKT13GEMD3BKPKCTBOQBPZR2P";

    var t = e.data.data && JSON.stringify(e.data.data)
      , n = A(t);
    e.data.appCode && e.data.appCode !== c && (c = e.data.appCode);
    var i = b(c, u)
      , r = y(i, n);
    return r.toUpperCase()
}

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
function b(e, t) {
    return A(y(A(e.substr(0, 16)), A(t)).toUpperCase().substr(0, 16))
}
function y(t, n) {
    var i = 16 - parseInt(n.length % 16);
    n = n.concat(new Array(i).fill(i));
    var r = wpk._yds('e04e').encrypt(n, t);
    return wpk._yds("b639").Buffer.from(r).toString("hex")
}

encData = enc_data(t);
console.log('encData:', encData);


/* ==== 响应数据 encData, 解密 ======*/

function dec_data(data){
    md_7d92 = wpk._yds('7d92');
    // console.log(md_7d92);  //{ a: [Getter], b: [Getter] }
    return md_7d92.b("SM4", data)
}

// enc_data = {
//     "code": 0,
//     "data": {
//         "signData": "z+482BZ2r6bLIIBYXd/hW5VzP/lqoxS8sQiqm3jWM03ALCZO8aSs0eFtT/c23v+HVuEMVD+36hNgAaLlDbKZkQ==",
//         "encType": "SM4",
//         "data": {
//             "encData": "1BA85A41FFE8BE3C096DBED625AF99E57FF0FAC4DF382887CE7C00745C55A0ED475C63D505FDC2A7CED0F40F817D1D9F5A938D59A04092CB26BE6AC085D08384FE01A8104FE24BD975B12A455FFD7B8CD58A8295975BDF71CCB831C778EB77D451B96B9964239BFCBB01569DB248010AF6D0F7B3DFD1D1C333AF18D2687407717134EDA6F753E7A14B2C2F9349C8FA74DB14F09288F9324DC3A5B3E8CFA50A953AEE061359A57B234A75585A3EC6DD0AD53CA2EA3D4206597A21AD8BA80BC19C941236D0581732F4F22683AB6ECD868BBF7A6C2974CC9C05DFB850C3DCAC3E7079DF6B1668525438AB2EB5977DDBAA6D4235C2280F06250DEC75399563006D2954281B6143929D930E5098B009089DC3CE1B386B0419AA6F5594AD063A74333C13FBB5A13576C33F21E01AF70E42B0BAC199EE7F6542A45216D49A480DC26A64D0137EB9EAC42DC5D50F580225F543F11F9AB604DEC4EDFBFFD80A5B0084BB9A67F9D5C99E6EDCB61C1F753BCD02D16DB702C13825D1F299CE623F61A38DBB1C1046E8DE84E59AD0F5B5FDB1489614EBC36B3FA41341B61ED737A8353AE98C06253575500FA01EC73D96686B9C1BDE577D9BAF56810237B5DAA6068A1CD471C370980CCC9E3CD2E7B02E47D6CD83C906D3C417FCC21A7265F8CD30FB3D59CB2B13FA5B756E92F52D7C412064433EE53DBF04D73C366C2390B773D3380F46C9A47A47B2F469F22E5E678383B2582C62C67FF8ED52340076C40B44A4285AE5552CB9F6590C894ADC5D55342BB6A474DA7B8789F95F0A3C0902049E4BFEFD35FFE607EC808D97A13A7B81FD9A38EE30D66A13FBB5A13576C33F21E01AF70E42B0BAC199EE7F6542A45216D49A480DC26A64D0137EB9EAC42DC5D50F580225F543F11F9AB604DEC4EDFBFFD80A5B0084BB9A28D293A9C4D7F3742DED1767469D3B7FB702C13825D1F299CE623F61A38DBB1C59A7BA477C5D5DF530413195465EAC26332F22654ACA8CB201582404250A67EEDAC3F1C98EA031D1CC39FC8E01757D9EC95A49E20FED01AC504A62B5AAA040487B5904687A1D88266A114BDB678DBDDC85F2FA0F2B77385FFA1F5867F9D8FEFC04F7457B5E65C4858FA70C52557624A46C98BDF65505B25E4D0D4A7A265C807A1120C48C67D0343A2441DAFF044FD1886345AF0E1723312AE1793A7A5B1DE19FBAF9E45B1B59674DF2B465A57DE16DCC5D6DCF41BB60E166684DF9529909A737B7416C9272FC4C52D27909CEE4E5FF966A3AF95B3BD1A4E3DC8D508262B5E7ED8DEA1682BE275C30C9E6844FF7B07646A17B5C885F6CB057910EC81548F47AB555C63BEF9683712BB8950DB2931A3FC3DE375D6CBD01ADC3CC402507AC226B2C212BFF39A31D407E2F8E1352D46D51C15264E7B5B70D4EFB60BDB1D7946FE69F4D69F2FAC2E8E4C7A08342A1309BAF268B5376131FD859F8203EAC3D763E3D1860B87EA50A8D7F0DF985E7049A4B1E48195EA8A05996FBC5373297ED0CAA4B1065C7AF8A2380A07000C756EDC8B15CDD04E533EE74A6543E68650E8B90478D8613FA5B756E92F52D7C412064433EE53D0E989C36F76043C68D66C040AD32EAD37A47B2F469F22E5E678383B2582C62C660045E6BFEA769E942C11D443542AC9750DAB1FA6CFEB2CB09BAAB86490B7F2DE43610EEA28F2B640AF2BC50B5329E4C463C6584F787B0515A053A9A1B2FA49782DD5B8F14CFDC3D88032903A3E5991ED3DC524557A8E97DD960D7B47F3A27122E8D035E9D21C3FA65C274B0C7F0CF23B9CDA8CCAE8E3F9D385DB76C24B6EB2566CB6819C911EE99B713077A9913B3E0E42094628B15F5709FCE26C6BC15FCBB7237D97193F6DD116D3CFF23F81AE401B4354E2377B37FE7B54896C218674A469FD2753347F853725E26A1015688F7056F1B3E8D6417D25CCD0BFDFD613FA069CB39B7FE6061AC85A3F3B904CD08ADD9437550498F01FE16907D580E250958E70040E3B653EF0C3761BBA4DC07F0681F320BADDCFB4802A59601BD28793BC3DCE82BB7E1E13A0D7D84BD9E360DEDFF648B4B2436262F4A8E5F512795C41380922265964A5195152C239DEA3FF41D5587598A3B348AE01F2094E9D71ACD91BCECC57E978D7F9752A409DC4E4B8305DD6BAAE4FAD058D8974087745CAFB44865C42AE59783DE38BE25856E2DFC1811626943087CB06F111F4A3926701C4718D577F764ECB41A3D56EB9271C79E3999C2D7E71368CEF75A6586390690352771D7C766DEDEFA3D3A722A8828C63B2AAF30D2B749A66336D2797DB02876DD7BF92D79FC37820B5A36E19AB1394B13F79CDA8C1A0A95016A24E5253380F4431E9259F2E0DDB5F7FFBEA52CC370FB18E34422EB580D713551D96A87D517CCE92E4232E63D7A8AFD346D0AFBE5BF330E58D86E3140819280F2D27F95314901A4D9022E626B81E41F05D5E0177492902188B59757BB16B254A64510E8B5AC43DA24EE450E1170D7D7AC5098BAB8A063AF1D7CE6D6B42F7F5FE538EB5A5BACF994048F2C999C1ABFA8DBBA216B4A74C2E9DED06CD4825E9F21E2FD816481527F08698204F6EDC1904B0B891608911DC9FA396E00FA41EF6F6AF18E35211DC8B51D2EB46EBFD7E571CFE97F232CF816A37F7E1DEB89"
//         },
//         "signType": "SM2",
//         "appCode": "T98HPCGN5ZVVQBS8LZQNOAEXVI9GYHKQ",
//         "version": "1.0.0",
//         "timestamp": "1675310001782"
//     },
//     "message": "成功",
//     "timestamp": "1675310001",
//     "type": "success"
// };
// console.log(dec_data(enc_data));


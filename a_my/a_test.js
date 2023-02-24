var CryptoJS = require('crypto-js');

// document = {}
// // console.log(ps());
// console.log(document.toString());
// console.log(document.toString());
//
// // ‌‌console.log(document.toString());
// // console.log(document.toString());
// console.log('console.log(document.toString());' === '‌‌console.log(document.toString());')

// // =========================
// const {JSDOM} =require("jsdom");
// const dom=new JSDOM("<!DOCTYPE html><p>Hello world</p>");
// // 补环境
// window=dom.window;
// document=window.document;  //document对象:代表给定浏览器窗口中的HTML文档,
// navigator=window.navigator; // 关于运行当前脚本的应用程序的相关信息
// location=window.location; //对象包含当前页面的URL信息
// history=window.history; // 历史会话
// screen=window.screen; // 浏览器屏幕
//
// var object_toString = Object.prototype.toString
// Object.prototype.toString = function (){
//     // [object HTMLDocument]
//     if (this.constructor.name == 'Document') {
//         return '[object HTMLDocument]'
//     }
//     return object_toString.call(this, arguments);
// }
// // document = {}
// console.log(document.toString());
// // qq = ['123', '122']
// // console.log(qq.toString());
// ww = {'a':123, 'b':222}
// console.log(ww.toString());
// ee = null
// console.log(ee.toString());

// e_data = encodeURIComponent('www.sss+/s.com/a/b')
// console.log(e_data);
//
// d_data_1 = decodeURIComponent(e_data);
// d_data_2 = unescape(e_data);
// console.log(d_data_1);
// console.log(d_data_2);

// e_data = encodeURIComponent('1676722853381000');
// e_data = encodeURI('1676722853381000');
// console.log(e_data);

// d = {
//     a:1,
//     b:function () {
//         console.log(this);
//         return this.c
//     },
//     c:22
// }
// // console.log(d);
// console.log(d.b());

function o(n) {
    t = '',
    // [f2, s2, d2, m2, l2, v2, p2, s2, l2, d2, h2, y2][M](function(n) {
    ['66', '72', '6f', '6d', '43', '68', '61', '72', '43', '6f', '64', '65']['forEach'](function(n) {
        t += unescape("%u00" + n)
    });
    var t, e = t;
    return String[e](n)
}
o('0x36cnfreeiphone')
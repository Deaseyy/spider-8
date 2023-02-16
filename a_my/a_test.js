var CryptoJS = require('crypto-js');

// r = CryptoJS.MD5('1678809600').toString()
// console.log(r)
// var window = global;
// document = {}
// ‌‌console.log(document.toString());
// console.log(exports)
// console.log(typeof exports)
// console.log(typeof(typeof exports))


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



// location = {}
// console.log(location.toString());

// a = {'q':111}
// // a.b = undefined
// console.log(a)
// console.log(a.b)
// console.log(a.c)
// console.log(a.constructor)

// console.log('\x70\x72\x6f\x74\x6f\x74\x79\x70\x65');
console.log('\x70');
console.log(0x70);
console.log(0xf);
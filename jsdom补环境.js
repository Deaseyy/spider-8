// jsdom 模拟浏览器环境
const {JSDOM} =require("jsdom");
const dom=new JSDOM("<!DOCTYPE html><p>Hello world</p>");
ppp = dom.window.document.querySelector('p').textContent
console.log(ppp);
window=dom.window;
document=window.document;  //document对象:代表给定浏览器窗口中的HTML文档,
navigator=window.navigator; // 关于运行当前脚本的应用程序的相关信息
location=window.location; //对象包含当前页面的URL信息
history=window.history; // 历史会话
screen=window.screen; // 浏览器屏幕

console.log(navigator);
console.log(location);


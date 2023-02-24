/** 实现 window.btoa  window.atob
btoa: binary to ASCII, base64编码过程;
atob: ASCII to binary, base64解码过程;
* */
// btoa  base64编码
res1 = Buffer.from('hello', 'binary').toString('base64');
// atob  base64解码
res2 = Buffer.from(res1, 'base64').toString('binary');
console.log(res1, res2);


/*
* js 字符串和16进制的互相转换
*
* */
// hex编码：字符串转16进制
function strToHexCharCode(s) {
　　if(s === "")
　　　　return "";
　　var hexCharCode = [];
// 　　hexCharCode.push("0x");  // 加上0x前缀分隔
　　for(var i = 0; i < s.length; i++) {
　　　　hexCharCode.push((s.charCodeAt(i)).toString(16));
　　}
　　return hexCharCode.join("");
}

// 16进制转字符串
function hexCharCodeToStr(hexCharCodeStr) {
　　var trimedStr = hexCharCodeStr.trim();
　　var rawStr =
　　trimedStr.substr(0,2).toLowerCase() === "0x"
　　?
　　trimedStr.substr(2)
　　:
　　trimedStr;
　　var len = rawStr.length;
　　if(len % 2 !== 0) {
　　　　alert("Illegal Format ASCII Code!");
　　　　return "";
　　}
　　var curCharCode;
　　var resultStr = [];
　　for(var i = 0; i < len;i = i + 2) {
　　　　curCharCode = parseInt(rawStr.substr(i, 2), 16); // ASCII Code Value
　　　　resultStr.push(String.fromCharCode(curCharCode));
　　}
　　return resultStr.join("");
}
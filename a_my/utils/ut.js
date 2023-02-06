/** 实现 window.btoa  window.atob
btoa: binary to ASCII, base64编码过程;
atob: ASCII to binary, base64解码过程;
 */
// btoa  base64编码
res1 = Buffer.from('hello', 'binary').toString('base64');
// atob  base64解码
res2 = Buffer.from(res1, 'base64').toString('binary');
console.log(res1, res2);
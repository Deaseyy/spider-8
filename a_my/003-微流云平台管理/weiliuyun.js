// https://wei-liu.com/user/login.html 微流云平台管理系统 登录界面

var JSEncrypt = require('jsencrypt')
var CryptoJS = require('crypto-js')


// 通过 https://api.wei-liu.com/api/v1/Token/code 接口获取 pubkey 和 pubcode

// pubkey = "-----BEGIN PUBLIC KEY-----\\r\\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAo0nnZ/9wVN7HV/VeepE3\\r\\nIVAlAT6n1fmkXrHxbA08Olv+nYp7QlTW3heOEsOWTEMKRcYU1xAIMwt7pZ+qbyFD\\r\\nitnHkQUqneYs6PKeK2nDxGXR4MIRUz/MFJ4I3QRzmmklFPkJpfxnL0HnwNHw0fm4\\r\\nuX3GD9qxEcVsqSdhQMvgrW7gFQMD9tSiaXflgyQv1CZjCPNW2xSpWVoFl0+ODpFT\\r\\nsEmEt+uRiBD1ZVJnTVTCI0txqFLzFw/JwhUcUgflFRovtkcXTU+8aUCtnAAW019U\\r\\n5Anw6S4S6Ct2PTO0ZFwRNgjboRmT/0x/zdUfn/h6otQSllRfdqF1RVG4HoDf1U0s\\r\\neQIDAQAB\\r\\n-----END PUBLIC KEY-----"
// 注意：复制粘贴的时候格式可能有问题，比如变成上面那行
pubkey = "-----BEGIN PUBLIC KEY-----\r\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAo0nnZ/9wVN7HV/VeepE3\r\nIVAlAT6n1fmkXrHxbA08Olv+nYp7QlTW3heOEsOWTEMKRcYU1xAIMwt7pZ+qbyFD\r\nitnHkQUqneYs6PKeK2nDxGXR4MIRUz/MFJ4I3QRzmmklFPkJpfxnL0HnwNHw0fm4\r\nuX3GD9qxEcVsqSdhQMvgrW7gFQMD9tSiaXflgyQv1CZjCPNW2xSpWVoFl0+ODpFT\r\nsEmEt+uRiBD1ZVJnTVTCI0txqFLzFw/JwhUcUgflFRovtkcXTU+8aUCtnAAW019U\r\n5Anw6S4S6Ct2PTO0ZFwRNgjboRmT/0x/zdUfn/h6otQSllRfdqF1RVG4HoDf1U0s\r\neQIDAQAB\r\n-----END PUBLIC KEY-----"
pubcode = "bda1f945da644082a7e70aa0f9beb3fc"

password = '123456'

var encrypt = new JSEncrypt();
encrypt.setPublicKey(pubkey)
encrypted = encrypt.encrypt(pubcode + CryptoJS.SHA512(password).toString())

console.log(encrypted)  // 每次加密结果不一样



/* 问题：
jsencrypt 导包 会报错： ReferenceError: window is not defined
解决：在 jsencrypt\bin\jsencrypt.js 文件上方加入 `window = global;`

 */
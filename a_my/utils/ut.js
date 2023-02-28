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
* ========= js 字符串和16进制的互相转换 ==============================
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

/*
* ====================  unicode 还原字符串 ============================
* */
function reconvert(str){
    str = str.replace(/(\\u)(\w{1,4})/gi,function($0){
        return (String.fromCharCode(parseInt((escape($0).replace(/(%5Cu)(\w{1,4})/g,"$2")),16)));
    });
    str = str.replace(/(&#x)(\w{1,4});/gi,function($0){
        return String.fromCharCode(parseInt(escape($0).replace(/(%26%23x)(\w{1,4})(%3B)/g,"$2"),16));
    });
    str = str.replace(/(&#)(\d{1,6});/gi,function($0){
        return String.fromCharCode(parseInt(escape($0).replace(/(%26%23)(\d{1,6})(%3B)/g,"$2")));
    });

    return str;
}
console.log(reconvert('{\n' +
    '            "\u002e\u0077\u0069\u0064\u0067\u0065\u0074": {\n' +
    '                "\u002e\u0077\u0069\u006e\u0064\u006f\u0077": {\n' +
    '                    "\u0061\u002e\u006c\u0069\u006e\u006b\u002e\u0061\u0062\u0073\u006f\u006c\u0075\u0074\u0065": Yt ? {\n' +
    '                        "\u002e\u0073\u006c\u0069\u0063\u0065\u0062\u0067\u002e\u0061\u0062\u0073\u006f\u006c\u0075\u0074\u0065": {\n' +
    '                            "\u0063\u0061\u006e\u0076\u0061\u0073\u002e\u0062\u0067\u002e\u0061\u0062\u0073\u006f\u006c\u0075\u0074\u0065": {},\n' +
    '                            "\u002e\u0073\u006c\u0069\u0063\u0065": {}\n' +
    '                        },\n' +
    '                        "\u0063\u0061\u006e\u0076\u0061\u0073\u002e\u0066\u0075\u006c\u006c\u0062\u0067\u002e\u0066\u0061\u0064\u0065\u002e\u0061\u0062\u0073\u006f\u006c\u0075\u0074\u0065": {}\n' +
    '                    } : {\n' +
    '                        "\u002e\u0073\u006c\u0069\u0063\u0065\u0062\u0067\u002e\u0061\u0062\u0073\u006f\u006c\u0075\u0074\u0065": {\n' +
    '                            "\u002e\u0062\u0067\u002e\u0061\u0062\u0073\u006f\u006c\u0075\u0074\u0065": {},\n' +
    '                            "\u002e\u0073\u006c\u0069\u0063\u0065": {}\n' +
    '                        },\n' +
    '                        "\u002e\u0066\u0075\u006c\u006c\u0062\u0067\u002e\u0066\u0061\u0064\u0065\u002e\u0061\u0062\u0073\u006f\u006c\u0075\u0074\u0065": {}\n' +
    '                    },\n' +
    '                    "\u002e\u0066\u006c\u0061\u0073\u0068\u006c\u0069\u0067\u0068\u0074\u002e\u0061\u0062\u0073\u006f\u006c\u0075\u0074\u0065": {},\n' +
    '                    "\u002e\u006c\u006f\u0061\u0064\u0069\u006e\u0067\u002e\u0061\u0062\u0073\u006f\u006c\u0075\u0074\u0065": {\n' +
    '                        "\u002e\u006c\u006f\u0061\u0064\u0069\u006e\u0067\u005f\u0069\u0063\u006f\u006e": {},\n' +
    '                        "\u002e\u006c\u006f\u0061\u0064\u0069\u006e\u0067\u005f\u0074\u0069\u0070": {}\n' +
    '                    },\n' +
    '                    "\u002e\u0072\u0065\u0073\u0075\u006c\u0074\u002e\u0065\u006e\u0074\u0065\u0072": {\n' +
    '                        "\u002e\u0072\u0065\u0073\u0075\u006c\u0074\u005f\u0069\u0063\u006f\u006e": {},\n' +
    '                        "\u002e\u0072\u0065\u0073\u0075\u006c\u0074\u005f\u0074\u0069\u0074\u006c\u0065": {},\n' +
    '                        "\u002e\u0072\u0065\u0073\u0075\u006c\u0074\u005f\u0063\u006f\u006e\u0074\u0065\u006e\u0074": {}\n' +
    '                    }\n' +
    '                },\n' +
    '                "\u002e\u0070\u0061\u006e\u0065\u006c": {\n' +
    '                    "\u0061\u002e\u0063\u006c\u006f\u0073\u0065": {\n' +
    '                        "\u002e\u0063\u006c\u006f\u0073\u0065\u005f\u0074\u0069\u0070": {}\n' +
    '                    },\n' +
    '                    "\u0061\u002e\u0072\u0065\u0066\u0072\u0065\u0073\u0068": {\n' +
    '                        "\u002e\u0072\u0065\u0066\u0072\u0065\u0073\u0068\u005f\u0074\u0069\u0070": {}\n' +
    '                    },\n' +
    '                    "\u0061\u002e\u0066\u0065\u0065\u0064\u0062\u0061\u0063\u006b": {\n' +
    '                        "\u002e\u0066\u0065\u0065\u0064\u0062\u0061\u0063\u006b\u005f\u0074\u0069\u0070": {}\n' +
    '                    },\n' +
    '                    "\u0061\u002e\u006c\u006f\u0067\u006f": {}\n' +
    '                }\n' +
    '            },\n' +
    '            "\u002e\u0073\u006c\u0069\u0064\u0065\u0072": {\n' +
    '                "\u002e\u0073\u006c\u0069\u0064\u0065\u0072\u005f\u0074\u0069\u0070": {},\n' +
    '                "\u002e\u0073\u006c\u0069\u0064\u0065\u0072\u005f\u0062\u0075\u0074\u0074\u006f\u006e": {},\n' +
    '                "\u002e\u0073\u006c\u0069\u0064\u0065\u0072\u005f\u0073\u0074\u0061\u0074\u0075\u0073": {}\n' +
    '            }\n' +
    '        },'))

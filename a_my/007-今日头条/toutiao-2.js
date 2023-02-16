/* 使用油猴脚本注入

*     前提：控制台已导出加密函数
*     1.将下面的脚本添加到油猴插件中，开启插件
*     2.打开对应网站激活脚本即可
*       有时需要多次刷新，或关掉重新进入网站
* */
// ===================== 脚本内容，从UserScript开始 =========================

// ==UserScript==
// @name         toutiao_signature
// @namespace    https://www.toutiao.com/
// @version      0.1
// @description  破解头条的signature参数
// @author       yds
// @match        https://www.toutiao.com/*
// @icon         https://www.google.com/s2/favicons?sz=64&domain=toutiao.com
// @grant        none
// @require      https://sekiro.virjar.com/sekiro-doc/assets/sekiro_web_client.js
// ==/UserScript==

(function() {
    'use strict';

    // Your code here...
    function guid() {
        function S4() {
            return (((1+Math.random())*0x10000)|0).toString(16).substring(1);
        }
        return (S4()+S4()+"-"+S4()+"-"+S4()+"-"+S4()+"-"+S4()+S4()+S4());
    }


    var client = new SekiroClient("ws://127.0.0.1:5620/business-demo/register?group=toutiao&clientId=" + guid());

    // 参数o 依赖python端传入，使用request接收，这里先写死
    var o = {
        url: "https://www.toutiao.com/api/pc/list/feed?channel_id=0&max_behot_time=1675742044&category=pc_profile_recommend&aid=24&app_name=toutiao_web"
    };
    client.registerAction("signature",function(request, resolve, reject ){
        resolve(window.byted_acrawler.sign(o));
    });
})();

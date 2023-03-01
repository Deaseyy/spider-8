/* 使用rpc 控制台注入

* 以下是注入控制台的 rpc 连接脚本（需要先注入 rpc 客户端js）
*     前提：控制台已导出加密函数
*     1.先注入rpc客户端到控制台
*     2.再将下面的脚本复制到控制台运行即可
* */

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
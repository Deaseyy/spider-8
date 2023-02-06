/* 可以对外提供接口，而不用暴露算法源代码 */

// 1.导入 express
const express = require('express');

// 2.创建 web 服务器
const app = express();
const port = 5001;

function jiemi(){
    return '解密结果'
}

function jiemi_params(p){
    return '参数：' + p
}

app.get('/', (req, res) => {
    let data = jiemi();
   res.send(data)
});

app.get('/params', (req, res) => {
    let data = jiemi_params(req.query.name);
   res.send(data)
});

// 3.启动 web 服务器
app.listen(port, () => {
    console.log('express server running at http://127.0.0.1:' + port);
});
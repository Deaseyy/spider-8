/*
* 说明：var在函数内部，用于定义局部变量
*
* */
// 参考：https://blog.csdn.net/L1194774003/article/details/104189068


// =================== 示例1：  x, f 不使用var定义 ===================
var x = 10000;
function f1() {
    // 前面不加 var，x和f2 都属于全局变量，外部可直接调用
    x = 10; // 不加var，x属于全局变量赋值，会覆盖外部x的值
    f11 = function () {
        return 222 + x
    };
    return f11();
}

console.log(f1());  // 232
console.log(f11());  // 232  //需先提前触发f1执行
// console.log(window.f11());  // 浏览器环境可调用
console.log(x);  // 10 覆盖全局变量x的值， //需先提前触发f1执行
// 总结：不使用var定义，在外部可直接调用内部函数或变量


console.log('--------------------------------------------------------------')
// =================== 示例2： x, f 使用var定义  ===================
// 说明：
var x = 10000;
function f2() {
    // 以下x, f2均属于局部变量，外部无法调用
    var x = 10;
    var f22 = function () {
        return 222 + x
    };
    return f22()
}

console.log(f2());  // 232
// console.log(f22());  // 无法调用
// console.log(window.f22());  // 无法调用
console.log(x);  // 10000  ，值为全局变量x
// 总结：var在函数内部，用于定义局部变量，在外部无法直接调用内部函数或变量


console.log('--------------------------------------------------------------')
// =================== 示例 3：  x, f 赋值给this引用 ===================
var x = 10000;
function f3() {
    // 这里的this 在浏览器环境就代表window对象
    this.x = 10;
    this.f33 = function () {
        console.log('this指向: ', this);
        return 222 + this.x
    };
    return this.f33()
    // return f2() // 也行
}


console.log(f3());  // 232
console.log(f33());  // 232, //需先提前触发f3执行
// console.log(window.f33());  // 浏览器环境可调用, 需先提前触发f3执行
console.log(x);  // 10000 this.x=10 修改的是它指代对象的x值，
// 总结： 这里之前 基本和示例1 结论一致；




// // ============== 以下为浏览器环境测试 =========================
// function f3() {
//     // 这里的this 在浏览器环境就代表window对象
//     this.x = 10;
//     this.f33 = function () {
//         return 222 + this.x
//     };
//     return this  // 返回值就是window对象
// }

function Person(name){
    this.name = name;
    this.info = function(){
        alert("这是一个：" + this.name);
    }
}
var p = new Person("实例变量");
p.info();
var name = "全局变量";
p.info.call(window); // window对象替代p对象来调用info方法

// 可以看到，两次调用info，但是却输出了不同的值。
// 第一次调用info，调用它的对象是p，所以此时info前的this指的还是Person类，它将输出p对象内的name变量，即“局部变量”，
// 第二次调用info，是通过call调用的，此时调用info的对象是window，程序在全局也定义了一个变量name，它的值是“全局变量”，所以第二次调用info，输出的就是“全局变量”。

// 总结：
// 当定义某个类的方法时，该类内的局部函数是独立存在的，他不会作为类或是实例的附庸存在，
// 这些内嵌函数可以被分离出来独立使用，这也包括让局部函数成为另一个对象的局部函数。

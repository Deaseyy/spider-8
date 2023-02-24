/*
* 浏览器控制台，直接输出 this， 它默认就是一个window对象；
*
* this 指向问题：谁来调用的就是谁
*
* */


function f(x) {
    // f(), this为 <ref *1> Object [global]....，浏览器环境为window对象
    // d.a(), this为对象d本身, 即：{ a: [Function: f] }
    // new f(), this 为类实例对象
    // new d.a(), this 为类实例对象
    console.log(this);
    console.log(this.age);  // 即使对象d的属性age有值，在new f()时，this.age 也是undefined，因为this指向不同对象；
    this.age = 2;
    return x
}
// f()

d = {}
d.a = f
// console.log(d.a(1));
// console.log(f(1));  // this为： <ref *1> Object [global]....，浏览器就是一个window对象
d.a();  // this指向d, 给d添加了age=2
console.log(d);
console.log('d的age值: ', d.age);
o1 = new f();
console.log('o1: ', o1.age);  // 对象  f {}
o2 = new d.a();
console.log('o2: ', o2.age);  // 对象  f {}

// ===== 总结：
// 1.直接 f() 调用时，this指向 window对象
// 2.通过 obj = new f() 调用时，this 指向类实例obj，添加给this的属性将作为实例属性；
// 3.通过 d.a() 调用f时，this 指向对象d本身, 添加给this的属性将作为d的属性；
// ===================================================================================================

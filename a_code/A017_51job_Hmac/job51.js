/*
* 目标代码：
* e.headers.sign = p.a.HmacSHA256(t, s["a"].state.commonStore.cupid_sign_key)
*
* */

// p.a.HmacSHA256(t, s["a"].state.commonStore.cupid_sign_key)

// t为 api + 参数拼接
t = '/open/noauth/search-pc?api_key=51job&timestamp=1677837598&keyword=python&searchtype=2&function=&industry=&jobarea=000000&jobarea2=&landmark=&metro=&salary=&workyear=&degree=&companytype=&companysize=&jobtype=&issuedate=&sorttype=0&pagenum=3&requestid=018cfc464c55fecf9f124c510ac56af5&pagesize=50&source=1&accountid=&pagecode=sou%7csou%7csoulb'

// key 是写死的， s["a"].state.commonStore.cupid_sign_key
cupid_sign_key = "abfc8f9dcf8c3f3d8aa294ac5f2cf2cc7767e5592590f39c3f503271dd68562b";

// p.a.HmacSHA256
// 可用标准算法包模拟

// 所以headers.sign 参数可以直接在python中模拟
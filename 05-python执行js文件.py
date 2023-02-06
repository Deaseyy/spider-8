import execjs

with open('05-test.js', encoding='utf-8') as f:
    js_code = f.read()

# 编译js 文件
ctll = execjs.compile(js_code)

# 执行 js
res = ctll.call('f1')
print(res)

res2 = ctll.call('f2', 'QW', 'ER')
print(res2)

# 直接执行js代码
print(execjs.eval('Date.now()'))
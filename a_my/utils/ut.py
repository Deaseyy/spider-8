
"""修改编码方式，windows 默认编码是gbk，Mac 和 Linux 默认是utf-8
import subprocess
from functools import partial
# 修改编码方式，windows 默认编码是gbk，Mac 和 Linux 默认是utf-8
subprocess.Popen = partial(subprocess.Popen, encoding='utf-8')
"""
import execjs


def compile_js(path):
    """编译js文件"""
    with open(path, encoding='utf-8') as f:
        js_code = f.read()

    exe = execjs.compile(js_code)
    return exe

# res = exe.call('f', 'params')





"""
windows 默认编码是gbk，Mac 和 Linux 默认是utf-8
1.编码问题一：解码错误
    - UnicodeDecodeError: 'gbk' codec can't decode byte 0xa6 in position 190: illegal multibyte sequence
解决：
    - 修改编码方式，添加以下代码：
        import subprocess
        from functools import partial
        # 修改编码方式，windows 默认编码是gbk，Mac 和 Linux 默认是utf-8
        subprocess.Popen = partial(subprocess.Popen, encoding='utf-8')

2.编码问题二：编码错误
    - UnicodeEncodeError: 'gbk' codec can't encode character '\u200c' in position 1228: illegal multibyte sequence
解决：
    - 修改 c:\python38\lib\subprocess.py 文件，找到一个包含形参`encoding=None`的__init__方法， 改为 'utf-8' .
"""

import execjs


def compile_js(path):
    """编译js文件"""
    with open(path, encoding='utf-8') as f:
        js_code = f.read()

    exe = execjs.compile(js_code)
    return exe

# res = exe.call('f', 'params')




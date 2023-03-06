
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
import time
from urllib.parse import quote

import execjs


def compile_js(path):
    """编译js文件"""
    with open(path, encoding='utf-8') as f:
        js_code = f.read()

    exe = execjs.compile(js_code)
    return exe

# res = exe.call('f', 'params')


def format_query_params(params, sort=True, blank=True, urlencode=False):
    """字典参数格式化
    - sort: True-字典排序
    - blank: True-保留值为空串的键值对
    - urlencode: True-进行url编码，安全字符 '/,&,='
    """
    keys = list(params)
    if sort:
        keys.sort()

    if blank:
        buff = [f'{k}={params[k]}' for k in keys]
    else:
        buff = [f'{k}={params[k]}' for k in keys if params[k]]

    res = "&".join(buff)
    if urlencode:
        res = quote(res, safe='/,&,=')

    return res


def ctime(ms=True):
    """当前时间戳"""
    t = time.time()
    if ms:
        return int(t * 1000)
    return int(t)


if __name__ == '__main__':
    print(ctime())
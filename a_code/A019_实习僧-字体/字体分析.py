from fontTools.ttLib import TTFont

"""
实习僧字体文件分析
html源码中找到字体引用位置：
- @font-face {    font-family: myFont;    src: url(/interns/iconfonts/file?rand=0.4593412100222354);}
- 根据network栏的字体选项卡找到对应字体文件地址，下载；

做出定义：
    - 正常字符：页面正常显示的字符，
    - 编码字符：源文件中的编码字符
"""
font = TTFont("file.woff")
# k-v; key为 编码字符 的10进制表示， value为 正常字符 的unicode码表示
cmap = font.get("cmap").getBestCmap()
print(cmap)
font_dict = {}
for k, v in cmap.items():
    if v[3:]:  # value默认标记 uni   默认3位
        content = "\\u00" + v[3:] if len(v[3:]) == 2 else "\\u" + v[3:]  # uni51  \\u0051   uni4E00 \\u4E00
        # unicode码对应的字符，即正常字符
        real_content = content.encode('utf-8').decode('unicode_escape')
        # key的16进制表示
        k_hex = hex(k)
        # 网页返回的字体是以&#x开头  ，换成以这个开头，下面代码就是直接替换
        real_k = k_hex.replace("0x", "&#x")
        font_dict[real_k] = real_content

print(font_dict)
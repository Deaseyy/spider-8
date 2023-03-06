"""识别缺口位置"""
import io
from pathlib import Path

import ddddocr
from PIL import ImageChops, Image

# ===================================== 方式1 ===========================================
def compute_gap1(bg, full_bg):
    """使用 ddddocr库 进行缺口识别"""
    if isinstance(bg, str):
        with open(bg, 'rb') as f:
            bg = f.read()
        with open(full_bg, 'rb') as f:
            full_bg = f.read()

        # bg_img = Image.open(bg)
        # full_img = Image.open(full_bg)
        # # 创建一个字节流管道
        # bg_bytes = io.BytesIO()
        # full_bytes = io.BytesIO()
        # # 把PNG格式转换成的四通道转成RGB的三通道，然后再保存成jpg格式
        # bg_img = bg_img.convert("RGB")
        # full_img = full_img.convert("RGB")
        # # 将图片数据存入字节流管道， format可以按照具体文件的格式填写
        # bg_img.save(bg_bytes, format="JPEG")
        # full_img.save(full_bytes, format="JPEG")
        # # 从字节流管道中获取二进制
        # bg = bg_bytes.getvalue()
        # full_bg = full_bytes.getvalue()

    slide = ddddocr.DdddOcr(det=False, ocr=False)
    # 参数必须为byte类型
    res = slide.slide_comparison(bg, full_bg)
    print('缺口坐标：', res)
    return res.get('target')[0]  # x坐标, 即滑动距离


# ===================================== 方式2 ===========================================
def compute_gap2(bg, full_bg):
    """计算缺口偏移"""
    if isinstance(bg, (str, Path)):
        img_bg = Image.open(bg)
        img_full = Image.open(full_bg)
    elif isinstance(bg, bytes):
        img_bg = Image.open(io.BytesIO(bg))
        img_full = Image.open(io.BytesIO(full_bg))
    else:
        raise ValueError(f'输入图片类型错误, 必须是<type str>/<type Path>/<type bytes>: {type(bg)}')

    # 将图片修改为RGB模式
    img_bg = img_bg.convert("RGB")
    img_full = img_full.convert("RGB")

    # 计算差值
    diff = ImageChops.difference(img_bg, img_full)
    # 灰度图
    diff = diff.convert("L")

    table = []
    for i in range(256):
        if i < 50:
            table.append(0)
        else:
            table.append(1)

    # 二值化
    diff = diff.point(table, '1')

    left = 43
    # 这里做了优化为减少误差 纵坐标的像素点大于5时才认为是找到
    # 防止缺口有凸起时有误差
    for w in range(left, diff.size[0]):
        lis = []
        for h in range(diff.size[1]):
            if diff.load()[w, h] == 1:
                lis.append(w)
            if len(lis) > 5:
                return w


if __name__ == '__main__':
    bg = '../bg.jpg'
    full_bg = '../full.jpg'
    print(compute_gap1(bg, full_bg))
    print(compute_gap2(bg, full_bg))


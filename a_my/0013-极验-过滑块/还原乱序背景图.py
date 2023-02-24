import io
from pathlib import Path
from PIL import Image


def parse_bg_captcha(img, im_show=False, save_path=None):
    """
    滑块乱序背景图还原
    :param img: 图片路径str/图片路径Path对象/图片二进制
        eg: 'assets/bg.webp'
            Path('assets/bg.webp')
    :param im_show: 是否显示还原结果, <type 'bool'>; default: False
    :param save_path: 保存路径, <type 'str'>/<type 'Path'>; default: None
    :return: 还原后背景图 RGB图片格式
    """
    if isinstance(img, (str, Path)):
        _img = Image.open(img)
    elif isinstance(img, bytes):
        _img = Image.open(io.BytesIO(img))
    else:
        raise ValueError(f'输入图片类型错误, 必须是<type str>/<type Path>/<type bytes>: {type(img)}')

    # 极验的图片还原顺序, 定值（slide.js中写死的）
    _Ge = [39, 38, 48, 49, 41, 40, 46, 47, 35, 34, 50, 51, 33, 32, 28, 29, 27, 26, 36, 37, 31, 30, 44, 45, 43, 42, 12,
           13, 23, 22, 14, 15, 21, 20, 8, 9, 25, 24, 6, 7, 3, 2, 0, 1, 11, 10, 4, 5, 19, 18, 16, 17]
    w_sep, h_sep = 10, 80

    # 还原后的背景图
    new_img = Image.new('RGB', (260, 160))

    for idx in range(len(_Ge)):
        x = _Ge[idx] % 26 * 12 + 1
        y = h_sep if _Ge[idx] > 25 else 0
        # 从背景图中裁剪出对应位置的小块
        img_cut = _img.crop((x, y, x + w_sep, y + h_sep))
        # 将小块拼接到新图中
        new_x = idx % 26 * 10
        new_y = h_sep if idx > 25 else 0
        new_img.paste(img_cut, (new_x, new_y))

    if im_show:
        new_img.show()
    if save_path is not None:
        save_path = Path(save_path).resolve().__str__()
        new_img.save(save_path)
    return new_img


parse_bg_captcha('d401d55fc.webp', save_path='bg_parse.jpg')



# slide.js 中还原背景图的js代码，上面使用python来还原
"""
function $_BEG(t, e) {
    var $_DAHHo = QBLnx.$_Db()[12][19];
    for (; $_DAHHo !== QBLnx.$_Db()[15][16]; ) {
        switch ($_DAHHo) {
        case QBLnx.$_Db()[15][19]:
            t = t[$_CJEl(38)],
            e = e[$_CJEl(38)];
            var n = t[$_CJEl(64)]
              , r = t[$_CJEl(1)]
              , i = h[$_CJFA(32)]($_CJEl(57));
            i[$_CJEl(64)] = n,
            i[$_CJFA(1)] = r;
            $_DAHHo = QBLnx.$_Db()[3][18];
            break;
        case QBLnx.$_Db()[0][18]:
            var o = i[$_CJEl(44)]($_CJEl(22));
            o[$_CJEl(94)](t, 0, 0);
            var s = e[$_CJFA(44)]($_CJEl(22));
            $_DAHHo = QBLnx.$_Db()[0][17];
            break;
        case QBLnx.$_Db()[12][17]:
            e[$_CJEl(1)] = r,
            e[$_CJEl(64)] = 260;
            for (var a = r / 2, _ = 0; _ < 52; _ += 1) {
                var c = Ut[_] % 26 * 12 + 1
                  , u = 25 < Ut[_] ? a : 0
                  , l = o[$_CJFA(27)](c, u, 10, a);
                s[$_CJFA(81)](l, _ % 26 * 10, 25 < _ ? a : 0);
            }
            $_DAHHo = QBLnx.$_Db()[15][16];
            break;
        }
    }
}
"""
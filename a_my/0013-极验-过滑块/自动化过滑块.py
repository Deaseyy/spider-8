"""
步骤：
pip install selenium // 当前脚本运行版本：selenium==4.8.2
pip install ddddocr // 图像识别



"""
import base64
import time

import ddddocr
from selenium import webdriver

from selenium.webdriver.common.by import By


# 1.创建浏览器
options = webdriver.ChromeOptions()
# 过 navigator.webdriver 环境检测
options.add_argument('--disable-blink-features=AutomationControlled')
browser = webdriver.Chrome(options=options)
# 窗口最大化; 自动化过滑块, 最好是最大化, 可能会比例缩放
browser.maximize_window()
browser.get('https://www.geetest.com/demo/slide-float.html')


# 2.填写信息
browser.find_element(by=By.ID, value='username').send_keys('13811111111')
browser.find_element(by=By.ID, value='password').send_keys('123456')
time.sleep(2)

# 3.点击弹出验证
btn = browser.find_element(by=By.XPATH, value='//div[@class="geetest_btn"]/div[@class="geetest_radar_btn"]')
btn.click()

# 点击弹出验证码, 滑块内容还没出来, 需要等待一会儿，才能获取到图片(滑块标签是第三方js注入的)
time.sleep(2)
# 4.图片获取
# 备注： bg_src 为含缺口图， full_src 为完整原图
bg_src = browser.execute_script("return document.getElementsByClassName('geetest_canvas_bg geetest_absolute')[0].toDataURL('image/png')")
full_src = browser.execute_script("return document.getElementsByClassName('geetest_canvas_fullbg geetest_fade geetest_absolute')[0].toDataURL('image/png')")
print('bg_src: ', bg_src)
print('full_src: ', bg_src)

# 图片数据被 base64 编码过，需要解码
bg_base = bg_src.split(',')[1]  # 去掉 data:image/png;base64,
bg_base = base64.b64decode(bg_base)
with open('bg.jpg','wb') as f:
    f.write(bg_base)

full_base  = full_src.split(',')[1]
full_base = base64.b64decode(full_base)
with open('full.jpg','wb') as f:
    f.write(full_base)

# 注意：可以不用写入文件，直接使用文件流数据，传入缺口识别模型。

# 5.进行缺口识别
def read_img():
    slide = ddddocr.DdddOcr(det=False, ocr=False)
    with open('bg.jpg', 'rb') as f:
        target_bytes = f.read()
    with open('full.jpg', 'rb') as f:
        background_bytes = f.read()

    res = slide.slide_comparison(target_bytes, background_bytes)
    print('==缺口坐标：', res)
    return res.get('target')[0]  # x坐标

x = read_img()  # 缺口的x坐标

# 6.拖动滑块
# 选中拖动的按钮
slide = browser.find_element(By.CSS_SELECTOR, 'div.geetest_slider_button')
action_cn = webdriver.ActionChains(browser) # 添加一个事件
# 点击 且 按住鼠标左键不放开
action_cn.click_and_hold(slide)
action_cn.pause(0.2) # 暂停
# 拖动
action_cn.move_by_offset(x-10, 0)  # 标准位置 ,需要减去10 (滑块和图片边缘有间隔缝隙, 所有的极验如此)
action_cn.pause(0.8)
action_cn.move_by_offset(10, 0) # 往前走 10  模拟手抖一抖
action_cn.pause(1.4)
action_cn.move_by_offset(-10, 0)  # 回退10
# 松开鼠标
action_cn.release()
# 执行事件
action_cn.perform()

# 7.点击提交
browser.find_element(By.ID, 'btn').click()
time.sleep(10)

'''
鼠标动作:
    click_and_hold  点击鼠标左键 不放开
    move_by_offset  鼠标移动指定距离
    release  松开鼠标

行为控制:
    perform 执行事件
    pause 事件的时间间隔
'''

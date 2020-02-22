"""
滑动和拖拽事件
滑动方法：
1.能够使用 swipe滑动屏幕
2.能够使用 scroll 滑动屏幕
3.能够使用 dfag_and_drop 滑动屏幕

Swipe滑动方式
·方法：
。driver.swipe（起始×坐标，起始y坐标，结束×坐标、结束y坐标，持续时间ms）
·特点：
。参数是坐标点
。持续时间短，惯性大。持续时间长，惯性小
"""
from appium import webdriver

desired_caps = {
                'platformName': 'Android',
                'platformVersion': '5.1',
                'appPackage': 'com.android.settings',
                'appActivity': '.Settings',
                'deviceName':  '127.0.0.1:62001',
                # 默认中文无效，需添加 unicodekeyboard，resetkeyboard两个参数
                'unicodekeyboard': 'True',
                'resetkeyboard': 'True'}
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)


# swipe滑动事件
# 概念
# 从一个坐标位置滑动到另一个坐标位置，只能是两个点之间的滑动。
# 方法名
# 从一个坐标位置滑动到另一个坐标位置，只能是两个点之间的滑动章参数：
# startx：起点X轴坐标#starty：起点Y陆坐标
# end_x：终点X轴坐标
# end-y：终点Y轴坐标
# duration：滑动这个操作一共持线的时间长度，单位：ms毫秒
# driver.swipe(start_x=1, start_y=2, end_x=3, end_y=4, duration=None)
# 滑动的距离越长，展示的效果越靠后
# 距离相同时，持续时间越长，惯性越小

driver.swipe(100, 2000, 100, 1000, 2000)

# 退出
driver.quit()
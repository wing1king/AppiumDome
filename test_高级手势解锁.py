"""
解锁画图
"""
import time
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction

desired_caps = {
    'platformName': 'Android',
    'platformVersion': '5.1',
    'appPackage': 'com.android.settings',
    'appActivity': '.Settings',
    'deviceName': '127.0.0.1:62001',
    # 默认中文无效，需添加 unicodekeyboard，resetkeyboard两个参数
    'unicodekeyboard': 'True',
    'resetkeyboard': 'True'}
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

# 移动操作【掌握】
# 应用场景
# 模拟手指移动操作，比如，手势解锁需要先按下，再移动。
# 方法名
# 模拟手指对元素或坐标的移动操作
# 参数：
# e1：元素
# ×：×坐标
# y:y坐标
# Touchection（driver）.move_to（el=None，X=None，y=None）.perform（）

TouchAction(driver).press(x=122, y=680).move_to(x=165, y=780).release().perform()

driver.quit()

"""
移动
关键方法
omove_to
参数：
    可以传入元素
        使用el参数
    可以传入坐标
        使用x和y参数
"""








# 移动操作【掌握】
# 应用场景
# 模拟手指移动操作，比如，手势解锁需要先按下，再移动。
# 方法名
# 模拟手指对元素或坐标的移动操作
# 参数：
# e1：元素
# ×：×坐标
# y:y坐标
# Touchection（driver）.move_to（el=None，X=None，y=None）.perform（）

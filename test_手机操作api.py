"""
手机操作api
"""

from appium import webdriver

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


driver.quit()

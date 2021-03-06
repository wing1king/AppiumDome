"""
应用前后台
"""
from appium import webdriver

desired_caps = {
                'platformName': 'Android',
                'platformVersion': '5.1',
                'appPackage': 'com.android.settings',
                'appActivity': '.Settings',
                'deviceName':  '127.0.0.1:62001',
                'noReset': 'True'}
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

# 输出当前程序的包名和界面名
print(driver.current_package)
print(driver.current_activity)

# app放置到后台一定时间后再回到前台，模拟热启动
# 参数：
# 后台停留5秒
driver.background_app(5)

# 关闭当前操作的app，不会关闭驱动对象
driver.close_app

# 关闭驱动对象，同时关闭所有关联的app
driver.quit()

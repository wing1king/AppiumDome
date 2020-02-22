import time
from appium import webdriver

desired_caps = {
                'platformName': 'Android',
                'platformVersion': '5.1',
                'appPackage': 'com.android.settings',
                'appActivity': '.Settings',
                'deviceName':  '127.0.0.1:62001',
                'noReset': 'True'}
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
# 如果安装则卸载
if driver.is_app_installed("cn.goapk.market"):
    driver.remove_app("包名")
else:
    # 安装包路径
    driver.install_app("/users/roson/oesktop/anzhishichang.apk")
# 等待
time.sleep(5)
# 退出
driver.quit()

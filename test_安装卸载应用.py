"""
安装和卸载应用
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

# 安装app
# 参致：
#  app_path:apk路径
driver.install_app("app_path")

# 卸载app
# 参数；
# app_id：应用程序包名
driver.remove_app("app_id")

# 判断app是否已经安装
# 参数：
# app_id：应用程序包名
# 返回值：
# 布尔类型，True为安装，False为没有安装
driver.install_app("app_path")

driver.quit()
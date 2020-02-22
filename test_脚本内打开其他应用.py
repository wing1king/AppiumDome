from appium import webdriver

desired_caps = {
                'platformName': 'Android',
                'platformVersion': '5.1',
                'appPackage': 'com.android.settings',
                'appActivity': '.Settings',
                'deviceName':  '127.0.0.1:62001',
                'noReset': 'True'}
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

# 脚本内启动其他app
# apppackage：要打开的程序的包名
# appActivity：要打开的程序的界面名
driver.start_activity("apppackage", "appActivity")

driver.quit()
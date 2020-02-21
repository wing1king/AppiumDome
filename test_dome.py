from appium import webdriver

desired_caps = dict()
# 手机参数
desired_caps['platformName'] = 'Android'
desired_caps['platformversion'] = '5.1'
desired_caps['devicewane'] = '192.168.56.101：5555'
# 应用参数
desired_caps['apppackage'] = "com.android.settings"
desired_caps['appActivity'] = '.settings'
# 获取
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

# 脚本内启动其他app
# apppackage：要打开的程序的包名
# appActivity：要打开的程序的界面名
driver.start_activity("apppackage", "appActivity")

# 存输出当前程序的包名和界面名
print(driver.current_package)
print(driver.current_activity)

# 退出
driver.quit()

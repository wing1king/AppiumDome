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
driver.is_app_installed("app_id")

# 关闭当前操作的app，不会关闭驱动对象
driver.close_app

# 关闭驱动对象，同时关闭所有关联的app
driver.quit()
# 退出
driver.quit()

# 如果《安智市场》已经安装，则卸载《安智市场》，如果没有则安装
import time
from appium import webdriver

desired_caps = dict()
# 手机参数
desired_caps['platformName'] = 'Android'
desired_caps['platforamversion'] = '5.1'
desired_caps['deviceName'] = '192.168.56.101:5555'
# 应用参数
desired_caps['apppackage'] = 'com.android.settings'
desired_caps['appActivity'] = '.settings'

# 获取driver
driver = webdriver.Remote("http://localhost：4723/wd/hub'，desired_caps")
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

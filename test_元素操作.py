"""
元素操作
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
# 点击
driver.find_element_by_id("").click()

# 输入
driver.find_element_by_class_name("").send_keys("要输入的内容")

# 清空
driver.find_element_by_xpath().clear()

# 退出
driver.quit()
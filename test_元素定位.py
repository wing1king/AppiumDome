"""
元素等待
"""
import time
from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

desired_caps = {
                'platformName': 'Android',
                'platformVersion': '5.1',
                'appPackage': 'com.android.settings',
                'appActivity': '.Settings',
                'deviceName':  '127.0.0.1:62001',
                'noReset': 'True'}
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
# 所有查找元素方法隐式等待10s
driver.implicitly_wait(10)

# 显式等待
# 5表示一个找几s
# 1表示多久找一次
wait = WebDriverWait(driver, 5, 1)
back_1 = wait.until(lambda x: x.driver.find_elements_by_id("com.android.settings:id/title"))
back_1.click()

driver.quit()
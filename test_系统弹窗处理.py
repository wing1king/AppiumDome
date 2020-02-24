"""
系统弹窗处理和跳过首页开屏图
"""

import time
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

desired_caps = {
                'platformName': 'Android',
                'platformVersion': '8.0',
                'appPackage': 'com.idreamsky.riko',
                'appActivity': '.MainActivity',
                'deviceName':  '127.0.0.1:62001',
                'noReset': 'True'}
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

time.sleep(5)

for i in range(5):
    loc = ("xpath", "//*[@text='始终允许']")

    try:
        e = WebDriverWait(driver, 1, 0.5).until(EC.presence_of_element_located(loc))
        e.click()
    except:
        pass
        print("已检测系统弹窗")
time.sleep(1)
try:
    driver.find_element_by_xpath("//*[@text='跳过']").click()
except:
    pass

time.sleep(5)

driver.quit()
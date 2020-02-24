"""
系统弹窗处理和跳过首页开屏图

fuction：权限弹窗-始终允许
args：
1.传driver
2.number，判断弹窗次数，默认给5次
其它：
WebDriverwait里面0.5s判断一次是否有弹窗，1s超时

for i in range（number）：
1oc=（"xpath"，"//*[@text=’始终允许]"）try：
e=Webpriverwait（driver，1，e.5）.until（EC.presence_of_element_located（1oc））
e.click（）exceRt：
pass


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
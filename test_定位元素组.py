"""
定位组元素
"""
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

titles = driver.find_elements_by_id("com.android.settings:id/title")
print(titles)
print(len(titles))
for res in titles:
    print(res)
titles[2].click()

text = driver.find_elements_by_class_name("android.widget.TextView")
print(titles)

# 通过xpath的形式，获取所有包含”设“的元素，并打印其文字内容
eles = driver.find_elements_by_xpath("//*[containscetext，'设）]")

print(eles)

time.sleep(2)

driver.quit()
"""
获取元素位置和大小
"""
from appium import webdriver

desired_caps = {
                'platformName': 'Android',
                'platformVersion': '5.1',
                'appPackage': 'com.android.settings',
                'appActivity': '.Settings',
                'deviceName':  '127.0.0.1:62001',
                # 默认中文无效，需添加 unicodekeyboard，resetkeyboard两个参数
                'unicodekeyboard': 'True',
                'resetkeyboard': 'True'}
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

search_button = driver.find_element_by_id("")
# 获取element的位置
# 返回值：
# 字典，x为元素的×坐标，y为元素的y坐标
print(search_button.location)
print(search_button.location["×"])
print(search_button.location["y"])
# 获取element的大小
# 返回值：
# 字典，width为宽度，height为高度
print(search_button.size)
print(search_button.size["width"])
print(search_button.size["height"])

# 退出
driver.quit()
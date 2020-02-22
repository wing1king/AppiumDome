"""
获取元素的属性值
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
# 应用场景
# 根据特征定位到元素后，使元素的属性名获取对应的属性值方法名
# 对element进行点击操作
# 参数：
# value：要获取的属性名
# 返回值：
# 根据属性名得到的属性值
# element.get_attribute（value）#value：元素的属性

titles = driver.find_elements_by_id("com. android. settings: id/title")
for title in titles:
    print(title. get_attribute("enabled"))
    print(title. get_attribute("text"))
    print(title. get_attribute("name"))
    print(title. get_attribute("resourcerId"))
    print(title. get_attribute("className"))

# 退出
driver.quit()
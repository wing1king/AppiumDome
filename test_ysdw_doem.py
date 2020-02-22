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
# 通过id定位一个元素
# 参数：
# id_value：元素的resource-id属性值
# 返回值；
# 定位到的单个元素
driver.find_element_by_id("")

# 通过c1lass_name定位一个元素
# 参数：
# class_value：元素的class属性值
# 返偏值：
# 定位到的单个元素
driver.find_element_by_class_name("")

# 通过xpath定位一个元素
# 参数
# xpath.value：定位元素的xpath表达式
# 返回值：
# 定位到的单个元素
driver.find_element_by_xpath()


# 1.2定位一组元素【掌握】
# 应用场景
# 和定位一个元素相同，但如果想要批量的获取某个相同特征的元素，使用定位一组元素的方式更加方便。
# 方法名
# 通过id定位一组元素
# 参数：
# id_value；元素的resource-id属性值
# 返回值：
# 列表，定位到的所有符合深价你的元素
driver.find_elements_by_id("id_value")

# 通过class_name定位一组元素
# 参数：
# class-value：元素的class属性值
# 返回值：
# 列表，定位到的所有符合调价你的元素
driver.findelements_by_class_name("class-value")

# 通过xpath定位一组元素
# 参数：
# xpath_value：定位元素的xpath表达式
# 返回值：
# 列表，定位到的所有符合调价你的元素
driver.findelements_by_xpath("xpath_value")
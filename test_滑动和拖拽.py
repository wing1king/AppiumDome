"""
滑动和拖拽事件
滑动方法：
1.能够使用 swipe滑动屏幕
2.能够使用 scroll 滑动屏幕
3.能够使用 dfag_and_drop 滑动屏幕

Swipe滑动方式
·方法：
。driver.swipe（起始×坐标，起始y坐标，结束×坐标、结束y坐标，持续时间ms）
·特点：
。参数是坐标点
。持续时间短，惯性大。持续时间长，惯性小
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


# swipe滑动事件
# 概念
# 从一个坐标位置滑动到另一个坐标位置，只能是两个点之间的滑动。
# 方法名
# 从一个坐标位置滑动到另一个坐标位置，只能是两个点之间的滑动章参数：
# startx：起点X轴坐标#starty：起点Y陆坐标
# end_x：终点X轴坐标
# end-y：终点Y轴坐标
# duration：滑动这个操作一共持线的时间长度，单位：ms毫秒
# driver.swipe(start_x=1, start_y=2, end_x=3, end_y=4, duration=None)
# 滑动的距离越长，展示的效果越靠后
# 距离相同时，持续时间越长，惯性越小

driver.swipe(100, 2000, 100, 1000, 2000)

# scroll滑动事件（有惯性）
# 概念
# 从一个元素滑动到另一个元素，直到页面自动停止。
# 方法名
# 从一个元素滑动到另一个元素，直到页面自动停止
# 参数：
# origin_el：滑动开始的元素
# destination_el：滑动结束的元素
# driver.scroll(origin_el，destination.el)
# 示例
# 从“存储”滑动到“更多”
# 核心代码
save_button = driver.find_element_by_xpath("//*[@text='存储]")
more_button = driver.find_element_by_xpath("//？[@text='更多]")
driver.scroll(save_button, more_button)

# drag and_drop拖搜事件（不能设置时间，没有惯性）
# 概念
# 从一个元素滑动到另一个元素，第二个元素替代第一个元素原本屏幕上的位置。
# 方法名
# 从一个元素滑动到另一个元素，第二个元素替代第一个元素原本屏幕上的位置
# 参数：
# origin_el：滑动开始的元素
# destination_el：滑动结束的元素
# driver.drag_and_drop(origin_e1，destination-el)
# 示例
# 将“存储”拖搜到“更多”
# 核心代码
save_button = driver.find_element_by_xpath("//*[etext='存储]")
more_button = driver.find_element_by_xpath("//*[@text='更多]")
driver.drag_and_drop(save_button, more_button)

# 退出
driver.quit()
"""
小结：
swipe滑动方式
方法：
driver.swipe（起始×坐标，起始y坐标，结束×坐标，结束y坐标，持续时间ms）
特点：
参数是坐标点
持续时间短，惯性大。持续时间长，惯性小

scroll滑动方式
方法：
driver.scroll（起始元素，结束元素）
特点：
参数是元素
没有持续时间，有惯性

drag and_drop滑动方式
方法：
driver.dragand_drop（起始元素，结束元素）
特点：
参数是元素
没有持续时间，没有惯性
"""

"""
滑动和拖拽事件的选择
滑动和拖拽无非就是考虑是否有“惯性”，以及传递的参数是“元素”还是“坐标”。
可以分成以下四种情况:

有“惯性”，传入“元素”
oscroll

无“惯性”，传入“元素”
drag_and_drop

有“惯性”，传入“坐标”
swipe，并且设置较短的duration 时间

无“惯性”，传入“坐标”
swipe，并且设置较长的duration时间

三种方式的选择
有惯性，传入参数坐标
swipe，设置较短的持续时间
有惯性，传入参数元素
scroll
无惯性，传入参数坐标
swipe，设置较长的持续时间
无惯性，传入参数元素
drag_and_drop
"""
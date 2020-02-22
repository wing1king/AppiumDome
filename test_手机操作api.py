"""
手机操作API
学习目标
    1.能够获取手机分辨率
    2.能够获取手机截图
    3.能够获取和设置网络状态
    4.能够发送键到设备
    5.能够打开和关闭手机通知栏
"""
from appium.webdriver.connectiontype import ConnectionType
from appium import webdriver

desired_caps = {
    'platformName': 'Android',
    'platformVersion': '5.1',
    'appPackage': 'com.android.settings',
    'appActivity': '.Settings',
    'deviceName': '127.0.0.1:62001',
    # 默认中文无效，需添加 unicodekeyboard，resetkeyboard两个参数
    'unicodekeyboard': 'True',
    'resetkeyboard': 'True'}
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

# 手机操作API
# 1.1获取手机分辨率【掌握】
# 应用场景
# 自动化测试可能会需要根据当前设备的屏幕分辨率来计算一些点击或者滑动的坐标
# 方法名
# #获取手机分辨率
# driver.get_window_size（）
# 示例
# 输出当前设备的屏幕分辨率
# 核心代码
# print（driver.get-window_size））

res = driver.get_window_size()

print(res)

# 手机截图【掌握】
# 应用场景
# 有些自动化的操作可能没有反应，但并不报错。此时我们就可以将操作过后的关键情况，截图留存。后期也可以根据图片发现问题。
# 方法名
# 获取手机分辨率
# 参数：
# filename：指定路径下，指定格式的图片
# get_screenshotas_file（filename）
# 示例
# 1.打开设置页面
# 2.截图当前页面保存到当前目录，命名为screen.png核心代码
driver.get_screenshot_as_file("d:/screen.png")
# 执行效果
# 项目目录下会将设置页面保存成screen.png

# 获取和设置手机网络【掌握】
# 应用场景
# 视频应用在使用流露看视频的时候，大部分都会提示用户正在是否继续播放。作为测试人员，
# 我们可能需要用自动化的形式来判断是否有对应的提示。即，用流量的时候应该有提示，不用流量的时候应该没有提示。
# 获取手机网络
# 属性名
# 获取手机网络
# driver.network_connection
# 示例
# 获取当前网络类型，并打印
# 核心代码
print(driver.network_connection)
# 设置当前网络    1 飞行 2.
driver.set_network_connection(2)
# 判断当前网络
if driver.network_connection == ConnectionType.DATA_ONLY:
    print(1)
else:
    print(2)

# 发送键到设备【掌握】
# 应用场景
# 模似按“返回键”home键”等等操作，比如，很多应用有按两次返回键退出应用的功能，
# 如果这个功能需要我们做自动化，那么一定会用到这个方法
# 方法名
# 发送键到设备
# 参数：
# keycode：发送给设备的关键代码
# metastate：关于被发送的关键代码的元信息，一般为默认值
# driver.press_keycode(keycode, metastate=None)
# 注意点
# 按键对应的编码，可以在百度搜索关键字"android keycode”
# 例如：https://blog.csdn.net/midux/article/details/80064054
# 需求：三次音量+返回两次音量-
driver.press_keycode(24)
driver.press_keycode(24)
driver.press_keycode(24)
driver.press_keycode(4)
driver.press_keycode(25)
driver.press_keycode(25)

# 操作手机通知栏
# 应用场景
# 测试即时通信类软件的时候，如果A给B发送一条消息，B的通知栏肯定会显示对应的消息。
# 我们想通过通知栏来判断B是否收到消息，一定要先操作手机的通知栏
# 方法名
# 打开手机通知栏
# driver.open_notifications()
# 注意点
# appium官方并没有为我们提供关闭通知的api，那么现实生活中怎么关闭，就怎样操作就行，比如，手指从下往上滑动，或者，按返回键
# 示例
# 打开通知栏，两秒后，关闭通知栏
# 核心代码
# 打开通知栏
driver.open_notifications()

# 退出
driver.quit()

"""
如何获取手机分辨率
关键方法：
driver_get_window_size
返回值：
    字典
    里面有两个key,分别是width 和height
    宽和高的值是int类型的
    
如何截图
关键方法：
driver_get_screenshot_as_file
参数：
    文件的路径
    如果直接写了文件名，则会默认保存在项目目录下
    
如何获取和设置当前手机的网络
获取网络状态
属性
    network_connection
设置网络状态
方法
    set_network_connection 
参数
    网络类型
注意点：
    网络的类型，建议使用系统提供的类型
from appium.webdriver.connectiontype import ConnectionType

发送键到设备
driver.press_keycode()
参数
    按键对应的编码
    
操作通知栏
打开
driver.open_notifications
关闭
    使用返回键
    press_keycode(4)
"""

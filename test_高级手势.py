"""
高级手势
1.能够使用代码完成轻敲手势
2.能够使用代码完成按下手势
3.能够使用代码完成抬起手势
4.能够使用代码完成等待操作
5.能够使用代码完成长按手势
6.能够使用代码完成手指移动操作
一.高级手势TouchAction
应用场景
TouchAction可以实现一些针对手势的操作，比如滑动、长按、拖动等。
我们可以将这些基本手势组合成一个相对复杂的手势。比如，我们解锁手机或者一些应用软件都有手势解锁的这种方式。
使用步骤
1.创建TouchAction对象
2.通过对象调用想执行的手势
3.通过perform()执行动作
注意点
所有手势都要通过执行perform()函数才会运行。
"""
import time
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction

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

# 手指轻敲操作【掌握】
# 应用场景
# 模拟手指对某个元素或坐标按下并快速抬起。比如，固定点击（100，100）的位置。
# 方法名
# 模拟手指对元素域坐标的轻触操作
# 参数：
# element：元素
# x：×继标#y:y坐标
# TouchAction（driver）.tap（elementaNone，x=None，y=None）.perform）
# 示例
# 1.打开《设置》
# 2.轻敲"WLAN”

# 核心代码
# 1.创建touchaction对象
# 2.调用想要执行的动作
el = driver.find_element_by_xpath("//*[contains（@text，'WLAN）]")
# 3.使用perform执行动作
TouchAction(driver).tap(el).perform()
# 通过坐标传参    count=2 为点击次数
TouchAction(driver).tap(x=100, y=200, count=2).perform()

# 按下和抬起操作【掌握】
# 应用场景
# 模拟手指一直按下，模拟手指抬凝。可以用来组合成轻敲或长按的操作方法名
# 模拟手指对元素或坐标的按下操作
# 参数：
# e1：元素
# x：×坐标
# y: y坐标
# TouchAction（driver）.press（el=None，X=None，y=None）.perform()
# 模拟手指对元素或坐标的抬起操作
# TouchAction（driver）.release().perform()
# 示例1
# 使用坐标的形式点击WLAN（650，650），2秒后，按下（650，650）的位置
# 核心代码
TouchAction(driver).press(X=650, y=650).perform()
time.sleep(2)
TouchAction(driver).press(X=650, y=650).perform()
# 示例2
# 使用坐标的形式点击WLAN（650，650），2秒后，按下（650，650）的位置，并抬起
# 核心代码
TouchAction(driver).press(X=650, y=650).perform()
time.sleep(2)
TouchAction(driver).press(X=650, y=650).release().perform()

# 等待操作【掌握】
# 应用场景
# 模拟手指等待，比如按下后博待5秒之后再抬起。
# 方法名
# 模拟手指暂定操作
# 参致：
# ms：暂停的毫秒数
# Touchection（driver）.wait（ms=0）.perform()
# 示例
# 使用坐标的形式点击 WLAN（650，650），2秒后，按下（650，650）的位置，暂停2秒，并抬起
# 核心代码
TouchAction(driver).tap(x=650, y=650).perform()
time.sleep(2)
TouchAction(driver).tap(x=650, y=650).perform().wait(2000).release().perform()

# 长按操作【掌握】
# 应用场景
# 模拟手指对元素或坐标的长按操作。比如，长按某个按钮弹出菜单。
# 方法名
# 模拟手指对元素或坐标的长按操作
# 参致：
    # el：元素
    # x：×坐标
    # #y:y坐标
# duration；长按时间，毫秒
# TouchAction（driver）.long_press（el=None，x=None，y=None，duration=1000）.perform()
# 示例
# 使用坐标的形式点击 WLAN（650，650），2秒后，长按（650，650）的位置持续2秒核心代码
TouchAction(driver).tap(x=400, y=400).perform()
time.sleep(2)
TouchAction(driver).long_press(x=400, y=400, duration=2000).release().perform()

# 退出
driver.quit()

"""
TouchAction
概念和作用：
高级手势，可以将小的动作组合成一系列复杂的动作
·步骤：
1.创建TouchAction对象
2.通过对象调用要执行的动作
3.通过perform进行执行

轻敲
关键方法：
tap
参数：
可以传入元素
    使用 element参数
可以传入坐标
    使用×和y参数
多次点击
    使用count参数

按下
关键方法：
press
参数：
可以传入元素
    使用 el参数
可以传入坐标
    使用×和y参数
    
抬起
关键方法：
    release
    
等待
关键方法：。
wait
参数：
    等待的时长（毫秒）
        使用ms参数    

长按
关键方法：
long.press
参数：
    可以传入元素
        使用el参数
    可以传入坐标
        使用x和y参数
    设置持续时间
        使用duration参数（毫秒）
额外补充
    长按<==>按下,等待,抬手
        
"""

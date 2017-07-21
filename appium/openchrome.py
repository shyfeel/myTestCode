#-*- coding: UTF-8 -*-
from appium import webdriver  #引入appium
from time import sleep
#通过chrome打开网站，并且截图
desired_caps={}
desired_caps['device'] = 'android'
desired_caps['platformName']='Android'
desired_caps['browserName']='chrome'
desired_caps['version']='4.4.4' #手机的android版本号
desired_caps['deviceName']='24eac1a2' #adb devices探测到的手机ID
#desired_caps['appPackage'] ='com.tencent.mm' #app的包名
#desired_caps['appActivity'] ='com.tencent.mm.ui.LauncherUI' #app的activity名

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
driver.get("http://www.qq.com")
#sleep(5)
#driver.get_screenshot_as_file("d:/temp/appiumscreenshot.png")
sleep(5)
#需要切换到native_app模式下才能使用tap操作
body = driver.find_element_by_tag_name("body")
#driver.switch_to.context('NATIVE_APP')
#driver.tap([(560,768)])

print body.location
#driver.swipe(175,500,175,0,800)
#driver.tap([(320,570)],500);
sleep(10)
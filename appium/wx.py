#-*- coding: UTF-8 -*-
from appium import webdriver  #引入appium
from time import sleep
#本脚本演示在手机上启动微信登陆的过程，在微信版本6.5.10测试通过，红米note1，24eac1a2
desired_caps={}
desired_caps['device'] = 'android'
desired_caps['platformName']='Android'
#desired_caps['browserName']='chrome'
desired_caps['version']='4.4.4' #手机的android版本号
desired_caps['deviceName']='24eac1a2' #adb devices探测到的手机ID
desired_caps['appPackage'] ='com.tencent.mm' #app的包名
desired_caps['appActivity'] ='com.tencent.mm.ui.LauncherUI' #app的activity名

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
sleep(10)
driver.find_element_by_android_uiautomator('new UiSelector().text("登录")').click()
sleep(5)
#driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.tencent.mm:id/eu")').click()
#sleep(5)
textfield1 = driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.tencent.mm:id/nu")')#通过text属性获取控件
#textfield1 = driver.find_element_by_android_uiautomator('new UiSelector().text("你的手机号码")')#通过text属性获取控件
sleep(2)
textfield1.send_keys("13424161992")#使用手机号登陆
sleep(2)
driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.tencent.mm:id/adj")').click()#点击下一步
textfield2 = driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.tencent.mm:id/fl")')#通过resource-id属性获取控件密码框
sleep(2)
textfield2.send_keys("12345678")
sleep(2)
driver.find_element_by_android_uiautomator('new UiSelector().text("登录")').click()#click点击此控件
sleep(10)
#driver.find_element_by_android_uiautomator('new UiSelector().text("我")').click()

#driver.find_element_by_android_uiautomator('new UiSelector().text("钱包")').click()

#driver.find_element_by_android_uiautomator('new UiSelector().text("理财通")').click()


driver.quit()
#-*- coding: UTF-8 -*-
from appium import webdriver  #引入appium
from time import sleep
import cv2
from selenium.webdriver.common.action_chains import ActionChains
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
driver.get("http://www.shyfeel.com/mouse/")
sleep(2)
layaCanvas = driver.find_element_by_id("layaCanvas")
sleep(5)

body = driver.find_element_by_tag_name("body")

driver.switch_to.context('NATIVE_APP')
driver.get_screenshot_as_file("d:\imgtest\screen.jpg")

imgNum = 0

def startgame():
    img = cv2.imread('D:\imgtest\screen.jpg',0)
    img2 = img.copy()
    template = cv2.imread('D:\imgtest\startgame.jpg',0)
    w, h = template.shape[::-1]

    methods = ['cv2.TM_CCOEFF']

    for meth in methods:
        img = img2.copy()
        method = eval(meth)

        # Apply template Matching
        res = cv2.matchTemplate(img,template,method)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
        #min_loc最小值位置，max_loc最大值位置，
        #print min_loc;
        #print max_loc;
        #print max_loc[0];
        #print max_loc[1];
        x = max_loc[0]+100
        y = max_loc[1]+40
        print x,y
    #点击开始游戏按钮
    sleep(5)
    #driver.switch_to.context('NATIVE_APP')
    driver.tap([(x,y)],1000)
    #print body.location
    #driver.tap([(x,y),(x,y)],500)
    #ActionChains(driver).move_to_element_with_offset(body, x, y).click().perform()
    #sleep(5)
def hitmouse():
    global imgNum
    driver.get_screenshot_as_file("d:\imgtest\gamescreen"+str(imgNum)+".jpg")
    img3 = cv2.imread("d:\imgtest\gamescreen"+str(imgNum)+".jpg",0)

    imgNum = imgNum + 1
    img4 = img3.copy()
    template1 = cv2.imread('D:\imgtest\gm1.jpg',0)
    w, h = template1.shape[::-1]

    methods = ['cv2.TM_CCOEFF']

    for meth in methods:
        img3 = img4.copy()
        method = eval(meth)

        # Apply template Matching
        res = cv2.matchTemplate(img3,template1,method)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
        print "max_val=",max_val
        #匹配度大于xxx才作为目标敲击
        if max_val >=20000000.0:
            
            #min_loc最小值位置，max_loc最大值位置，
            x = max_loc[0]+50
            y = max_loc[1]+50
            driver.tap([(x,y)],10)
            print "tap"
        else:
            x = 0
            y = 0
        #print x,y
    #点击匹配的老鼠
    #ActionChains(driver).move_to_element_with_offset(body, x, y).click().perform()
    #driver.tap([(x,y),])
    
    print x,y
    #sleep(0.1)
    #再点一次
    #ActionChains(driver).move_to_element_with_offset(body, x, y).click().perform()
    #driver.tap([(x,y)],10)
    
startgame()
for i in range(15):
    hitmouse()
    #sleep(1)
#coding=utf-8
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

import cv2

chromedriver = "D:\github\myTestCode\Selenium\chromedriver.exe"
os.environ["webdriver.chrome.driver"] = chromedriver



driver = webdriver.Chrome(chromedriver)
driver.maximize_window()
#driver.get("http://res.luckyfish.qq.com/test/dev10/?_wv=133120&log=yes")
driver.get("http://res.luckyfish.qq.com/test/dev10/?_wv=133120")
sleep(20)
#driver.find_element_by_id("layaCanvas").send_keys("selenium2")
layaCanvas = driver.find_element_by_id("layaCanvas")
sleep(5)
driver.save_screenshot("d:\imgtest\screen.jpg")
body = driver.find_element_by_tag_name("body")

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
    ActionChains(driver).move_to_element_with_offset(body, x, y).click().perform()

def hitmouse():
    driver.save_screenshot("d:\imgtest\gamescreen.jpg")
    img3 = cv2.imread('D:\imgtest\gamescreen.jpg',0)
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
        else:
            x = 0
            y = 0
        print x,y
    #点击匹配的老鼠
    ActionChains(driver).move_to_element_with_offset(body, x, y).click().perform()
    sleep(0.1)
    ActionChains(driver).move_to_element_with_offset(body, x, y).click().perform()
    
startgame()
sleep(2)

driver.execute_script("Laya.Stat.show(0,0);")
sleep(2)
fps = driver.execute_script("return Laya.Stat.FPS")
print "the fps:"+str(fps)

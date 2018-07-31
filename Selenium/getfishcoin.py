#coding=utf-8
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
import logging as LOG

import cv2

chromedriver = "D:\github\myTestCode\Selenium\chromedriver.exe"
os.environ["webdriver.chrome.driver"] = chromedriver


#driver = webdriver.PhantomJS()
driver = webdriver.Chrome(chromedriver)
driver.maximize_window()
driver.get("http://res.luckyfish.qq.com/test/dev10/?_wv=133120&log=yes")
sleep(10)
driver.find_element_by_id("u").clear()
driver.find_element_by_id("u").send_keys("13117319")
driver.find_element_by_id("p").clear()
driver.find_element_by_id("p").send_keys("test1234")
driver.find_element_by_id("go").click()
sleep(10)
#driver.find_element_by_id("layaCanvas").send_keys("selenium2")
layaCanvas = driver.find_element_by_id("layaCanvas")
sleep(5)
driver.save_screenshot("d:\imgtest\screen.jpg")
body = driver.find_element_by_tag_name("body")

#关闭每日转盘抽奖
def closedaydraw():
    img = cv2.imread('D:\imgtest\screen.jpg',0)
    img2 = img.copy()
    template = cv2.imread('D:\imgtest\close.jpg',0)
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
        x = max_loc[0]+25
        y = max_loc[1]+25
        print x,y
    #点击右上角x关闭按钮
    ActionChains(driver).move_to_element_with_offset(body, x, y).click().perform()

#快速进入游戏
def quickstart():
    driver.save_screenshot("d:\imgtest\screen1.jpg")	
    img = cv2.imread('D:\imgtest\screen1.jpg',0)
    img2 = img.copy()
    template = cv2.imread('D:\imgtest\quickstart.jpg',0)
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
        x = max_loc[0]+25
        y = max_loc[1]+25
        print x,y
    #点击右上角x关闭按钮
    ActionChains(driver).move_to_element_with_offset(body, x, y).click().perform()


def autofire():
    driver.save_screenshot("d:\imgtest\screen2.jpg")	
    img = cv2.imread('D:\imgtest\screen2.jpg',0)
    img2 = img.copy()
    template = cv2.imread('D:\imgtest\quickq.jpg',0)
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
        x = max_loc[0]+25
        y = max_loc[1]+25
        print x,y
    #点击右上角x关闭按钮
    ActionChains(driver).move_to_element_with_offset(body, x, y).click().perform()
	
	
sleep(0.2)

LOG.basicConfig(level=LOG.INFO,
#format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
format='%(asctime)s %(message)s',
#datefmt='%a, %d %b %Y %H:%M:%S',
datefmt='%H:%M:%S',
filename='test.log',
filemode='w')

closedaydraw()
sleep(1)
quickstart()
sleep(10)
autofire()
while True:
	coin = driver.execute_script("return ApplicationData.selfUserInfo.gold_num")
	print "the coin:"+str(coin)
	LOG.info('The coins is:'+str(coin))
	sleep(3)
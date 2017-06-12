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
driver.get("http://www.shyfeel.com/mouse/")
#driver.find_element_by_id("layaCanvas").send_keys("selenium2")
layaCanvas = driver.find_element_by_id("layaCanvas")
sleep(5)
driver.save_screenshot("d:\imgtest\screen.jpg")
body = driver.find_element_by_tag_name("body")
#点击开始游戏的按钮坐标
#ActionChains(driver).move_to_element_with_offset(layaCanvas, 410, 490).click().perform()

#执行调用js脚本
#js='alert("调用js测试")'
#driver.execute_script(js)


#driver.execute_script('alert("调用js测试")')

#driver.execute_script('GameStart.startBtn.click()')

#driver.quit()
#截图整个窗口
#driver.save_screenshot("d:\imgtest\screen.jpg")

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

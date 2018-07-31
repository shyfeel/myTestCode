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
driver.get("http://res.luckyfish.qq.com/test/dev10/?_wv=133120&log=yes")
#driver.find_element_by_id("layaCanvas").send_keys("selenium2")

sleep(5)
driver.save_screenshot("d:\imgtest\scree.jpg")
body = driver.find_element_by_tag_name("body")
print ("cap ok!")
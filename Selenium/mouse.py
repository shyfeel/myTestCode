#coding=utf-8
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

chromedriver = "D:\github\myTestCode\Selenium\chromedriver.exe"
os.environ["webdriver.chrome.driver"] = chromedriver

driver = webdriver.Chrome(chromedriver)
driver.get("http://www.shyfeel.com/mouse/")
#driver.find_element_by_id("layaCanvas").send_keys("selenium2")
layaCanvas = driver.find_element_by_id("layaCanvas")
sleep(10)
ActionChains(driver).move_to_element_with_offset(layaCanvas, 100, 100).click().perform()
#driver.quit()
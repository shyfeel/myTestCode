#coding=utf-8
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chromedriver = "D:\github\myTestCode\Selenium\chromedriver.exe"
os.environ["webdriver.chrome.driver"] = chromedriver

driver = webdriver.Chrome(chromedriver)
driver.get("http://www.baidu.com")
driver.find_element_by_id("kw").send_keys("selenium2")
driver.find_element_by_id("su").click()
#driver.quit()
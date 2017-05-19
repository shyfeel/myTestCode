#coding=utf-8
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

chromedriver = "D:\github\myTestCode\Selenium\chromedriver.exe"
os.environ["webdriver.chrome.driver"] = chromedriver

driver = webdriver.Chrome(chromedriver)
driver.get("http://literallycanvas.com/")
#driver.find_element_by_id("layaCanvas").send_keys("selenium2")
canvas = driver.find_element_by_tag_name("canvas");
#ActionChains(driver).move_to_element_with_offset(canvas, 0, 0).click_and_hold().drag_and_drop_by_offset(canvas,200,200).perform()
ActionChains(driver).click_and_hold(canvas).move_by_offset(10, 50).move_by_offset(50, 10).move_by_offset(-10, -50).move_by_offset(-50, -10).release().perform();
Thread.sleep(3000);
#driver.quit()


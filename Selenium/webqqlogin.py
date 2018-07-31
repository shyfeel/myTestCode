# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class Webqqlogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://xui.ptlogin2.qq.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_webqqlogin(self):
        driver = self.driver
        driver.get(self.base_url + "/cgi-bin/xlogin?appid=716027609&pt_3rd_aid=1105820955&daid=383&pt_skey_valid=0&style=35&s_url=http%3A%2F%2Fconnect.qq.com&refer_cgi=authorize&which=&display=mobile&scope=all&response_type=code&client_id=1105820955&state=1508743226301&redirect_uri=http%3A%2F%2Fres.luckyfish.qq.com%2Ftest%2Fdev10%2F%3F_wv%3D133120%26log%3Dyes")
        driver.find_element_by_id("u").clear()
        driver.find_element_by_id("u").send_keys("13117319")
        driver.find_element_by_id("p").clear()
        driver.find_element_by_id("p").send_keys("test1234")
        driver.find_element_by_id("go").click()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()

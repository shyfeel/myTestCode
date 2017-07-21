from selenium import webdriver
driver = webdriver.PhantomJS()
driver.get("http://www.shyfeel.com/admin/login.php")
#data = driver.title
driver.find_element_by_xpath('//*[@id="name"]').send_keys('admin')
driver.find_element_by_xpath('//*[@id="password"]').send_keys('wxwshdtddh')
driver.find_element_by_xpath('/html/body/div/div/form/p[3]/button').click()
cookie_list = driver.get_cookies()
print cookie_list

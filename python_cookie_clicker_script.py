from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("http://orteil.dashnet.org/cookieclicker/")
elem = driver.find_element_by_id("bigCookie")
while (True):
	elem.click()
	



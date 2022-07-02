from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Safari()

driver.get('http://google.com')
driver.refresh()
# driver.find_element_by_name("q").send_keys("python")

driver.find_element(By.NAME, "q").send_keys("python")
driver.find_element()
# driver.quit() - close browser
# driver.close() - close current tab
# driver.back()
# driver.refresh
# drive.forward


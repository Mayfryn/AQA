import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://google.com/')

# els = driver.find_element(By.CLASS_NAME, "gLFyf")
# els.send_keys("python")
# els.click()

els = driver.find_elements(By.CLASS_NAME, "gLFyf")
print(els)
els[0].send_keys("python")

# els = driver.find_elements(By.CSS_SELECTOR, "gLFyf")
# print(els)
# els[0].send_keys("python")

time.sleep(3)

button = driver.find_elements(By.CLASS_NAME, "gNO89b")
button[0].click()

els = driver.find_elements(By.PARTIAL_LINK_TEXT, "Python")
print(len(els))

# driver.quit()

from selenium import webdriver
import time

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(5)

driver.get("https://the-internet.herokuapp.com/windows")
driver.find_element(By.LINK_TEXT,"Click Here").click()
windowsopened = driver.window_handles   # return window open list

driver.switch_to.window(windowsopened[1])
print(driver.find_element(By.TAG_NAME,"h3").text)   # New Window
driver.close()
driver.switch_to.window(windowsopened[0])
print(driver.find_element(By.TAG_NAME,"h3").text)   # Opening a new window
assert "Opening a new window" == driver.find_element(By.TAG_NAME,"h3").text










time.sleep(10)
from selenium import webdriver

import time

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#")

driver.find_element(By.XPATH,"//input[@type='search']").send_keys("ber")

# results = driver.find_element(By.CSS_SELECTOR,"div[ class='.products'] div")
results = driver.find_element(By.XPATH,"//div[@class='products']/div")
count = len(results)

assert count > 0

time.sleep(2)







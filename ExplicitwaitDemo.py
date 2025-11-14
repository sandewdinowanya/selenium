from selenium import webdriver
#-- Chrome
from selenium.webdriver.common.by import By

import time

from selenium.webdriver.ie.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()

driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#")

driver.find_element(By.XPATH,"//input[@type='search']").send_keys("ber")

time.sleep(2)
# results = driver.find_element(By.CSS_SELECTOR,"div[ class='.products'] div")
results = driver.find_elements(By.XPATH,"//div[@class='products']/div")
count = len(results)
assert count > 0
for result in results:
    result.find_element(By.XPATH,"div/button").click()
    time.sleep(1)

driver.find_element(By.CSS_SELECTOR,"img[alt='Cart']").click()   #15
driver.find_element(By.XPATH,"//button[text()='PROCEED TO CHECKOUT']").click()
driver.find_element(By.CSS_SELECTOR,".promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR,".promoBtn").click()
wait = WebDriverWait(driver,10) #set for 10s
wait.until(expected_conditions.presence_of_element_located(By.CSS_SELECTOR),".promoInfo")
success_msg =(driver.find_element(By.CSS_SELECTOR,".promoInfo").text)
assert success_msg == "Code applied ..!"
print(success_msg)
driver.find_element(By.XPATH,"//button[text()='Place Order']").click()










time.sleep(3)











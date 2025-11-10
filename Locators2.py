from selenium import webdriver

import time

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/client")

# test link text
driver.find_element(By.LINK_TEXT,"Forgot password?").click()


#no attribute be found unique then do parent travel or child travel
driver.find_element(By.XPATH,"//form/div[1]/input").send_keys("demo@gmail.com")

# driver.find_element(By.XPATH,"//form/div[2]/input").send_keys("12345")

#we can do the same thing by using CSS_SELECTOR
driver.find_element(By.CSS_SELECTOR,"form div:nth-child(2) input").send_keys("12345")


driver.find_element(By.XPATH,"//form/div[3]/input").send_keys("12345")

# driver.find_element(By.XPATH,'//button[@type="submit"]').click()

driver.find_element(By.XPATH,"//button[text()='Save New Password']").click()



time.sleep(5000)

import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://rahulshettyacademy.com/angularpractice/")

# driver.find_element(By.NAME,"")

driver.find_element(By.NAME,"name").send_keys("helloworld")
driver.find_element(By.NAME,"email").send_keys("helloworld@gmail.com")
driver.find_element(By.ID,"exampleInputPassword1").send_keys("123456")
driver.find_element(By.ID,"exampleCheck1").click()



time.sleep(500 )
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

#Xpath - //tagname[@attribute='value']
       # //input[@type='submit']

#CSS Selector - tagname[@attribute='value']
            #input[@type='submit']
            # id
            # .classname


driver.find_element(By.CSS_SELECTOR, '#inlineRadio1').click()
driver.find_element(By.XPATH,"//input[@type='submit']").click()
message = driver.find_element(By.CLASS_NAME,"alert-success").text
print(message)
assert 'success' in message

driver.find_element(By.XPATH,'(//input[@type="text"])[3]').send_keys("helloworld")

time.sleep(500)
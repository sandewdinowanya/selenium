from selenium import webdriver

#chrome driver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# service_obj = Service("C:\Users\Hp\AppData\Local\Temp\chromedriver-win64\chromedriver-win64.exe")
# driver = webdriver.Chrome(service=service_obj)

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
action = ActionChains(driver)
#action.double_click(driver.find_element(By.))
#action.context_click()  #right click
#action.drag_and_drop()
action.move_to_element(driver.find_element(By.ID,"mousehover")).perform()
time.sleep(2)
#action.context_click(driver.find_element(By.LINK_TEXT,"Top")).perform()
action.move_to_element(driver.find_element(By.LINK_TEXT,"Reload")).click().perform()









time.sleep(500)
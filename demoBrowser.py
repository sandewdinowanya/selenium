import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

#step one
#Chrome driver service Selenium 160->160 chrome driver
# service_obj = Service("C:\Users\Hp\AppData\Local\Temp\chromedriver-win64\chromedriver-win64.exe")
# driver = webdriver.chrome(service=service_obj)



#step two
driver = webdriver.Chrome()
driver.get("https://www.github.com")

# maximize window
driver.maximize_window()
print(driver.title)
print(driver.current_url)


driver.quite()























time.sleep(2)
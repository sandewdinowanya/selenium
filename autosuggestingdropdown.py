
from selenium import webdriver
import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("http://rahulshettyacademy.com/dropdownsPractise/")
driver.find_element(By.ID, "autosuggest").send_keys("ind")

time.sleep(2)

countries = driver.find_elements(By.CSS_SELECTOR, "li[class='ui-menu-item'] a")

print(len(countries))

# time.sleep(2000)

for country in countries:
    if country.text == "India":
            country.click()
            break

#print(driver.find_element(By.ID,"autosuggest").text)   #not work

print(driver.find_element(By.ID,"autosuggest").get_attribute("value"))

assert driver.find_element(By.ID,"autosuggest").get_attribute("value") == "India"




















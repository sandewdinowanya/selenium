from selenium import webdriver
import time

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("http://rahulshettyacademy.com/AutomationPractice/")

# driver.find_element(By.XPATH, "(//input[@type='checkbox'])[2]").click()

checkboxes = driver.find_elements(By.XPATH, "(//input[@type='checkbox'])")

for checkbox in checkboxes:
    if checkbox.get_attribute("value") == "option2":
        checkbox.click()
        assert checkbox.is_selected()
        break

points = driver.find_elements(By.XPATH,"//input[@type='radio']")

for point in points:
    if point.get_attribute("value") == "radio2":
        point.click()
        assert point.is_selected()
        break

assert driver.find_element(By.ID, "displayed-text").is_displayed()
driver.find_element(By.ID,"hide-textbox").click()
assert not driver.find_element(By.ID,"displayed-text").is_displayed()

time.sleep(5)


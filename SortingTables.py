from selenium import webdriver
import time

from selenium.webdriver.common.by import By

browserSortedVeggies = []
driver = webdriver.Chrome()
driver.implicitly_wait(10)

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")
# click on column header
driver.find_element(By.XPATH,"//span[text()='Veg/fruit name']").click()

# collect all veggie names -> BrowserSortedList  (A,B,C)   (B,A,C)  If there is a bug we will catch by this ->
veggieWebElements = driver.find_elements(By.XPATH,"//tr/td[1]")
for ele in veggieWebElements:
    browserSortedVeggies.append(ele.text)

originalBrowserSortedList = browserSortedVeggies.copy()

# Sort this veggieList => newSortedList   -> (A,B,C)  ->
browserSortedVeggies.sort()

#veggieList == neSortedList
assert browserSortedVeggies == originalBrowserSortedList








time.sleep(30)
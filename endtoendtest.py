from selenium import webdriver
from selenium.webdriver.common.by import By

#chrome driver
driver = webdriver.Chrome()

driver.get("https://rahulshettyacademy.com/angularpractice/")

driver.implicitly_wait(4)

# //a[contains(@href,'shop')]  css selector -> a[href*='shop']
driver.find_element(By.CSS_SELECTOR, "a[href*='shop']").click()

products =driver.find_elements(By.XPATH,"//div[@class='card h-100']")

for product in products:
    product_name=product.find_element(By.XPATH,"div/h4/a").text
    if product_name =='Blackberry':
        product.find_element(By.XPATH,"div/button").click()

driver.find_element(By.CSS_SELECTOR, "a[class*='btn-primary']").click()
driver.find_element(By.XPATH," //button[@class='btn btn-success']").click()
driver.find_element(By.ID,"country").send_keys("ind")


print("Success")
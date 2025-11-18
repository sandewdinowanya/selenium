from selenium import webdriver
import time

from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("headless")
chrome_options.add_argument("--ignore-certificate-errors")


driver = webdriver.Chrome(options=chrome_options)
driver.implicitly_wait(10)

driver.get("https://rahulshettyacademy.com/angularpractice/")

print(driver.title)













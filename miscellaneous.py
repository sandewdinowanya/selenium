from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

driver.execute_script("window.scrollBy(0,document.body.scrollHeight);")
driver.execute_script("window.scrollTo(0,500)")
# driver.get_screenshot_as_file("screen.png")
driver.get_screenshot_as_png()













time.sleep(50)
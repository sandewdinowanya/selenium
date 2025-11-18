from selenium import webdriver
import time

#headless mode
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('headless')

chrome_options.add_argument("--ignore-certificate-errors")

driver = webdriver.Chrome(options=chrome_options)
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

driver.execute_script("window.scrollBy(0,document.body.scrollHeight);")
driver.execute_script("window.scrollTo(0,500)")
# driver.get_screenshot_as_file("screen.png")
driver.get_screenshot_as_png()














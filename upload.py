# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# file_path = r"C:\\Users\\Hp\\PycharmProjects\\PythonTesting\\selenium\\Book1.xlsx"
#
# fruit_name="apple"
#
# service = Service()
# options = Options()
#
# driver = webdriver.Chrome()
# driver.implicitly_wait(5)
# driver.get("https://rahulshettyacademy.com/upload-download-test/index.html")
#
# driver.find_element(By.ID, "downloadButton").click()
#
# # Upload the edited excel
# file_input = driver.find_element(By.CSS_SELECTOR, "input[type='file']")
# file_input.send_keys(file_path)
#
# wait = WebDriverWait(driver, 5)
# toast_locator = (By.CSS_SELECTOR, ".Toastify__toast-body div:nth-child(2)")
#
# wait.until(EC.visibility_of_element_located(toast_locator))
# print(driver.find_element(*toast_locator).text)
# priceColumn = driver.find_element(By.XPATH,"//div[text()='Price']").get_attribute("data-column-id")
# actual_price = driver.find_element(By.XPATH("//div[text()='"+fruit_name+"']/parent::div/parent::div/div[@id='cell-"+priceColumn+"-undefined']")).text
# print(actual_price)


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

file_path = r"C:\\Users\\Hp\\PycharmProjects\\PythonTesting\\selenium\\Book1.xlsx"

fruit_name = "apple"

# Remove the unused service and options or configure them
options = Options()
# options.add_argument('--headless')  # Add options if needed

driver = webdriver.Chrome(options=options)  # Or just webdriver.Chrome()
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/upload-download-test/index.html")

driver.find_element(By.ID, "downloadButton").click()

# Upload the edited excel
file_input = driver.find_element(By.CSS_SELECTOR, "input[type='file']")
file_input.send_keys(file_path)

wait = WebDriverWait(driver, 5)
toast_locator = (By.CSS_SELECTOR, ".Toastify__toast-body div:nth-child(2)")

wait.until(EC.visibility_of_element_located(toast_locator))
print(driver.find_element(*toast_locator).text)

priceColumn = driver.find_element(By.XPATH, "//div[text()='Price']").get_attribute("data-column-id")

# Fixed XPath syntax error (you had By.XPATH(...) instead of By.XPATH, "...")
actual_price = driver.find_element(By.XPATH, "//div[text()='"+fruit_name+"']/parent::div/parent::div/div[@id='cell-"+priceColumn+"-undefined']").text
print(actual_price)

driver.quit()  # Don't forget to close the browser
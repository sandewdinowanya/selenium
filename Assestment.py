
from selenium import webdriver
import time

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(10)

driver.get("https://rahulshettyacademy.com/seleniumPractise/#")

driver.find_element(By.XPATH, "//input[@type='search']").send_keys("ber")
time.sleep(2)

products = driver.find_elements(By.XPATH,"//div[@class='products']/div")

# expected products to display on the webpage
expected_products = []
for product in products:
    product_name = product.find_element(By.XPATH,"//h4[@class='product-name']").text
    expected_products.append(product_name)
print("Expected result : ", expected_products)

# actual products in the web page
actual_results = []
for product in products:
    assert product_name in expected_products
    actual_results.append(product_name)
print("Actual result : ", actual_results)

#add products to the cart
for product in products:
    product.find_element(By.XPATH,"//button[text()='ADD TO CART']").click()


# open cart
driver.find_element(By.XPATH,"//img[@alt='Cart']").click()
# proceed to checkout
driver.find_element(By.XPATH,"//button[text()='PROCEED TO CHECKOUT']").click()
time.sleep(5)
# give promo code
driver.find_element(By.XPATH,"//input[@class='promoCode']").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR,".promoBtn").click()
# success_msg
msg = driver.find_element(By.CSS_SELECTOR,".promoInfo").text
print(msg)
# total amount
total_amount = driver.find_element(By.CSS_SELECTOR,".totAmt").text
total_after_discount = driver.find_element(By.CSS_SELECTOR,".discountAmt").text

assert total_amount > total_after_discount
print("Total amount : ", total_amount)

time.sleep(5)
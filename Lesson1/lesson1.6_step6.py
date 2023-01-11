from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    link = "http://suninjuly.github.io/huge_form.html"
    browser = webdriver.Chrome()
    browser.get(link)

    elements = browser.find_elements(By.CSS_SELECTOR, "input[type='text']")
    for element in elements:
        element.send_keys("ответ")

    button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

finally:
    time.sleep(20)
    browser.quit()
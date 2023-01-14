# скролл страницы до появления элемента

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
link = "http://suninjuly.github.io/execute_script.html"
browser = webdriver.Chrome()
browser.get(link)

try:
    znachenie_x = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = znachenie_x.text
    y = calc(x)
    print(y)
    # input1 = browser.find_element(By.CSS_SELECTOR, "#answer").send_keys(y)

    input1 = browser.find_element(By.CSS_SELECTOR, "#answer")
    input1.send_keys(y)

    input2 = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    input2.click()

    input3 = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    browser.execute_script("return arguments[0].scrollIntoView(true);", input3) # скролл страницы до появления элемента
    input3.click()

    input4 = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    # browser.execute_script("return arguments[0].scrollIntoView(true);", input4)
    input4.click()
finally:
    time.sleep(10)
    browser.quit()
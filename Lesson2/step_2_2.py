from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import math
import time

def calc (x, y):
    return x + y

try:
    link = "https://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Num1 = browser.find_element(By.CSS_SELECTOR, "#num1").text
    # Num2 = browser.find_element(By.CSS_SELECTOR, "#num2").text
    Sum = int(browser.find_element(By.CSS_SELECTOR, "#num1").text) + int(browser.find_element(
        By.CSS_SELECTOR, "#num2").text)


    # Арифметика
    # x = int(Num1)
    # y = int(Num2)
    # Sum = calc(x, y)
    # print(Sum)
    # Sum1 = str(Sum)
    # Выбор с селекторе нужное значение

    select = Select(browser.find_element(By.CSS_SELECTOR, "#dropdown"))
    select.select_by_value(str(Sum))

    Button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

finally:
    time.sleep(10)
    browser.quit()


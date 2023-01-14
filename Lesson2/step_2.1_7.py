from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
  link = "http://suninjuly.github.io/get_attribute.html"
  browser = webdriver.Chrome()
  browser.get(link)

  x_element = browser.find_element(By.CSS_SELECTOR, "#treasure")
  x_element1 = x_element.get_attribute("valuex")
  x = x_element1
  print("Значение атрибута", x_element1)
  y = calc(x)

  input1 = browser.find_element(By.CSS_SELECTOR, "#answer").send_keys(y)
  checkbox = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox").click()
  radio = browser.find_element(By.CSS_SELECTOR, "#robotsRule").click()
  button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
  assert x is not None, "Значение Х отсутствует"
finally:
  time.sleep(20)
  browser.quit()

from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
  link = "https://suninjuly.github.io/math.html"
  browser = webdriver.Chrome()
  browser.get(link)

  x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
  x = x_element.text
  y = calc(x)

  input1 = browser.find_element(By.CSS_SELECTOR, "#answer").send_keys(y)
  checkbox = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox").click()
  radio = browser.find_element(By.CSS_SELECTOR, "#robotsRule").click()
  button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

finally:
  time.sleep(20)
  browser.quit()

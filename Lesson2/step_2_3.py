from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
import pyperclip

link1 = "http://suninjuly.github.io/alert_accept.html"
browser1 = webdriver.Chrome()
browser1.get(link1)

try:
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))



    button1 = browser1.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    confirm = browser1.switch_to.alert
    confirm.accept()

    input1 = browser1.find_element(By.CSS_SELECTOR, "#input_value").text
    x = int(input1)
    y = calc(x)

    input2 = browser1.find_element(By.CSS_SELECTOR, "#answer")
    input2.send_keys(y)

    button2 = browser1.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    # alert = browser1.switch_to.alert
    # alert_text = alert.text
    # text_copy = alert_text.split(': ')[-1]
    # pyperclip.copy(text_copy)

    # print(text_copy)

finally:
    time.sleep(10)
    browser1.quit()

    # link2 = "https://stepik.org/lesson/184253/step/4?unit=158843"
    # browser2 = webdriver.Chrome()
    # browser2.get(link2)
    # time.sleep(2)
    #
    #
    # browser2.quit()

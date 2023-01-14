import math

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/redirect_accept.html"
browser = webdriver.Chrome()
browser.get(link)

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
try:
    button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    new_window = browser.window_handles[1] #Узнаем имя новой вкладки
    browser.switch_to.window(new_window) #переключиться на новую вкладку

    input1 = browser.find_element(By.CSS_SELECTOR, "#input_value").text
    x = int(input1)
    y = calc(x)
    input2 = browser.find_element(By.CSS_SELECTOR, "[name='text']").send_keys(y)
    input3 = browser.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    alert = browser.switch_to.alert #переключиться на окно
    alert_text = alert.text #использовать текст(скопировать)
    text_copy = alert_text.split(": ")[-1] #Скопировать текст в определенном месте, в данном случае после ': '
    print(text_copy)

    first_window = browser.window_handles[0] #Узнаем имя новой вкладки
    browser.switch_to.window(first_window) #переключиться на начальную вкладку


finally:
    time.sleep(4)
    browser.quit()
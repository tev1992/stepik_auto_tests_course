from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/registration2.html"
browser = webdriver.Chrome()
browser.get(link)

try:
    #Заполнение обязательных полей
    First_name = browser.find_element(By.CSS_SELECTOR, ".first[required]").send_keys("Имя")
    Last_name = browser.find_element(By.CSS_SELECTOR, ".second[required]").send_keys("Фамилия")
    Email = browser.find_element(By.CSS_SELECTOR, ".third[required]").send_keys("Email")
    button = browser.find_element(By.CSS_SELECTOR, "[type*='submit']").click()
    proverka = browser.find_element(By.CSS_SELECTOR, "h1").text
    proverka1 = "Congratulations! You have successfully registered!"
    assert proverka1 == proverka, f"тест не пройден, текст отображается другой - {proverka}"
    # time.sleep(3)
    # browser.back()

    #Проверка валидации - не проверять
    # First_name1 = browser.find_element(By.CSS_SELECTOR, ".first[placeholder*='name']").clear()
    # Last_name2 = browser.find_element(By.CSS_SELECTOR, ".second[placeholder*='name']").clear()
    # Email3 = browser.find_element(By.CSS_SELECTOR, ".third[placeholder*='email']").clear()
    # Phone = browser.find_element(By.CSS_SELECTOR, "input[type = 'text'][placeholder*='phone']").send_keys("111")
    # button1 = browser.find_element(By.CSS_SELECTOR, "[type*='submit']").click()
    # proverka2 = browser.find_element(By.CSS_SELECTOR, "h1").text
    # proverka3 = "Congratulations! You have successfully registered!"
    # assert proverka2 != proverka3, f"валидаия не работает"

finally:
    time.sleep(5)
    browser.quit()


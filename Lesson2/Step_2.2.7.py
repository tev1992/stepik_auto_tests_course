# Задание: загрузка файла

from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time

# Пример кода, который позволяет указать путь к файлу 'file1.txt',
# current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
# file_path = os.path.join(current_dir, 'file1.txt')           # добавляем к этому пути имя файла
# element.send_keys(file_path)

link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
browser.get(link)

try:
    # ввод значений в поля
    imput2 = browser.find_elements(By.CSS_SELECTOR, "input[type='text']")
    for imput1 in imput2:
        imput1.send_keys("тестовые данные")

    # загрузка файла
    # load_file = browser.find_element(By.CSS_SELECTOR, "#file")
    # current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    # file_path = os.path.join(current_dir, "file1.txt") # добавляем к этому пути имя файла
    # load_file.send_keys(file_path)

    # загрузка изображения
    load_image = browser.find_element(By.CSS_SELECTOR, "#file")
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, "image1.jpg")
    load_image.send_keys(file_path)

    button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

finally:

    time.sleep(10)
    browser.quit()
assert abs(-42) == 42, "Значение не соответствует"

# Если вы проверяете наличие элемента, то обязательно пишите, что это за элемент по смыслу на странице:

# assert self.is_element_present('create_class_button', timeout=30), "No create class button"


# Форматирование строк с помощью конкатенации

actual_result = "abrakadabra"
print("Wrong text, got " + actual_result + ", something wrong")

# Форматирование строк с помощью str.format

print("Let's count together: {}, then goes {}, and then {}".format("one", "two", "three"))

# Форматирование строк с помощью f-strings

str1 = "one"
str2 = "two"
str3 = "three"
print(f"Let's count together: {str1}, then goes {str2}, and then {str3}")

# catalog_text = self.catalog_link.text # считываем текст и записываем его в переменную
# assert catalog_text == "Каталог", \
#     f"Wrong language, got {catalog_text} instead of 'Каталог'"


s = 'My Name is Julia'

if 'Name' in s:
    print('Substring found')

index = s.find('Name')
if index != -1:
    print(f'Substring found at index {index}')


# assert "login" in browser.current_url,  # сообщение об ошибке
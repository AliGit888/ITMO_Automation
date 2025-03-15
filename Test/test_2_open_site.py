from selenium.webdriver.commom.by import By
from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://demoqa.com/')

# поиск элемeнта
icon = driver.find_element(By.CSS_SELECTOR,'header > a > img') #переменная iconб к которой обращаемся через драйвер с помощью метода find_element(первым эл-том передаём тип поиска,вторым тип локатора, который будем искать)
if icon is None:
    print('Элемент не найден')
else:
    print('Элемент найден')
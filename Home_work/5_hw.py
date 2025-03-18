from selenium import webdriver
from selenium.webdriver.common.by import By

def open_site():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")

def find_element(driver):
    username_field = driver.find_element(By.ID, "user-name")
    password_field = driver.find_element(By.ID, "password")
    login_button = driver.find_element(By.ID, "login-button")

def check_element(username_field,password_field,login_button):
    if username_field and password_field and login_button is None:
        print("Элемент(ы) не найдены")
    else:
        print("Элементы найдены")


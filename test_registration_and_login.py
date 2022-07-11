#   Проверяем возможность регистрации и дальнейшей авторизации на сайте "ParaBank"

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from colorama import init, Fore, Back, Style

#   Регистрация
Username = input(Fore.GREEN + 'Введите Username:')
Password = input(Fore.GREEN + 'Введите Password:')

browser = webdriver.Chrome()

browser.get('https://parabank.parasoft.com/parabank/index.htm')

time.sleep(2)

browser.find_element(By.CSS_SELECTOR, '#loginPanel > p:nth-child(3) > a').click()

time.sleep(1)

browser.find_element(By.CSS_SELECTOR, '#customer\.firstName').send_keys('Ivan')
browser.find_element(By.CSS_SELECTOR, '#customer\.lastName').send_keys('Ivanov')
browser.find_element(By.CSS_SELECTOR, '#customer\.address\.street').send_keys('Lenina, 1')
browser.find_element(By.CSS_SELECTOR, '#customer\.address\.city').send_keys('Ekaterinburg')
browser.find_element(By.CSS_SELECTOR, '#customer\.address\.state').send_keys('Russia')
browser.find_element(By.CSS_SELECTOR, '#customer\.address\.zipCode').send_keys('225864')
browser.find_element(By.CSS_SELECTOR, '#customer\.phoneNumber').send_keys('89221860699')
browser.find_element(By.CSS_SELECTOR, '#customer\.ssn').send_keys('12345678901')
browser.find_element(By.CSS_SELECTOR, '#customer\.username').send_keys(Username)
browser.find_element(By.CSS_SELECTOR, '#customer\.password').send_keys(Password)
browser.find_element(By.CSS_SELECTOR, '#repeatedPassword').send_keys(Password)
browser.find_element(By.CSS_SELECTOR, '#customerForm > table > tbody > tr:nth-child(13) > td:nth-child(2)'
                                      ' > input').click()

time.sleep(1)

RegistrationText1 = browser.find_element(By.CSS_SELECTOR, '#rightPanel > p')
RegistrationText = RegistrationText1.text

if RegistrationText == 'Your account was created successfully. You are now logged in.':
    print(Fore.CYAN + 'Регистрация успешно пройдена')
else:
    print(Fore.RED + 'Ошибка регистрации')

# Авторизация

browser.find_element(By.CSS_SELECTOR, '#leftPanel > ul > li:nth-child(8) > a').click()

time.sleep(1)

browser.find_element(By.CSS_SELECTOR, '#loginPanel > form > div:nth-child(2) > input').send_keys(Username)
browser.find_element(By.CSS_SELECTOR, '#loginPanel > form > div:nth-child(4) > input').send_keys(Password)
browser.find_element(By.CSS_SELECTOR, '#loginPanel > form > div:nth-child(5) > input').click()

WelcomeText1 = browser.find_element(By.CSS_SELECTOR, '#leftPanel > p > b')
WelcomeText = WelcomeText1.text

if WelcomeText == 'Welcome':
    print(Fore.CYAN + 'Авторизация успешно пройдена')
else:
    print(Fore.RED + 'Ошибка регистрации')

browser.quit()

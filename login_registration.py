from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
####Тест для регистрации
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)
driver.get('http://practice.automationtesting.in/')

menu_btn = driver.find_element_by_id('menu-item-50')
menu_btn.click()

reg_mail = driver.find_element_by_id('reg_email')
reg_mail.send_keys('fitz994@mail.ru')

time.sleep(3)

reg_pass = driver.find_element_by_id('reg_password')
reg_pass.send_keys('sk8erboy94')

reg_btn = driver.find_element_by_class_name('woocommerce-Button.button')
reg_btn.click()

driver.quit()



####Тест для входа
from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)
driver.get('http://practice.automationtesting.in/')

menu_btn = driver.find_element_by_id('menu-item-50')
menu_btn.click()

log_mail = driver.find_element_by_id('username')
log_mail.send_keys('fitz994@mail.ru')

log_pass = driver.find_element_by_id('password')
log_pass.send_keys('sk8erboy94')

log_btn = driver.find_element_by_css_selector('[value="Login"]')
log_btn.click()

driver.quit()
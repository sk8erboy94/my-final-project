from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)
driver.get('http://practice.automationtesting.in/')

driver.execute_script("window.scrollBy(0, 600);")

read_more_btn = driver.find_element_by_css_selector('[data-product_id="160"]')
read_more_btn.click()

reviews_btn = driver.find_element_by_class_name('reviews_tab')
reviews_btn.click()

star5_btn = driver.find_element_by_class_name('star-5')
star5_btn.click()

comment = driver.find_element_by_id('comment')
comment.send_keys('Nice book!')

name = driver.find_element_by_id('author')
name.send_keys('Ilya')

email = driver.find_element_by_id('email')
email.send_keys('fitz994@mail.ru')

submit_btn = driver.find_element_by_class_name('submit')
submit_btn.click()

driver.quit()


####Отображение страницы товара
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

shop_btn = driver.find_element_by_id('menu-item-40')
shop_btn.click()

book_HTML = driver.find_element_by_css_selector('[title="Mastering HTML5 Forms"]')
book_HTML.click()

book_name = driver.find_element_by_css_selector('.product_title.entry-title')
book_name_text = book_name.text

assert book_name_text == "HTML5 Forms"

driver.quit()


####Количество товаров в категории
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

shop_btn = driver.find_element_by_id('menu-item-40')
shop_btn.click()

HTML_btn = driver.find_element_by_link_text('HTML')
HTML_btn.click()

items_count = driver.find_elements_by_class_name('price')

if len(items_count) == 3:
    print('На странице отображается 3 товара')
else:
    print('Ошибка. Количество товаров равно ' + str(len(items_count)))

driver.quit()


####Сортировка товаров
from selenium import webdriver
from selenium.webdriver.support.select import Select

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

shop_btn = driver.find_element_by_id('menu-item-40')
shop_btn.click()

default_sort = driver.find_element_by_css_selector('[value="menu_order"]')
default_sort_sel = default_sort.get_attribute('selected')
if default_sort_sel is not None:
    print('Выбран вариант сортировки по умолчанию')
else:
    print('Ошибка. Выбран другой селектор')


element = driver.find_element_by_css_selector('[name="orderby"]')
select = Select(element)
select.select_by_index(5)

high_to_low = driver.find_element_by_css_selector('[value="price-desc"]')
high_to_low_sel = high_to_low.get_attribute('selected')
if high_to_low_sel is not None:
    print('Выбран селектор "От большего к меньшему"')
else:
    print('Ошибка. Выбран другой селектор')

driver.quit()


####Отображение, скидка товара
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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

shop_btn = driver.find_element_by_id('menu-item-40')
shop_btn.click()

book_android = driver.find_element_by_css_selector('[title="Android Quick Start Guide"]')
book_android.click()

old_price = driver.find_element_by_css_selector('del>:nth-child(1)')
old_price_text = old_price.text
assert old_price_text == '₹600.00'
new_price = driver.find_element_by_css_selector('ins>:nth-child(1)')
new_price_text = new_price.text
assert new_price_text == '₹450.00'

wait = WebDriverWait(driver, 10)

image = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[title="Android Quick Start Guide"]')))
image.click()

image2 = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'pp_close')))
image2.click()

driver.quit()


####Проверка цены в корзине

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)
driver.get('http://practice.automationtesting.in/')

shop_btn = driver.find_element_by_id('menu-item-40').click()

add_basket = driver.find_element_by_css_selector('[data-product_id="182"]').click()

basket = driver.find_element_by_css_selector('[href="http://practice.automationtesting.in/basket/"]').click()

item = driver.find_element_by_class_name('cartcontents')
item_count = item.text
assert item_count == '1 Item'

price = driver.find_element_by_class_name('amount')
price_count = price.text
assert price_count == '₹180.00'

wait = WebDriverWait(driver, 10)

subtotal = wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, '.product-price>.woocommerce-Price-amount.amount'), '₹180.00'))

total = wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, '.order-total>[data-title="Total"]>strong'), '₹189.00'))

driver.quit()


####Работа в корзине
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)
driver.get('http://practice.automationtesting.in/')

shop_btn = driver.find_element_by_id('menu-item-40').click()

driver.execute_script("window.scrollBy(0, 300);")

add_basket = driver.find_element_by_css_selector('[href="/shop/?add-to-cart=182"]').click()

time.sleep(3)

add_basket_2 = driver.find_element_by_css_selector('[href="/shop/?add-to-cart=180"]').click()

time.sleep(3)

basket = driver.find_element_by_css_selector('[href="http://practice.automationtesting.in/basket/"]').click()

delete = driver.find_element_by_css_selector('[data-product_id="182"]').click()

undo = driver.find_element_by_link_text('Undo?').click()

quantity = driver.find_element_by_css_selector('[name="cart[045117b0e0a11a242b9765e79cbf113f][qty]"]')
quantity.clear()
quantity.send_keys('3')

update_btn = driver.find_element_by_css_selector('[name="update_cart"]').click()

quantity_value = quantity.get_attribute('value')
assert quantity_value == '3'

time.sleep(3)

apply_btn = driver.find_element_by_css_selector('[name="apply_coupon"]').click()

coupon = driver.find_element_by_class_name('woocommerce-error')
coupon_error = coupon.text
assert coupon_error == 'Please enter a coupon code.'

driver.quit()


####Покупка товара. (ФИНАЛОЧКА!!!)
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)
driver.get('http://practice.automationtesting.in/')

wait = WebDriverWait(driver, 10)

shop_btn = driver.find_element_by_id('menu-item-40').click()

driver.execute_script("window.scrollBy(0, 300);")

add_basket = driver.find_element_by_css_selector('[href="/shop/?add-to-cart=182"]').click()

basket = driver.find_element_by_css_selector('[href="http://practice.automationtesting.in/basket/"]').click()

checkout = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[href="http://practice.automationtesting.in/checkout/"]'))).click()

first_name = wait.until(EC.element_to_be_clickable((By.ID, 'billing_first_name'))).send_keys('Ilya')

last_name = driver.find_element_by_id('billing_last_name').send_keys('Voinov')

email = driver.find_element_by_id('billing_email').send_keys('fitz994@mail.ru')

phone = driver.find_element_by_id('billing_phone').send_keys('12345678910')

country = driver.find_element_by_id('select2-chosen-1').click()

country_2 = driver.find_element_by_class_name('select2-input').send_keys('Russia')

country_res = driver.find_element_by_id('select2-results-1').click()

adress = driver.find_element_by_id('billing_address_1').send_keys('Mira street')

town = driver.find_element_by_id('billing_city').send_keys('Severodvinsk')

state = driver.find_element_by_id('billing_state').send_keys('Arhangelskaya obl')

postcode = driver.find_element_by_id('billing_postcode').send_keys('165500')

driver.execute_script("window.scrollBy(0, 600);")

time.sleep(3)

check_payments = driver.find_element_by_id('payment_method_cheque').click()

place_order = driver.find_element_by_id('place_order').click()

thanks = driver.find_element_by_class_name('woocommerce-thankyou-order-received')
thanks_text = thanks.text
assert thanks_text == 'Thank you. Your order has been received.'

method = driver.find_element_by_class_name('method')
method_text = method.text
assert 'Check Payments' in method_text

driver.quit()

import time

from selenium import webdriver
from selenium.webdriver.common.by import By

chrome = webdriver.Chrome()

'''chrome.get("https://formy-project.herokuapp.com/")
component1 = chrome.find_element(By.LINK_TEXT, "Buttons")
component1.click()
component2 = chrome.find_element(By.LINK_TEXT, "Checkbox")
component2.click()
component3 = chrome.find_element(By.LINK_TEXT, "Datepicker")
component3.click()

chrome.get("https://the-internet.herokuapp.com/")
tab1 = chrome.find_element(By.PARTIAL_LINK_TEXT, "Dynamic")
tab1.click()

tab2 = chrome.find_element(By.PARTIAL_LINK_TEXT, "Add")
tab2.click()

tab3 = chrome.find_element(By.PARTIAL_LINK_TEXT, "Basic")

chrome.get("https://formy-project.herokuapp.com/autocomplete")
address_field1 = chrome.find_element(By.ID,"autocomplete")
address_field1.send_keys("magnoliei")

state_field = chrome.find_element(By.ID, "administrative_area_level_1")
state_field.send_keys("09")

postal_code_field = chrome.find_element(By.ID, "postal_code")
postal_code_field.send_keys("08")

chrome.get("https://www.techlistic.com/p/selenium-practice-form.html")

first_name_field = chrome.find_element(By.NAME, "firstname")
first_name_field.send_keys("ioana")
second_name_field = chrome.find_element(By.NAME, "lastname")
second_name_field.send_keys("Anghel")

chrome.get("https://the-internet.herokuapp.com/login")

username_field = chrome.find_element(By.NAME, "username")
username_field.send_keys("Gigel")

chrome.get("https://formy-project.herokuapp.com/autocomplete")
input_field = chrome.find_element(By.TAG_NAME, "input")
input_field.send_keys("joi")

chrome.get("https://phptravels.net/")
car_rental_button = chrome.find_element(By.TAG_NAME, "span")
car_rental_button.click()

chrome.get("https://formy-project.herokuapp.com/enabled")
disable_field = chrome.find_element(By.TAG_NAME, "input")
disable_field.click()

chrome.get("https://the-internet.herokuapp.com/checkboxes")
check_field = chrome.find_element(By.TAG_NAME, "form")
check_field.click()

chrome.get("https://the-internet.herokuapp.com/drag_and_drop")
drag_element = chrome.find_element(By.CLASS_NAME, "column")
print(drag_element)

chrome.get("https://formy-project.herokuapp.com/autocomplete")
button_field = chrome.find_element(By.CLASS_NAME, "navbar-brand")
print(button_field)
chrome.get("https://formy-project.herokuapp.com/keypress")
street2_field = chrome.find_element(By.CLASS_NAME, "form-control")
street2_field.send_keys("you")

chrome.get("https://formy-project.herokuapp.com/autocomplete")
address_field1 = chrome.find_element(By.CSS_SELECTOR,"#autocomplete")
address_field1.send_keys("magnoliei")

chrome.get("https://formy-project.herokuapp.com/autocomplete")
button_field = chrome.find_element(By.CSS_SELECTOR, ".navbar-brand")
print(button_field)

placeholder = chrome.find_element(By.CSS_SELECTOR, "input[placeholder*= Enter")
placeholder.send_keys("joi")'''

chrome.get("https://www.techlistic.com/p/selenium-practice-form.html")
name = chrome.find_element(By.XPATH, "//input[@name='firstname']")
name.send_keys("Mi")






time.sleep(3)